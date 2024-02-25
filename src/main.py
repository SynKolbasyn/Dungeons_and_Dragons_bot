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
    answer, buttons, image = distributor.process_action(message)
    await message.answer_photo(photo=image, caption=answer, reply_markup=buttons)


@dp.callback_query()
async def main_callback(message: aiogram.types.CallbackQuery) -> None:
    answer, buttons, image = distributor.process_action(message.message)
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
