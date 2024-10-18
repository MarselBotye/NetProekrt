import requests
import base64
import re

branch = "main"
def get_github_repo_as_string(repo_url, branch):
    """Извлекает весь код из репозитория GitHub и возвращает его в виде строки.

    Args:
        repo_url: URL репозитория GitHub (например, "https://github.com/MarselBotye/Okno").
        branch: Ветка репозитория, которую нужно извлечь (по умолчанию "main").

    Returns:
        Строка, содержащая весь код репозитория, или None, если произошла ошибка.
    """

    match = re.match(r"https://github.com/([^/]+)/([^/]+)", repo_url)
    if not match:
        print("Неверный URL репозитория.")
        return None

    owner, repo = match.groups()
    repo_content = ""

    def get_file_content(path):
        nonlocal repo_content
        url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={branch}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            print('Все норм жди')
            data = response.json()
            if isinstance(data, list):  # Это директория
                for item in data:
                    get_file_content(item["path"])
            else:  # Это файл
                if data["type"] == "file":
                    file_content = base64.b64decode(data["content"]).decode("utf-8")
                    repo_content += f"--- {path} ---\n{file_content}\n\n"
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к GitHub API: {e}")
            return None  # или обработать ошибку иначе

    # Начинаем с корневой директории
    get_file_content(".")
    return repo_content


# Пример использования:
repo_url = "https://github.com/2gW94/OGTaudio"  # Или любой другой URL репозитория
repo_string = get_github_repo_as_string(repo_url, branch)

if repo_string:
    print(f"Длина строки с кодом репозитория: {(repo_string)}")
    # Дальше можно работать с repo_string, например, сохранить в файл:
    # with open("repo_content.txt", "w", encoding="utf-8") as f:
    #     f.write(repo_string)
else:
    print("Не удалось получить код репозитория.")