from database import WorkoutTable, VisitorTable

class Workout:
    name: str
    workout_type: str
    complexity: str
    runtime: float
    data: int

    def __init__(self, id, workout_type, complexity, runtime, data):
        WorkoutTable.create(id, workout_type, complexity, runtime, data) 

    
    def email_is_Busy(cls, email):
        return WorkoutTable.has_runtime(email)

class Workout_type: 
    name: str

class Visitor:
    id: int
    name: str
    age: int
    workout: str

    def __init__(self, id, name, age, workout):
        VisitorTable.create(id, name, age, workout)
    
    
    def email_is_busy(email) -> bool:
        return VisitorTable.has_email
    
    
class Coach: 
    name: str
    salary: float
    age: int
    specialization: list[Workout]