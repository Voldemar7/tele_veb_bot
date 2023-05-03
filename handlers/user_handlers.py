import sqlite3

from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message
from services.verification import check_login, corect_password
from lexicon.lexicon_ua import LEXICON
from database.database import user_base, append_database
from aiogram.types import User

router: Router = Router()


# цей хендлер спрацьовує на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'])

    # збираэмо user_id, username, full_name, avatar з користувача
    user: User = message.from_user
    user_base['user_id'] = str(user.id)
    user_base['username'] = user.username
    user_base['full_name'] = user.full_name

# цей хендлер спрацьовує на команду /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['/help'])


# цей хендлер спрацьовує на команду /set_login
@router.message(Command(commands=['register']))
async def process_set_login_command(message: Message):
    await message.answer(text=LEXICON['/register'])


# Отримання і збереження логіна користувача
@router.message(Text(startswith='Логін:'))
async def process_login_message(message: Message):
    login = message.text[6:]
    if check_login(login) == 'check_login':
        await message.answer(text=LEXICON['check_login'])
    else:
        await message.answer(text=LEXICON['not_check_login'])
        user_base['login'] = login
        await message.answer(text=LEXICON['login_next'])


@router.message(Text(startswith='Пароль:'))
async def process_password_message(message: Message):
    password = message.text[7:]
    if corect_password(password) == 'corect_password':
        user_base['password'] = password
        await message.answer(text=LEXICON['corect_password'])
    else:
        await message.answer(text=LEXICON['not_corect_password'])


@router.message(Command(commands=['get_data']))
async def process_get_data_message(message: Message):
    await message.answer(
        text=f'Ваш логін: {user_base["login"]}\nВаш пароль: {user_base["password"]}\nНадішліть команду /save_data, щоб зберегти данні\n\nЩоб поміняти пароль чи логін надішліть /register')


@router.message(Command(commands=['save_data']))
async def process_save_data(messagee: Message):
    append_database()
    await messagee.answer(text=LEXICON['/save_data'])
