# Функция обработки поступившего сообщения

from flask import Blueprint, jsonify, request
from router.summary import _get_summary, clean_text
from router.improved_prompt import _get_adpromt
from router.generate_image import _get_genimg
message_bp = Blueprint('message', __name__) # Создаем Blueprint

@message_bp.route('/message', methods=['POST'])  
def process_message():
    data = request.get_json()
    message = data.get('message')

    if not message:
        return jsonify({'error': 'Сообщение не найдено'}), 400

    # Логика определения ответа (здесь нужно добавить модуль распознования интентов) пусть пока будет вот так
    if message.startswith('http'):
        summary = _get_summary(message) # Используем функцию
        return jsonify({'message': summary})
    else:
        improved_prompt = _get_adpromt(message)  # Передаем message сюда
        image_base64 = _get_genimg(improved_prompt) # А затем сюда
        image_response = f'data:image/png;base64,{image_base64}'
        return jsonify({'message': improved_prompt, 'imageUrl': image_response})