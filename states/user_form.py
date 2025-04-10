from aiogram.fsm.state import StatesGroup, State


class UserForm(StatesGroup):
    empty = State()
    catering = State()
    calculator_hookah = State()
    calculator_hour = State()
