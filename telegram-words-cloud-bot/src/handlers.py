from telegram import Update
from telegram.ext import ContextTypes

import actions as Actions
import utils as Utils
import messages as Messages


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await Actions.start_action(update, context)


async def generate_word_cloud_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.document is None or not update.message.document.file_name.endswith('.json'):
        await Actions.wrong_file_action(update, context)
        return

    try:
        await Actions.generate_word_cloud_action(context, update)
    except Exception as e:
        await Actions.error_action(update, context)
        print(e)


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await Actions.help_action(update, context)


async def set_language_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await Actions.set_language_action(update, context)


def set_language_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return Actions.set_language_callback_action(update, context)


def wrong_file_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return Actions.wrong_file_action(update, context)
