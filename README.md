# Speech recognition app
## Веб-приложение для распознавания речи из микрофона и автоматической трансляции в текст

### Для запуска требуется python3.13!

### Инструкция по запуску

#### 1. Склонировать проект
git clone <url>

#### 2. Перейти в корень проекта
cd <path>/SpeechRecognitionApp

#### 3. Создать виртуальное окружение
python -m venv venv

#### 4. Активировать окружение
##### Windows:
venv\Scripts\activate
##### Linux/Mac:
source venv/bin/activate

#### 5. Установить зависимости
pip install -r requirements.txt

#### 6. Запустить веб-приложение
uvicorn main:app

#### 7. Открыть в браузере http://127.0.0.1:8000