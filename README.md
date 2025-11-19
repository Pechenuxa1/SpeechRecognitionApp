# Speech recognition app
## Веб-приложение для распознавания речи из микрофона и автоматической трансляции в текст

### Для запуска требуется python3.13!

### Инструкция по запуску

#### 1. Склонируйте проект
git clone {url}

#### 2. Перейдите в корень проекта
cd {path}/SpeechRecognitionApp

#### 3. Скачайте модель vosk-model-small-ru-0.22.zip
https://alphacephei.com/vosk/models
или
https://github.com/kercre123/vosk-models

#### 4. Распакуйте zip-файл модели в папку {path}/SpeechRecognitionApp/model/

#### 5. Создайте виртуальное окружение
python -m venv venv

#### 6. Активируйте окружение
##### Windows:
venv\Scripts\activate
##### Linux/Mac:
source venv/bin/activate

#### 7. Установите зависимости
pip install -r requirements.txt

#### 8. Запустите веб-приложение
uvicorn main:app

#### 9. Откройте в браузере http://127.0.0.1:8000