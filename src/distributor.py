import os

import aiogram


PROJECT_DIR = os.getenv("PROJECT_DIR")


def process_action(message: aiogram.types.Message) -> tuple[str, aiogram.types.InlineKeyboardMarkup, aiogram.types.InputFile]:
    return (
        "test",
        aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[aiogram.types.InlineKeyboardButton(text="test", callback_data="test")]]),
        aiogram.types.FSInputFile(path=f"{PROJECT_DIR}/game_data/images/fantasy-of-the-middle-ages.png")
    )
