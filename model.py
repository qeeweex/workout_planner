class Workout:
    name: str
    workout_type: str
    complexity: str
    runtime: float
    data: int

class Workout_type: 
    name: str

class Visitor:
    name: str
    age: int
    workout: str

class Coach: 
    name: str
    salary: float
    age: int
    specialization: list[Workout]