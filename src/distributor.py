from os import getenv
import aiogram

from player import Player
import db


PROJECT_DIR = getenv("PROJECT_DIR")


def process_action(message: aiogram.types.Message | aiogram.types.CallbackQuery) -> tuple[str, aiogram.types.InlineKeyboardMarkup, aiogram.types.InputFile]:
    data = db.get_data(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.full_name, message.from_user.username)
    player = Player(data)
    answer = player.process_request(message.text if type(message) is aiogram.types.Message else message.data)
    return (
        answer,
        aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[aiogram.types.InlineKeyboardButton(text="button", callback_data="button")]]),
        aiogram.types.FSInputFile(path=f"{PROJECT_DIR}/game_data/images/logo.png")
    )
