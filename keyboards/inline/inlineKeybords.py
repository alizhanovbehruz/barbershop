from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inlinemenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Courses", callback_data="curs"),
            InlineKeyboardButton(text="Books", callback_data="books"),
            InlineKeyboardButton(text="Admin", url='https://t.me/hyperman0011')
        ],
    ],
)

bar_menu= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Сельский",callback_data="fil1"),
            InlineKeyboardButton(text="Шаурмяна",callback_data="fil2")
        ]
    ]
)