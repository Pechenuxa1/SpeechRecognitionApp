import asyncio

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from speech_recognizer import SpeechRecognizer

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return FileResponse("static/index.html")


@app.websocket("/ws/recognize")
async def ws_recognize(websocket: WebSocket):
    await websocket.accept()

    r = SpeechRecognizer()
    send_task = None

    async def send_text():
        while r.is_recording:
            text = r.get_text()
            if text:
                await websocket.send_text(text)
            await asyncio.sleep(0.1)

    try:
        while True:
            data = await websocket.receive_text()
            if data == 'start' and not r.is_recording:
                r.start_recognition()
                send_task = asyncio.create_task(send_text())
            elif data == 'stop' and r.is_recording:
                r.stop_recognition()
                if send_task:
                    send_task.cancel()
                break
    except WebSocketDisconnect:
        r.stop_recognition()
        if send_task:
            send_task.cancel()

