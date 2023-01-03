import os

from telegram import Update
from telegram.ext import ContextTypes

from actions import generate_word_cloud_action, help_action
from messages import GREETINGS_MESSAGE, WRONG_FILE_MESSAGE, PARSE_ERROR_MESSAGE


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=GREETINGS_MESSAGE
    )
    await help_action(update, context)


async def generate_word_cloud_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.document.file_name.endswith('.json'):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=WRONG_FILE_MESSAGE
        )
        return

    username = update.message.from_user.username + "_" + str(update.message.from_user.id)
    file_count = len(os.listdir(f'./data/{username}')) if os.path.exists(f'./data/{username}') else 0
    generated_file_name = f'./data/{username}/{username}_{update.message.date.date()}_{file_count}.json'
    message = str(update.message.caption) if update.message.caption else str(update.message.text)

    try:
        await generate_word_cloud_action(context,
                                         update,
                                         username,
                                         generated_file_name,
                                         message)
    except Exception as e:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=PARSE_ERROR_MESSAGE
        )
        print(e)


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await help_action(update, context)
