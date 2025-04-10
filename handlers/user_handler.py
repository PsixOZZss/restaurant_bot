from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery, Contact
from aiogram.filters import CommandStart, CommandObject
from aiogram.fsm.context import FSMContext

from aiogram.types.input_file import FSInputFile


from filters.user_filter import UserFilter
from keyboards.user_keyboard import *
from crud.user_bd import UserDatabase
from states.user_form import UserForm
from utils.send_image import send_img


router = Router()
HOOKAH_COUNT = [str(x) for x in range(3, 51)]
HOUR_COUNT = [str(x) for x in range(3, 51)]
MODERATOR_ID = {
    "Oktyabr": 1218938938,
    "Rassvet": 1218938938,
    "Hamovniki": 1218938938,
    "Sochi": 1218938938,
}
KITCHEN_MENU = [
    "./src/menu/kitchen_0.jpg",
    "./src/menu/kitchen_1.jpg",
    "./src/menu/kitchen_2.jpg",
    "./src/menu/kitchen_3.jpg",
    "./src/menu/kitchen_4.jpg",
    "./src/menu/kitchen_5.jpg",
]
BAR_MENU = [
    "./src/menu/bar_0.jpg",
    "./src/menu/bar_1.jpg",
]
PUFF_MENU = [
    "./src/menu/__puffs--1.jpg",
    "./src/menu/__puffs--2.jpg",
    "./src/menu/__puffs--3.jpg",
    "./src/menu/__puffs--4.jpg",
    "./src/menu/__puffs--5.jpg",
    "./src/menu/__puffs--6.jpg",
    "./src/menu/__puffs--7.jpg",
    "./src/menu/__puffs--8.jpg",
    "./src/menu/__puffs--9.jpg",
    "./src/menu/__puffs--10.jpg",
]


@router.message(CommandStart(), UserFilter())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    UserDatabase().create_user(user_id)

    await send_img(message, ["./src/main_menu/start.png"])
    await message.answer(
        """Здравствуйте. Меня зовут ДымзаводБот .

Я помогу вам забронировать стол и расскажу о нас."""
    )
    await message.answer("Главное меню:", reply_markup=start_keyboard())


@router.message(F.text == "Главное меню", UserFilter())
async def start_menu_m(message: Message):
    await send_img(message, ["./src/main_menu/start.png"])
    await message.answer("Главное меню:", reply_markup=start_keyboard())


@router.callback_query(F.data == "StartMenu", UserFilter())
async def start_menu_cq(callback_query: CallbackQuery):
    await callback_query.answer()

    await send_img(callback_query.message, ["./src/main_menu/start.png"])
    await callback_query.message.answer("Главное меню:", reply_markup=start_keyboard())


@router.callback_query(F.data == "NoneData", UserFilter())
async def none_data(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("Функционал в разработке...")


@router.message(F.contact, UserFilter())
async def get_contact(message: Message):
    contact = message.contact
    user_id = contact.user_id
    UserDatabase().update_user(
        user_id,
        phone_number=contact.phone_number,
        name=contact.first_name,
    )
    await message.answer(f"Вы успешно авторизовались", reply_markup=start_keyboard())


@router.callback_query(F.data == "Reservation", UserFilter())
async def reservation(callback_query: CallbackQuery):
    await callback_query.answer()
    user_id = callback_query.from_user.id
    phone_number = UserDatabase().read_user(user_id).phone_number
    if phone_number:
        await callback_query.message.answer(
            """Забронируйте стол для своего мероприятия

Филиалы:""",
            reply_markup=reservation_keyboard(),
        )
    else:
        await callback_query.message.answer(
            "Для создания бронирования необходимо авторизоваться по номеру телефона",
            reply_markup=auth_keyboard(),
        )


@router.callback_query(F.data == "Menu", UserFilter())
async def menu(callback_query: CallbackQuery):
    await callback_query.answer()
    # await message.answer(f"img")
    await callback_query.message.answer(
        "Исследуйте меню, где каждый вкус — это искусство, а подача — настоящее впечатление",
        reply_markup=menu_keyboard(),
    )


@router.callback_query(F.data == "Bar", UserFilter())
async def bar(callback_query: CallbackQuery):
    await callback_query.answer()
    await send_img(callback_query.message, BAR_MENU)
    await callback_query.message.answer(
        """🍹 Наша барная карта — искусство миксологии в каждом бокале""",
        reply_markup=in_menu_keyboard(),
    )


@router.callback_query(F.data == "Kitchen", UserFilter())
async def kitchen(callback_query: CallbackQuery):
    await callback_query.answer()
    await send_img(callback_query.message, KITCHEN_MENU)
    await callback_query.message.answer(
        """🍴 Наше меню — ваш проводник по миру вкуса""",
        reply_markup=in_menu_keyboard(),
    )


@router.callback_query(F.data == "Puff", UserFilter())
async def wine_list(callback_query: CallbackQuery):
    await callback_query.answer()
    await send_img(callback_query.message, PUFF_MENU)
    await callback_query.message.answer(
        "💨 SPECIAL PUFF'S — дымный аккорд вашей вечеринки",
        reply_markup=in_menu_keyboard(),
    )


@router.callback_query(F.data == "Address", UserFilter())
async def address(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(
        """Наши филиалы в Москве и Сочи:""",
        reply_markup=address_keyboard(),
    )


@router.callback_query(F.data == "Oktyabr", UserFilter())
async def oktyabr(callback_query: CallbackQuery):
    await callback_query.answer()
    await send_img(callback_query.message, ["./src/filials/oktyabr.jpg"])
    await callback_query.message.answer(
        """«Красный Октябрь» — зеленый уголок в самом сердце столицы
«Дымзавод» на «Красном Октябре» — место для тех, кто ценит простор и уют под открытым небом, с зелёной верандой и панорамным видом на Москву реку, где каждый момент наполнен гармонией.

🏠 Общая площадь – 2000м²
🌿 Круглогодичная веранда
📍 Адрес: Болотная набережная, д. 3, стр. 2
📞 Телефон: 8(499)111-59-29

Время работы:
Вс-Чт 12.00 — 03.00
Пт-Сб 12.00 — 05.00""",
        reply_markup=in_address_button(),
    )


@router.callback_query(F.data == "Rassvet", UserFilter())
async def rassvet(callback_query: CallbackQuery):
    await callback_query.answer()
    await send_img(callback_query.message, ["./src/filials/rassvet.jpg"])
    await callback_query.message.answer(
        """«Рассвет» — шикарный отдых и гастроромантика городской жизни
«Дымзавод» на Столярном переулке — яркие локации для уединенных встреч с друзьями и живописных мероприятий.

🏠 Общая площадь – 900м²
🌿 Веранда: открыта с апреля по октябрь
📍 Адрес: Столярный переулок, 3/14
📞 Телефон: 8(499)888-19-99

Время работы:
Вс-Чт 12.00 — 03.00
Пт-Сб 12.00 — 05.00
""",
        reply_markup=in_address_button(),
    )


@router.callback_query(F.data == "Hamovniki", UserFilter())
async def hamovniki(callback_query: CallbackQuery):
    await callback_query.answer()
    await send_img(callback_query.message, ["./src/filials/hamovniki.jpg"])
    await callback_query.message.answer(
        """«Дымзавод» в Хамовниках — новое пространство для ценителей вкуса, уюта и стильного отдыха
Здесь авторская кухня удивляет смелыми сочетаниями, винная карта радует редкими находками, а атмосфера окутывает с первых минут

🌿 Веранда: открыта с апреля по сентябрь
📍 Адрес: Комсомольский проспект, 21/10
📞 Телефон: 8(499)681-74-19
""",
        reply_markup=in_address_button(),
    )


@router.callback_query(F.data == "Sochi", UserFilter())
async def sochi(callback_query: CallbackQuery):
    await callback_query.answer()
    await send_img(callback_query.message, ["./src/filials/sochi.jpg"])
    await callback_query.message.answer(
        """«Дымзавод» Сочи — уют, вдохновение и особая атмосфера
Идеальное место для теплых встреч, стильных мероприятий и романтических ужинов. Здесь восточные мотивы гармонично сочетаются с современной эстетикой, создавая пространство для незабываемых моментов

Общая площадь – 700м²
🌿 Веранда: открыта с апреля по октябрь, 66 м2
📍 Адрес: ул. Просвещения, 25, корп. 4, жилой район Адлер, Сочи.
📞 Телефон: 8(499)116-34-21
""",
        reply_markup=in_address_button(),
    )


@router.callback_query(F.data.endswith("_r"), UserFilter())
async def sochi(callback_query: CallbackQuery, bot: Bot):
    await callback_query.answer()

    location = callback_query.data.split("_")[0]
    moderator_id = MODERATOR_ID[f"{location}"]

    user_id = callback_query.from_user.id
    user = UserDatabase().read_user(user_id)

    await bot.send_message(
        chat_id=moderator_id,
        text=f"""Оставили заявку
Имя: {user.name}
Номер: {user.phone_number}""",
    )
    await callback_query.message.answer(
        "Вы успешно оставили заявку, в ближайшее время свяжемся с Вами для уточнения информации",
    )
    await callback_query.message.answer(
        "Главное меню:",
        reply_markup=start_keyboard(),
    )


# @router.callback_query(F.data == "Loyalty", UserFilter())
# async def loyalty(callback_query: CallbackQuery):
#     await callback_query.answer()
#     user_id = callback_query.from_user.id
#     phone_number = UserDatabase().read_user(user_id).phone_number
#     if phone_number:
#         pass
#     else:
#         await callback_query.message.answer(
#             "Возможно, вы уже участвуете в нашей программе лояльности Premium Bonus? Давайте проверим это. Поделитесь, пожалуйста, своим номером телефона.",
#             reply_markup=loyalty_keyboard(),
#         )

# @router.callback_query(F.data == "CancelReservation", UserFilter())
# async def cancel_reservation(callback_query: CallbackQuery):
#     await callback_query.answer()
#     user_id = callback_query.from_user.id
#     phone_number = UserDatabase().read_user(user_id).phone_number
#     if phone_number:
#         pass
#     else:
#         await callback_query.message.answer(
#             """Для отмены бронирования необходимо войти в личный кабинет программы лояльности Munterra или по телефону +74950013968""",
#             reply_markup=cancel_reservation_keyboard(),
#         )


# @router.callback_query(F.data == "Catering", UserFilter())
# async def catering(callback_query: CallbackQuery):
#     await callback_query.answer()
#     # await message.answer(f"img")
#     await callback_query.message.answer(
#         """Организация премиального кальянного кейтеринга на вашем мероприятии в Москве и Московской области. Авторские позиции и сервис Munterra — в особенный день только для вас и ваших гостей. Составим меню под настроение вашего мероприятия, создадим атмосферу замедления и релакса, организуем чёткий и внимательный сервис.""",
#         reply_markup=catering_keyboard(),
#     )


# @router.callback_query(F.data == "Calculator", UserFilter())
# async def calculator(callback_query: CallbackQuery, state: FSMContext):
#     await callback_query.answer()
#     await state.set_state(UserForm.calculator_hookah)
#     # await message.answer(f"img")
#     await callback_query.message.answer(
#         """Сколько единовременно кальянов вы хотите на своем мероприятии? От 3 шт.""",
#     )


# @router.message(F.text.in_(HOOKAH_COUNT), UserForm.calculator_hookah, UserFilter())
# async def calculator_hookah_t(message: Message, state: FSMContext):
#     await state.set_state(UserForm.calculator_hour)

#     hookah_count = int(message.text)
#     await state.update_data({"hookah_count": hookah_count})

#     await message.answer(
#         "Сколько часов вы планируете отвести под курение? от 3-х часов."
#     )


# @router.message(~F.text.in_(HOOKAH_COUNT), UserForm.calculator_hookah, UserFilter())
# async def calculator_hookah_f(message: Message, state: FSMContext):
#     await message.answer("Введите число от 3 до 50")


# @router.message(F.text.in_(HOUR_COUNT), UserForm.calculator_hour, UserFilter())
# async def calculator_hour_t(message: Message, state: FSMContext):
#     # await state.set_state(UserForm.calculator_hour)

#     data = await state.get_data()
#     hookah_count = int(data["hookah_count"])
#     hour_count = int(message.text)
#     total_count = int(hookah_count * hour_count * 2 / 3)
#     total_price = total_count * 5000
#     await message.answer(
#         f"""Предварительная стоимость вашего кейтеринга получается {total_price} рублей, за {total_count} чаш.
# Расчет произведен с учетом только классических чаш. Для более детального рассчета оставьте свою заявку и наш руководитель кальянной станции свяжется с вами."""
#     )


# @router.message(~F.text.in_(HOUR_COUNT), UserForm.calculator_hour, UserFilter())
# async def calculator_hour_f(message: Message, state: FSMContext):
#     await message.answer("Введите число от 3 до 50")

# @router.message(F.text == "Узнать больше", UserFilter())
# async def info(message: Message):
#     user_id = message.from_user.id
#     phone_number = UserDatabase().read_user(user_id).phone_number

#     # await message.answer(f"img")
#     await message.answer(
#         """Чтобы присоединиться к нашей программе лояльности, вам нужно поделиться номером телефона.
# При регистрации вы получите 1000  баллов в подарок, а также 3% кэшбек с суммы каждого чека!"""
#     )
#     await message.answer(
#         """Процент кэшбека будет повышаться с учетом потраченной суммы. Munterra всегда ждёт вас.
# В личном кабинете приложения Munterra можно ознакомиться с электронными товарами и предложениями, которыми можно воспользоваться в обмен на баллы лояльности."""
#     )
#     if phone_number:
#         pass
#     else:
#         await message.answer(
#             "Возможно, вы уже участвуете в нашей программе лояльности Premium Bonus? Давайте проверим это. Поделитесь, пожалуйста, своим номером телефона.",
#             reply_markup=loyalty_keyboard(),
#         )
