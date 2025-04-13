from aiogram import Router
from aiogram.filters import Command
from aiogram.filters.state import StateFilter
from aiogram import F
from aiogram.fsm.state import StatesGroup, State, FSMContext
from aiogram.types import Message


class workout_edit():
    Workout = State() # отметить тренировку как выполненую невыполненую и пропущенную 