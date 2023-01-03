import os

from telegram.ext import ContextTypes
from telegram import Update, InputMediaPhoto

from messages import GENERATING_CLOUD_MESSAGE, GENERATED_CLOUD_MESSAGE, HELP_MESSAGE
from wc import run_wordcloud_generator


def setup_folders_action(username):
    if not os.path.exists(f'./data/{username}'):
        os.makedirs(f'./data/{username}')
    if not os.path.exists(f'./output/{username}'):
        os.makedirs(f'./output/{username}')


async def generate_word_cloud_action(context: ContextTypes.DEFAULT_TYPE, update: Update, username, file_name,
                                     stopwords):
    setup_folders_action(username)
    if not os.path.exists(f'./data/{username}'):
        os.makedirs(f'./data/{username}')
    new_file = await context.bot.get_file(update.message.document.file_id)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=GENERATING_CLOUD_MESSAGE)
    await new_file.download_to_drive(custom_path=file_name)

    stopwords = set(stopwords.split(' ')) if len(stopwords) > 0 else set()
    run_wordcloud_generator(file_name, username, stopwords)
    output_wordcloud_name = os.path.basename(file_name).split(".")[0] + "_wordcloud.png"
    output_words_name = os.path.basename(file_name).split(".")[0] + "_words.txt"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=GENERATED_CLOUD_MESSAGE)
    await context.bot.send_photo(chat_id=update.effective_chat.id,
                                 photo=open(f'./output/{username}/{output_wordcloud_name}', 'rb'),
                                 filename=username + "_wordcloud.png")
    await context.bot.send_document(chat_id=update.effective_chat.id,
                                    document=open(f'./output/{username}/{output_words_name}', 'rb'),
                                    filename=username + "_words.txt")


async def help_action(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_media_group(
        chat_id=update.effective_chat.id,
        media=[
            InputMediaPhoto(open('./assets/HELP_1.jpg', 'rb')),
            InputMediaPhoto(open('./assets/HELP_2.jpg', 'rb')),
        ],
        caption=HELP_MESSAGE
    )
