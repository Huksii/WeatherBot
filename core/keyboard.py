from aiogram.types import *

menu = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Казахстан"),
    KeyboardButton("Россия"),
    KeyboardButton("Украина"),
    KeyboardButton("США"),
)

menu_kz = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Алматы"),
    KeyboardButton("Астана"),
    KeyboardButton("Атырау"),
    KeyboardButton("Актобе"),
    KeyboardButton("Павлодар"),
    KeyboardButton("Уральск"),
    KeyboardButton("Костанай"),
    KeyboardButton("Караганда"),
    KeyboardButton("Семей"),
    KeyboardButton("Талдыкорган"),
    KeyboardButton("Тараз"),
    KeyboardButton("Меню"),
)

menu_ru = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Москва"),
    KeyboardButton("Санкт-Петербург"),
    KeyboardButton("Красноярск"),
    KeyboardButton("Краснодар"),
    KeyboardButton("Екатеринбург"),
    KeyboardButton("Сочи"),
    KeyboardButton("Владивосток"),
    KeyboardButton("меню")
)

menu_ua = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Полтава"),
    KeyboardButton("Черкассы"),
    KeyboardButton("Одесса"),
    KeyboardButton("Николаев"),
    KeyboardButton("Херсон"),
    KeyboardButton("Львов"),
    KeyboardButton("Ужгород"),
    KeyboardButton("Черновцы"),
    KeyboardButton("Ровно"),
    KeyboardButton("Житомир"),
    KeyboardButton("Сумы"),
    KeyboardButton("Чернигов"),
    KeyboardButton("Запорожье"),
)

menu_en = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Нью-Йорк"),
    KeyboardButton("Вашингтон"),
    KeyboardButton("Лос-Анджелес"),
    KeyboardButton("Лас-вегас"),
    KeyboardButton("Чикаго"),
    KeyboardButton("меню"),
)