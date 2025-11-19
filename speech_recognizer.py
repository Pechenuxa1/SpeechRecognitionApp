import threading
import queue
import json

from vosk import Model, KaldiRecognizer
import sounddevice as sd


class SpeechRecognizer:
    def __init__(self):
        self.is_recording = False
        self.audio_queue = queue.Queue()
        self.text_queue = queue.Queue()

        self.model = Model("model/vosk-model-small-ru-0.22")
        self.recognizer = KaldiRecognizer(self.model, 16000)

    def start_recognition(self):
        self.is_recording = True

        record_thread = threading.Thread(target=self._record_audio)
        record_thread.daemon = True
        record_thread.start()

        process_thread = threading.Thread(target=self._process_audio)
        process_thread.daemon = True
        process_thread.start()

    def stop_recognition(self):
        self.is_recording = False

    def _record_audio(self):
        def callback(indata, frames, time, status):
            if self.is_recording:
                self.audio_queue.put(indata.tobytes())

        with sd.InputStream(
            samplerate=16000,
            channels=1,
            callback=callback,
            blocksize=1024,
            dtype='int16'
        ):
            while self.is_recording:
                sd.sleep(100)

    def _process_audio(self):
        while self.is_recording:
            try:
                audio_data = self.audio_queue.get(timeout=0.1)
                if self.recognizer.AcceptWaveform(audio_data):
                    result = json.loads(self.recognizer.Result())
                    text = result.get("text", "")
                    if text:
                        self.text_queue.put(text)
            except queue.Empty:
                continue

    def get_text(self):
        try:
            return self.text_queue.get_nowait()
        except queue.Empty:
            return None
