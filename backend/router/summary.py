# router/summary.py

import os
from flask import Blueprint, jsonify, request
import trafilatura
import re
from html import unescape
import ollama  # Assuming you have the ollama library installed
from dotenv import load_dotenv
from config import Config
load_dotenv()

summary_route = Blueprint("summary", __name__)

model_name = Config.MODEL_NAME  #  This might not be needed anymore, as we use ollama directly

def clean_text(text):
    clean_text = re.sub(r'<[^>]+>', '', text)
    clean_text = unescape(clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    return clean_text


# функция для вызова из других
def _get_summary(url: str) -> str:
    downloaded = trafilatura.fetch_url(url)
    text = trafilatura.extract(downloaded)

    if text:
        cleaned_text = clean_text(text)
        print(cleaned_text)
        try:
            response = cleaned_text
            return response
        except Exception as e:
            return f"Произошла ошибка: {e}"  # Return the error message for debugging
    else:
        return "Не удалось извлечь текст из указанного URL."


        system_prompt = """Ты - искусственный интеллект, специализирующийся на анализе и обобщении текстов. Твоя задача - создать краткое, но информативное резюме следующей статьи. При составлении резюме следуй этим инструкциям:

        1. **Анализ**: Внимательно прочитай статью и выяви основные темы, аргументы и выводы.
        2. **Сжатие**: Сфокусируйся на ключевых моментах, опустив детали, которые не критичны для понимания основной идеи.
        3. **Структура**: Начни с введения, где упомяни тему статьи, затем перейди к основным пунктам, и заверши выводом или заключением.
        4. **Ясность**: Используй простой и понятный язык, избегай жаргона, если он не является ключевым для темы статьи.
        5. **Объективность**: Суммарное изложение должно быть нейтральным, без личных мнений или комментариев.
        6. **Длина**: Суммари должно быть не длиннее 150 слов, но достаточно подробным, чтобы передать суть статьи."""

        # Пока убрал суммаризацию, по сути мы будем запихивать все это в массив с контекстом и потом спрашивать по промту
        """ 
        
        
        -- # Формирование полного запроса к Ollama
        full_prompt = f"{system_prompt}\n\nСтатья для суммаризации:\n{cleaned_text}\n\nПожалуйста, предоставь своё резюме:"

        try:
            response = ollama.generate(model=model_name, prompt=full_prompt)  # Directly using ollama
            return response['response']
        except Exception as e:
            return f"Произошла ошибка при запросе к Ollama: {e}" # Return the error message for debugging
    else:
        return "Не удалось извлечь текст из указанного URL.--"""



@summary_route.route("/summary", methods=["POST"])
def summary():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    summary_result = _get_summary(url)

    return jsonify({"message": summary_result}), 200