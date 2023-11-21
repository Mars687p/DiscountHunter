import asyncio, re
from threading import Thread
from aiogram import Dispatcher, executor, Bot
from aiogram.utils.exceptions import TerminatedByOtherGetUpdates
from .configuration import get_bot_token, get_name_pc, get_user_id
from .logs import logger


async def escaping_characters(text) -> str:  
    return re.sub(r'(?=[\!\-\|\.\(\)<>=])', r'\\', text)

def start_bot():
    asyncio.set_event_loop(loop)
    try:
        executor.start_polling(dp, skip_updates=True)
    except TerminatedByOtherGetUpdates:
        pass


@logger.catch
def send_msg_err(err=None):
    async def wrap(err):
        text = f'*{name_pc}*\n\nОшибка - *{err}*'
        text = await escaping_characters(text)

        try:
            await bot.send_message(user_id, text)
        except:
            text = await escaping_characters(f'*{name_pc}.*\n\n Неопределенное действие.')
            await bot.send_message(user_id, text)

    loop.create_task(wrap(err))

@logger.catch
def send_msg_info(product, price):
    async def wrap(product, price):
        text = f'*{name_pc}*\n\nНа "{product}" цена = {price}'
        text = await escaping_characters(text)
        try:
            await bot.send_message(user_id, text)
        except:
            text = await escaping_characters(f'*{name_pc}.*\n\n Неопределенное действие.')
            await bot.send_message(user_id, text)

    loop.create_task(wrap(product, price))


name_pc = get_name_pc()
user_id = get_user_id()

bot = Bot(get_bot_token(), parse_mode='MarkdownV2') 
dp = Dispatcher(bot)
loop = asyncio.new_event_loop()


bot_th = Thread(target=start_bot, daemon=True)
bot_th.start()


