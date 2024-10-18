import os
from flask import Blueprint, jsonify, request
from utils.text2image import Text2ImageAPI
from dotenv import load_dotenv
from config import Config
from router.improved_prompt import _get_adpromt

load_dotenv()
generate_image = Blueprint("generate_image", __name__)

def _get_genimg(improved_prompt: str):  # improved_prompt передается как аргумент
    # ... ваш код для генерации изображения, используйте improved_prompt

    # Ну че тут переменные кандинского
    kandinsky_url = Config.KANDINSKY_URL 
    kandinsky_api_key = Config.KANDINSKY_API_KEY
    kandinsky_secret_key = Config.KANDINSKY_SECRET_KEY

    kandinsky_api = Text2ImageAPI(kandinsky_url, kandinsky_api_key, kandinsky_secret_key)
    model_id = kandinsky_api.get_model()
    uuid = kandinsky_api.generate(improved_prompt, model_id)
    images = kandinsky_api.check_generation(uuid)
    import os
from flask import Blueprint, request, jsonify, render_template
from utils.text2image import Text2ImageAPI
from dotenv import load_dotenv
from config import Config
from router.improved_prompt import _get_adpromt

# Чтобы норм отображались картинки
from PIL import Image
from io import BytesIO
import base64

load_dotenv()
generate_image = Blueprint("generate_image", __name__)

def _get_genimg(improved_prompt: str):  # improved_prompt передается как аргумент
    # ... ваш код для генерации изображения, используйте improved_prompt

    # Ну че тут переменные кандинского
    kandinsky_url = Config.KANDINSKY_URL 
    kandinsky_api_key = Config.KANDINSKY_API_KEY
    kandinsky_secret_key = Config.KANDINSKY_SECRET_KEY

    kandinsky_api = Text2ImageAPI(kandinsky_url, kandinsky_api_key, kandinsky_secret_key)
    model_id = kandinsky_api.get_model()
    uuid = kandinsky_api.generate(improved_prompt, model_id)
    images = kandinsky_api.check_generation(uuid)
    
     #  Декодируем  base64  изображение  в  байты
    image_bytes = base64.b64decode(images[0])

    #  Создаем  объект  изображения  из  байтов
    image = Image.open(BytesIO(image_bytes)) 

    # Преобразуем картинку в байты
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    image_bytes = buffered.getvalue()

    # Кодируем изображение в base64
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')

    # Возвращаем base64 в виде JSON ответа
    return image_base64