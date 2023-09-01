

# Homework 2.15.8.1

class File:
    """
    Upgraded version of the File context manager - now when you try
    open non-existent file manager automatically creates and
    opens this file in write mode.
    """

    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)  # Add self.mode
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


if __name__ == '__main__':
    with File('example.txt', 'w+') as file:
        file.write('Hello World!!')







# Homework 2.15.8.2

import math
from abc import ABC

class MyMath(ABC):


    @classmethod
    def circle_len(cls, radius: int) -> float:
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: int) -> float:
        return math.pi * radius ** 2

    @classmethod
    def cube_value(cls, edge: int) -> float:
        return edge ** 3

    @classmethod
    def sphere_area(cls, radius: int) -> float:
        return 4 * math.pi * radius ** 2

res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)







# Homework 2.15.8.3

class Date:
    def __init__(self,day:int=0,month:int=0,year:int=0)->None:
        self.day=day
        self.month=month
        self.year=year

    def __str__(self)->str:
        return f'Day:{self.day}  Month:{self.month}  Year:{self.year}'

    @classmethod
    def is_date_valid(cls,date:str)->bool:
        day,month,year=map(int,date.split('-'))
        date_obj=cls(day,month,year)
        return 0<day<=31 and 0<month<=12 and 0<year<=9999

    @classmethod
    def from_string(cls,date:str)->'Date':
        day, month, year = map(int, date.split('-'))
        date_obj = cls(day, month, year)
        return date_obj

date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

