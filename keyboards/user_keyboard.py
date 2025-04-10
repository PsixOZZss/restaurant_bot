from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from crud.user_bd import UserDatabase


def start_keyboard():
    builder = InlineKeyboardBuilder()
    button_list = [1, 2, 1]

    # builder.button(text="Программа лояльности", callback_data="Loyalty")
    builder.button(text="Забронировать стол", callback_data="Reservation")
    # builder.button(text="Отменить бронь", callback_data="CancelReservation")
    builder.button(text="Меню", callback_data="Menu")
    builder.button(text="Адреса", callback_data="Address")
    # builder.button(text="Интерьер", callback_data="NoneData")
    # builder.button(text="Афиша", callback_data="NoneData")
    builder.button(text="Задать вопрос", callback_data="NoneData")
    # builder.button(text="Кейтеринг", callback_data="Catering")

    builder.adjust(*button_list)
    return builder.as_markup()


def loyalty_keyboard():
    builder = ReplyKeyboardBuilder()
    button_list = [3]

    builder.button(text="Поделиться номером телефона", request_contact=True)
    builder.button(text="Узнать больше")
    builder.button(text="Главное меню")

    builder.adjust(*button_list)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def auth_keyboard():
    builder = ReplyKeyboardBuilder()
    button_list = [2]

    builder.button(text="Поделиться номером телефона", request_contact=True)
    builder.button(text="Главное меню")

    builder.adjust(*button_list)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def reservation_keyboard():
    builder = InlineKeyboardBuilder()
    button_list = [2, 2, 1]

    builder.button(text="«Красный Октябрь»", callback_data="Oktyabr_r")
    builder.button(text="«Рассвет»", callback_data="Rassvet_r")
    builder.button(text="«Дымзавод» в Хамовниках", callback_data="Hamovniki_r")
    builder.button(text="«Дымзавод» Сочи", callback_data="Sochi_r")
    builder.button(text="Назад", callback_data="StartMenu")

    builder.adjust(*button_list)
    return builder.as_markup()


def cancel_reservation_keyboard():
    builder = ReplyKeyboardBuilder()
    button_list = [1, 1]

    builder.button(text="Поделиться номером телефона", request_contact=True)
    builder.button(text="Главное меню")

    builder.adjust(*button_list)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def menu_keyboard():
    builder = InlineKeyboardBuilder()
    button_list = [2, 1, 1]

    builder.button(text="Основное меню", callback_data="Kitchen")
    builder.button(text="Барное меню", callback_data="Bar")
    builder.button(text="SPECIAL PUFF'S", callback_data="Puff")
    builder.button(text="Главная", callback_data="StartMenu")

    builder.adjust(*button_list)
    return builder.as_markup()


def in_menu_keyboard():
    builder = InlineKeyboardBuilder()
    button_list = [1, 1]

    builder.button(text="Забронировать стол", callback_data="Reservation")
    builder.button(text="Меню", callback_data="Menu")

    builder.adjust(*button_list)
    return builder.as_markup()


def address_keyboard():
    builder = InlineKeyboardBuilder()
    button_list = [2, 2, 1]

    builder.button(text="«Красный Октябрь»", callback_data="Oktyabr")
    builder.button(text="«Рассвет»", callback_data="Rassvet")
    builder.button(text="«Дымзавод» в Хамовниках", callback_data="Hamovniki")
    builder.button(text="«Дымзавод» Сочи", callback_data="Sochi")
    builder.button(text="Главная", callback_data="StartMenu")

    builder.adjust(*button_list)
    return builder.as_markup()


def in_address_button():
    builder = InlineKeyboardBuilder()
    button_list = [1]
    builder.button(text="Назад", callback_data="Address")

    builder.adjust(*button_list)
    return builder.as_markup()


def catering_keyboard():
    builder = InlineKeyboardBuilder()
    button_list = [1, 2]

    builder.button(text="Оставить заявку", callback_data="NoneData")
    builder.button(text="Калькулятор", callback_data="Calculator")
    builder.button(text="Главная", callback_data="StartMenu")

    builder.adjust(*button_list)
    return builder.as_markup()
