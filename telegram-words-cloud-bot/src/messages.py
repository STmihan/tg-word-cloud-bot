GREETINGS_MESSAGE = \
    """Привет!
Я бот, который создает облако слов из вашего чата в Telegram.
Чтобы начать, пришлите мне файл с сообщениями вашего чата в формате .json."""
WRONG_FILE_MESSAGE = \
    """Пожалуйста, пришлите файл в формате .json"""
PARSE_ERROR_MESSAGE = \
    """Что-то пошло не так. Проверьте, что вы отправили нужный файл и попробуйте еще раз."""
GENERATING_CLOUD_MESSAGE = \
    """Облако слов генерируется. Это может занять некоторое время. Пожалуйста, подождите."""
GENERATED_CLOUD_MESSAGE = \
    """Облако слов сгенерировано. Отправляю вам его в виде изображения."""
HELP_MESSAGE = \
    """Чтобы начать, пришлите мне файл с сообщениями вашего чата в формате .json.
После этого я сгенерирую для вас облако слов из сообщений чата.
Чтобы сгенерировать json файл, вам нужно:
1. Открыть чат в настольном приложении Telegram
2. Нажать на кнопку "..." в правом верхнем углу
3. Выбрать "Экспорт чата"
4. Выбрать Формат: JSON
5. Убрать все галочки
5. Нажать "Экспортировать"
6. Пришлите полученный файл мне

Если вы хотите исключить слова из облака, то отправьте мне их через пробел вместе с файлом."""