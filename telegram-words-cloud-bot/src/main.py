import logging
import os

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

import handlers as Handlers

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def main():
    TOKEN = os.getenv('TOKEN')
    print(TOKEN)
    application = ApplicationBuilder().token(TOKEN).build()

    handlers = [
        CommandHandler('start', Handlers.start),
        CommandHandler('help', Handlers.help_handler),
        MessageHandler(filters.ATTACHMENT, Handlers.generate_word_cloud_handler),
    ]
    application.add_handlers(handlers)

    application.run_polling()


if __name__ == '__main__':
    main()
