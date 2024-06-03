from aiogram.types import InlineKeyboardButton

import text

menu_start = [
    [
        InlineKeyboardButton(
            text=text.to_continue, callback_data='continue'
        ),
    ],
]
menu = [
    [
        InlineKeyboardButton(text=text.tariff, callback_data='tariff'),
    ],
    [
        InlineKeyboardButton(text=text.price, callback_data='price'),
        InlineKeyboardButton(text=text.about, callback_data='about'),
    ],
    [
        InlineKeyboardButton(text=text.reviews, url="https://clck.ru/3AuzzH"),
    ],
    [
        InlineKeyboardButton(text=text.chat, callback_data='chat'),
    ],
]
back = [
    [
        InlineKeyboardButton(text=text.back, callback_data='back'),
    ],
]
menu_tariff = [
    [
        InlineKeyboardButton(text=text.tests, callback_data='tests'),
        InlineKeyboardButton(text=text.practices, callback_data='practices'),
    ],
    [
        InlineKeyboardButton(text=text.diplomas, callback_data='diplomas'),
    ],
    [
        InlineKeyboardButton(text=text.back, callback_data='back'),
    ],
]
