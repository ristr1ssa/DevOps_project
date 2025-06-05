import bleach
import html


def sanitize_input(user_input):
    """
    Очищает входные данные от потенциально вредных HTML/JS.
    """
    if not isinstance(user_input, str):
        return ""
    return bleach.clean(user_input, tags=[], attributes={}, strip=True)


def escape_output(text):
    """
    Экранирует спецсимволы, чтобы предотвратить XSS при выводе.
    """
    if not isinstance(text, str):
        return ""
    return html.escape(text)
