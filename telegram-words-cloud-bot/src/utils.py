from telegram.ext import ContextTypes


async def send_message(context: ContextTypes.DEFAULT_TYPE, chat_id: int, text: dict):
    language = context.user_data.get('language', 'ru')
    await context.bot.send_message(
        chat_id=chat_id,
        text=text[language]
    )


async def send_media_group(context: ContextTypes.DEFAULT_TYPE,
                           chat_id: int,
                           media: dict,
                           text: dict):
    language = context.user_data.get('language', 'ru')
    await context.bot.send_media_group(
        chat_id=chat_id,
        media=media[language],
        caption=text[language]
    )
