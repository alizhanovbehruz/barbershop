from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="◀️Назад")
        ]
    ],
    resize_keyboard=True
)
contback = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить номер телефона",request_contact=True)
        ],
        [
            KeyboardButton(text="◀️Назад")
        ]
    ],
    resize_keyboard=True
)