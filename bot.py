import contextlib
import asyncio
from aiogram.types import ChatJoinRequest
from aiogram import Bot, Dispatcher, F
import logging

BOT_TOKEN = '6529995376:AAHwDLWztC0J3kWaM9q9_kPGTnxRVqaAPvQ'
CHANNEL_ID = -1001964634300
ADMIN_ID = 6573949973

async def approve_request(chat_join: ChatJoinRequest, bot: Bot):
    msg = (
        f'✅You got access to the bot for the game aviator\r\n\r\n' \
        f'Why is this bot needed?🧐\r\n\r\n' \
        f'- earn money playing the game💸 \r\n' \
        f'- receive signals in any quantity🤝 \r\n' \
        f'- use 3 modes to earn money😍 \r\n\r\n' \
        f'IN ORDER TO PICK UP THE BOT CLICK HERE AND WRITE TO ME\r\n' 
        f'https://amar-inc-dm.vercel.app?gnat=219916737527447 👈' 
    )
    await bot.send_message(chat_id=chat_join.from_user.id, text=msg)
    await chat_join.approve()

async def start():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "%(filename)s.%(funcName)s(%(lineno)d) - %(message)s")

    bot : Bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.chat_join_request.register(approve_request, F.chat.id ==CHANNEL_ID)
    
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as ex:
        logging.error(f'[Exception] - {ex}', exc_info=True)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())
