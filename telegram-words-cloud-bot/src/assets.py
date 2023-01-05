from telegram import InputMediaPhoto

HELP_ASSETS = {
    'ru': [
        InputMediaPhoto(open('./assets/HELP_1_RU.jpg', 'rb')),
        InputMediaPhoto(open('./assets/HELP_2_RU.jpg', 'rb')),
    ],
    'en': [
        InputMediaPhoto(open('./assets/HELP_1_EN.jpg', 'rb')),
        InputMediaPhoto(open('./assets/HELP_2_EN.jpg', 'rb')),
    ],
    'ua': [
        InputMediaPhoto(open('./assets/HELP_1_UA.jpg', 'rb')),
        InputMediaPhoto(open('./assets/HELP_2_UA.jpg', 'rb')),
    ],
}