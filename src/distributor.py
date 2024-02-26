from os import getenv
import aiogram

from player import Player
import db


PROJECT_DIR = getenv("PROJECT_DIR")


def create_buttons_from_str(buttons: list[list[str]]) -> list[list[aiogram.types.InlineKeyboardButton]]:
    res = []
    for i in buttons:
        tmp = []
        for j in i:
            tmp.append(aiogram.types.InlineKeyboardButton(text=j, callback_data=j))
        res.append(tmp)
    return res


def process_action(message: aiogram.types.Message | aiogram.types.CallbackQuery) -> tuple[
    str,
    aiogram.types.InlineKeyboardMarkup,
    aiogram.types.InputFile
]:
    data = db.get_data(
        message.from_user.id,
        message.from_user.first_name,
        message.from_user.last_name,
        message.from_user.full_name,
        message.from_user.username
    )
    player = Player(data)
    answer, image, buttons = player.process_request(
        message.text if type(message) is aiogram.types.Message else message.data
    )
    return (
        answer,
        aiogram.types.InlineKeyboardMarkup(inline_keyboard=create_buttons_from_str(buttons)),
        aiogram.types.FSInputFile(path=image)
    )
