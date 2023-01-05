import os

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

import assets as Assets
import messages as Messages
import utils as Utils
from wc import run_wordcloud_generator


def __setup_folders_action(username):
    if not os.path.exists(f'./data/{username}'):
        os.makedirs(f'./data/{username}')
    if not os.path.exists(f'./output/{username}'):
        os.makedirs(f'./output/{username}')


async def start_action(update, context):
    context.user_data['from_start'] = True
    await set_language_action(update, context)


async def generate_word_cloud_action(context: ContextTypes.DEFAULT_TYPE,
                                     update: Update):
    username = update.message.from_user.username + "_" + str(update.message.from_user.id)
    file_count = len(os.listdir(f'./data/{username}')) if os.path.exists(f'./data/{username}') else 0
    file_name = f'./data/{username}/{username}_{update.message.date.date()}_{file_count}.json'
    stopwords = str(update.message.caption) if update.message.caption else str(update.message.text)

    __setup_folders_action(username)

    if not os.path.exists(f'./data/{username}'):
        os.makedirs(f'./data/{username}')
    new_file = await context.bot.get_file(update.message.document.file_id)
    await Utils.send_message(context, update.effective_chat.id, Messages.GENERATING_CLOUD_MESSAGE)
    await new_file.download_to_drive(custom_path=file_name)

    stopwords = set(stopwords.split(' ')) if len(stopwords) > 0 else set()
    run_wordcloud_generator(file_name, username, stopwords)
    output_wordcloud_name = os.path.basename(file_name).split(".")[0] + "_wordcloud.png"
    output_words_name = os.path.basename(file_name).split(".")[0] + "_words.txt"

    await Utils.send_message(context, update.effective_chat.id, Messages.GENERATED_CLOUD_MESSAGE)
    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                 photo=open(f'./output/{username}/{output_wordcloud_name}', 'rb'),
                                 filename=username + "_wordcloud.png")
    await context.bot.send_document(chat_id=update.effective_chat.id,
                                    document=open(f'./output/{username}/{output_words_name}', 'rb'),
                                    filename=username + "_words.txt")


async def help_action(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await Utils.send_media_group(context, update.effective_chat.id, Assets.HELP_ASSETS, Messages.HELP_MESSAGE)


async def set_language_action(update, context):
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Русский", callback_data='set_language_ru')],
        [InlineKeyboardButton("English", callback_data='set_language_en')],
        [InlineKeyboardButton("Українська", callback_data='set_language_ua')],
    ])

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=Messages.CHOOSE_LANGUAGE_MESSAGE,
                                   reply_markup=markup)


async def set_language_callback_action(update, context):
    query = update.callback_query
    await query.answer()
    language = query.data.split('_')[2]
    context.user_data['language'] = language
    await Utils.send_message(context, update.effective_chat.id, Messages.GREETINGS_MESSAGE)
    if context.user_data.get('from_start', False):
        context.user_data['from_start'] = False
        await help_action(update, context)


async def error_action(update, context):
    await Utils.send_message(context, update.effective_chat.id, Messages.ERROR_MESSAGE)


async def wrong_file_action(update, context):
    await Utils.send_message(context, update.effective_chat.id, Messages.WRONG_FILE_MESSAGE)
