from aiogram import Router
from aiogram.filters import Command
from aiogram.filters.state import StateFilter
from aiogram import F
from aiogram.fsm.state import State, FSMContext
from aiogram.types import Message

router = Router()

class Registation:
    name = State()
    age = State()
    weight = State()


@router.message(Command("Start"))
async def start(message: Message):
    ("Привет! Я бот для управления личным бюджетом."
                        '''
            Используйте команду /register для регистрации на тренировку.
            Далее ввидите свое имя , возраст и вес , что бы выбрать подходящую тренировку
    
    ''')                      

@router.message(Command("register"))
async def register(message: Message, state: FSMContext):
    await message.answer("Введите имя")
    await state.set_state(Registation.name)

@router.message(Command("age_input"))
async def age_input(message: Message, state: FSMContext):
    await message.answer("Введите возраст")
    await state.set_state(Registation.age)


@router.message(Command("weight_input"))
async def weight_input(message: Message, state: FSMContext):
    await message.answer("Введите свой вес")
    await state.set_state(Registation.age)

