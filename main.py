from aiogram import Bot, Dispatcher, executor
from aiogram.types import *

from core.config import TOKEN, ADMIN_ID, API, IMAGE
from core.weather import Forecast
from core.keyboard import menu, menu_kz, menu_ru, menu_en, menu_ua

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=('start'))
async def start(message: Message):
    user_id = message.from_user.id

    if str(user_id) == ADMIN_ID:
        admin_text = """
Добро пожаловать в наш телеграм бот для прогноза погоды.
Мы готовы помочь вашим пользователям всегда быть в 
курсе актуальной погодной информации. 
Не стесняйтесь обращаться, 
если у вас есть какие-либо вопросы или запросы по 
улучшению бота. Вместе мы создадим удивительный 
сервис для наших пользователей!"""
        await message.reply_photo(photo=IMAGE, caption=admin_text, reply_markup=menu)
    else:
        text = "Добро пожаловать в наш телеграм бот для прогноза погоды."
        await message.reply_photo(photo=IMAGE,caption=text, reply_markup=menu)
        
@dp.message_handler(content_types=ContentTypes.TEXT)
async def text(message: Message):
    if message.text.lower() == "казахстан":
        await message.answer("Меню для Казахстана", reply_markup=menu_kz)
                             
    elif message.text.lower()=="сша":
        await message.answer("меню для США", reply_markup=menu_en)
    
    elif message.text.lower() == "россия":
        await message.answer("Вы в меню России", reply_markup=menu_ru)
    
    elif message.text.lower() == "украина":
        await message.answer("Вы в меню Украина", reply_markup=menu_ua)

    elif message.text.lower() == "меню": 
        await message.answer("В меню", reply_markup=menu)

    else:
        rez = Forecast(API, city=message.text)
        await message.reply(rez)

@dp.message_handler(content_types=ContentTypes.PHOTO)
async def photo(message: Message):
    await message.answer(message.photo[len(message.photo)-1].file_id)

if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except (KeyboardInterrupt,  SystemExit):
        pass