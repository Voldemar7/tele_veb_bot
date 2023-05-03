from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ua import LEXICON

router: Router = Router()


# Хендлер для сповіщень, які не попали в інші хендлери
@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON['other_answer'])