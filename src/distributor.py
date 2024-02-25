from os import getenv

import aiogram

from player import Player


PROJECT_DIR = getenv("PROJECT_DIR")


def process_action(message: aiogram.types.Message | aiogram.types.CallbackQuery) -> tuple[str, aiogram.types.InlineKeyboardMarkup, aiogram.types.InputFile]:
    player = Player()
    answer = player.process_request(message.text if type(message) is aiogram.types.Message else message.data)
    return (
        answer,
        aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[aiogram.types.InlineKeyboardButton(text=answer, callback_data=answer)]]),
        aiogram.types.FSInputFile(path=f"{PROJECT_DIR}/game_data/images/fantasy-of-the-middle-ages.png")
    )
