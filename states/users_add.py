from aiogram.dispatcher.filters.state import StatesGroup , State

class user_sels(StatesGroup):
    full_name = State()
    numb_phone = State()
    data = State()
    time = State()