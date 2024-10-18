def split_text(text, max_length=512):
    # Разбиваем текст на части по 512 символов
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]