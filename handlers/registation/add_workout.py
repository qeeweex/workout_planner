from aiogram import Router
from aiogram.filters import Command
from aiogram.filters.state import StateFilter
from aiogram import F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from model import Workout   
from database import Database

router = Router()

class Workout_add():
    name_workout = State()
    complexity = State()
    runtime = State()
    data = State()

@router.message(Command('add_workout'))
async def start_add_workout(message: Message, state: FSMContext):
    await state.set_state(Workout_add.name_workout)
    await message.answer("Назовите название тренировки:")

@router.message(StateFilter(Workout_add.name_workout))
async def process_name_workout(message: Message, state: FSMContext):
    await state.update_data(name_workout=message.text)
    await state.set_state(Workout_add.complexity)
    await message.answer("Укажите сложность тренировки (например, легкая, средняя, сложная):")

@router.message(StateFilter(Workout_add.complexity))
async def process_complexity(message: Message, state: FSMContext):
    await state.update_data(complexity=message.text)
    await state.set_state(Workout_add.runtime)
    await message.answer("Укажите продолжительность тренировки в минутах:")

@router.message(StateFilter(Workout_add.runtime))
async def process_runtime(message: Message, state: FSMContext):
    await state.update_data(runtime=message.text)
    await state.set_state(Workout_add.data)
    await message.answer("Укажите дату тренировки (например, 2023-11-01):")



@router.message(Command("workout_add"))
async def workout_add(message: Message, state: FSMContext):
    
    user_data = await state.get_data()
    name_workout = user_data.get('name_workout')
    complexity = user_data.get('complexity')
    runtime = user_data.get('runtime')
    date = message.text  

    
    new_workout = Workout(
        name=name_workout,
        complexity=complexity,
        runtime=runtime,
        date=date
    )

    await Database.add_workout(new_workout)  
    await message.answer("Тренировка успешно добавлена!")