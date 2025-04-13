import mysql.connector
from model import * 

connection = mysql.connector.connect(
    user='seschool_01',
    password='seschool_01',
    host='109.206.169.221',
    database='seschool_01_pks1'
)

class Database: 
    __conection = None
    
    @classmethod
    def open(cls, 
             host='109.206.169.221', 
             user='seschool_01', 
             password='seschool_01', 
             database='seschool_01_pks1'):
        if cls.__conection is None:
            cls.__conection = mysql.connector.connect(
                user=user,
                password=password,
                host=host,
                database=database   
            )
        
    @classmethod
    def query(cls, sql, values):
        cursor = cls.cls.__conection.cursor()
        
        cursor.execute(sql, values)
        result = cls.__conection.cursor().fetchall()
        cls.__conection.commit()
        
        return result
    
    @classmethod
    def close(cls):
        cls.__conection.close()

    

class WorkoutTable:
    def get_by_id():
        pass
    
    @classmethod
    def add(cls, workout: Workout): 
        sql = "INSERT INTO Workout (`name`, `workout_type`, `complexity`, `runtime`, `data`) VALUE(%s, %s, %s, %s, %s)"
        values = [workout.name, workout.workout_type, workout.complexity, workout.data, workout.runtime]
        Database.query(sql, values)

    @classmethod
    def has_runtime(cls, runtime: int):
        sql = "SELECT `runtime` FROM `WorkoutTable` WHERE `runtime` = %s"
        runtime = Database.query(sql, [runtime])
        return runtime == 0 
    
    @classmethod
    def has_data(cls, data: int):
        sql = "SELECT `data` FROM `WorkoutTable` WHERE `data` = %s "
        data = Database.query(sql, [data])
        return data == 0 


class Visitor:
    @staticmethod 
    def email_is_busy(email) -> bool:
        return VisitorTable.has_email
    