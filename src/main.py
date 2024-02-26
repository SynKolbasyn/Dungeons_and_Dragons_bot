from os import getenv
import logging
import asyncio

import aiogram

import distributor


PROJECT_DIR = getenv("PROJECT_DIR")

TOKEN = getenv("BOT_TOKEN")

dp = aiogram.Dispatcher()


@dp.message()
async def main_handler(message: aiogram.types.Message) -> None:
    logging.log(
        logging.INFO,
        f"id -> {message.from_user.id} | "
        f"full_name -> {message.from_user.full_name} | "
        f"username -> {message.from_user.full_name} | "
        f"text -> {message.text}"
    )
    answer, buttons, image = distributor.process_action(message)
    await message.answer_photo(photo=image, caption=answer, reply_markup=buttons)


@dp.callback_query()
async def main_callback(message: aiogram.types.CallbackQuery) -> None:
    logging.log(
        logging.INFO,
        f"id -> {message.from_user.id} | "
        f"full_name -> {message.from_user.full_name} | "
        f"username -> {message.from_user.full_name} | "
        f"text -> {message.data}"
    )
    answer, buttons, image = distributor.process_action(message)
    await message.message.edit_media(
        media=aiogram.types.InputMediaPhoto(media=image, caption=answer),
        reply_markup=buttons
    )


async def main() -> None:
    bot = aiogram.Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(filename=f"{PROJECT_DIR}/logs/logs.log", encoding="utf-8")
        ]
    )
    asyncio.run(main())
