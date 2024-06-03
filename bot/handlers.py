import os

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    CallbackQuery
)

import kb
import text

bot = Bot(token=str(os.environ.get("BOT_TOKEN")), parse_mode=ParseMode.HTML)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_input_help_handler(message: Message):
    """
    Обработчик для команды /start
    """
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb.menu_start)
    await message.answer(text.start, reply_markup=keyboard)


@dp.callback_query(F.data.startswith("continue"))
async def continue_callback_handler(callback: CallbackQuery):
    """
    Обработчик для нажатия на кнопку "Продолжить"
    """
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb.menu)
    await callback.message.edit_text(text=text.menu, reply_markup=keyboard)
    await callback.answer()


@dp.callback_query(F.data.startswith("price"))
async def price_callback_handler(callback: CallbackQuery):
    """
    Обработчик для нажатия на кнопку "Цены"
    """
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb.back)
    await callback.message.edit_text(
        text=text.menu_price, reply_markup=keyboard
    )
    await callback.answer()


@dp.callback_query(F.data.startswith("back"))
async def back_callback_handler(callback: CallbackQuery):
    """
    Обработчик для нажатия на кнопку "Назад"
    """
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb.menu)
    await callback.message.edit_text(text=text.menu, reply_markup=keyboard)
    await callback.answer()


@dp.callback_query(F.data.startswith("about"))
async def about_callback_handler(callback: CallbackQuery):
    """
    Обработчик для нажатия на кнопку "О нас"
    """
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb.back)
    await callback.message.edit_text(
        text=text.menu_about, reply_markup=keyboard
    )
    await callback.answer()


@dp.callback_query(F.data.startswith("tariff"))
async def tariff_callback_handler(callback: CallbackQuery):
    """
    Обработчик для нажатия на кнопку "Выберите тариф"
    """
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb.menu_tariff)
    await callback.message.edit_text(
        text=text.menu_tariff, reply_markup=keyboard
    )
    await callback.answer()


@dp.callback_query(F.data.startswith(("tests", "practices", "diplomas")))
async def otvet_callback_handler(callback: CallbackQuery):
    """
    Обработчик для нажатия на кнопку "Тесты", "Выполнение практики", "Дипломы"
    """
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb.back)
    await callback.message.edit_text(text=text.otvet, reply_markup=keyboard)
    await callback.answer()
