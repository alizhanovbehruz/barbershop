from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="◀️Назад")
        ]
    ],
    resize_keyboard=True
)
async def n_back(f_n):
    res = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=f"{f_n}")
            ],
            [
                KeyboardButton(text="◀️Назад")
            ]
        ],
        resize_keyboard=True
    )
    return res

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