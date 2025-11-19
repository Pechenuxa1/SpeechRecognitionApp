# Speech recognition app
## Веб-приложение для распознавания речи из микрофона и автоматической трансляции в текст

### Для запуска требуется python3.13!

### Инструкция по запуску

#### 1. Склонируйте проект
git clone {url}

#### 2. Перейдите в корень проекта
cd {path}/SpeechRecognitionApp

#### 3. Создайте виртуальное окружение
python -m venv venv

#### 4. Активируйте окружение
##### Windows:
venv\Scripts\activate
##### Linux/Mac:
source venv/bin/activate

#### 5. Установите зависимости
pip install -r requirements.txt

#### 6. Запустите веб-приложение
uvicorn main:app

#### 7. Откройте в браузере http://127.0.0.1:8000