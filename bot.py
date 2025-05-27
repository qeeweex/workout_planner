import asyncio

from aiogram import Bot, Dispatcher
from handlers.registation import add_workout
from database import Database
from aiogram.fsm.state import FSMContext


from config import TOKEN

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
      
    Database.open() 
    dp.include_router(add_workout.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())