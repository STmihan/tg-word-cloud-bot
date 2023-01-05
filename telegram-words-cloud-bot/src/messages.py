CHOOSE_LANGUAGE_MESSAGE = \
    """Выберите язык / Choose language / Выберіть мову:"""
GREETINGS_MESSAGE = \
    {
        "ru": """Привет!
Я бот, который создает облако слов из вашего чата в Telegram.
Чтобы начать, пришлите мне файл с сообщениями вашего чата в формате .json.""",
        "en": """Hello!
I'm a bot that creates a word cloud from your Telegram chat.
To start, send me a file with messages from your chat in .json format.""",
        "ua": """Привіт!
Я бот, який створює хмару слів з вашого чату в Telegram.
Щоб почати, надішліть мені файл з повідомленнями вашого чату у форматі .json.""",
    }
WRONG_FILE_MESSAGE = \
    {
        "ru": """Пожалуйста, пришлите файл в формате .json""",
        "en": """Please, send a file in .json format""",
        "ua": """Будь ласка, надішліть файл у форматі .json""",
    }
ERROR_MESSAGE = \
    {
        "ru": """Что-то пошло не так. Проверьте, что вы отправили нужный файл и попробуйте еще раз. Если ошибка 
        повторяется - напишите @STmihan """,
        "en": """Something went wrong. Check that you sent the right file and try again. If the error persists -
    write @STmihan """,
        "ua": """Щось пішло не так. Перевірте, що ви надіслали потрібний файл і спробуйте ще раз. Якщо помилка 
        повторюється - напишіть @STmihan """,
    }
GENERATING_CLOUD_MESSAGE = \
    {
        "ru": """Облако слов генерируется. Это может занять некоторое время. Пожалуйста, подождите.""",
        "en": """The word cloud is being generated. This may take some time. Please wait.""",
        "ua": """Хмара слів генерується. Це може зайняти деякий час. Будь ласка, зачекайте.""",
    }
GENERATED_CLOUD_MESSAGE = \
    {
        "ru": """Облако слов сгенерировано. Отправляю вам его в виде изображения.""",
        "en": """The word cloud has been generated. I'm sending it to you as an image.""",
        "ua": """Хмара слів згенерована. Надсилаю вам її у вигляді зображення.""",
    }
HELP_MESSAGE = \
    {
        "ru": """Чтобы начать, пришлите мне файл с сообщениями вашего чата в формате .json.
После этого я сгенерирую для вас облако слов из сообщений чата.
Чтобы сгенерировать json файл, вам нужно:
1. Открыть чат в настольном приложении Telegram
2. Нажать на кнопку "..." в правом верхнем углу
3. Выбрать "Экспорт чата"
4. Выбрать Формат: JSON
5. Убрать все галочки
5. Нажать "Экспортировать"
6. Пришлите полученный файл мне

Если вы хотите исключить слова из облака, то отправьте мне их через пробел вместе с файлом.""",
        "en": """To get started, send me a file with the messages from your chat in .json format.
After that, I will generate a word cloud for you from the chat messages.
To generate a json file, you need to:
1. Open the chat in the Telegram desktop app
2. Click on the "..." button in the upper right corner
3. Select "Export chat"
4. Select Format: JSON
5. Remove all checks
5. Click "Export"
6. Send me the file you received

If you want to exclude words from the cloud, send them to me separated by spaces with the file.""",
        "ua": """Щоб почати, надішліть мені файл з повідомленнями вашого чату у форматі .json.
Після цього я згенерую для вас хмару слів з повідомлень чату.
Щоб згенерувати json файл, вам потрібно:
1. Відкрити чат у настільному додатку Telegram
2. Натиснути на кнопку "..." в правому верхньому кутку
3. Вибрати "Експорт чату"
4. Вибрати Формат: JSON
5. Зняти всі позначки
5. Натиснути "Експортувати"
6. Надішліть мені отриманий файл

Якщо ви хочете виключити слова з хмари, то надішліть мені їх через пробіл разом з файлом.""",
    }
