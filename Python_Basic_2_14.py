
# Homework 2.14.6.1

from typing import Callable,Any
import functools

def general(func:Callable)->Callable:
    @functools.wraps(func)
    def wrapper(*args,**kwargs)->Any:
        input('How are you:')
        print('Not all nice! Okay, keep your function.')
        res=func(*args,**kwargs)
        return res
    return wrapper


@general
def test():
    print('<Something\'s going on...>')

test()




import time
from typing import Callable, Any
import functools

def waiting(func: Callable) -> Callable:
    @functools.wraps(func)
    def timing(*args,**kwargs) -> Any:
        print('Downloding... Wait!')
        time.sleep(3)
        tim=func(*args,**kwargs)
        return tim
    return timing

@waiting
def test():
    print('Complete!')

test()





# Homework 2.14.6.3
from typing import Callable, Any
import datetime


def logging(func: Callable) -> Any:
    def wrapped(*args, **kvargs):
        try:
            return func(*args, **kvargs)
        except Exception as error:
            error_time = datetime.datetime.now()
            with open('function_errors.log', 'a') as file:
                file.write(f'{error_time.strftime("%Y-%m-%d %H:%M:%S")} {func.__name__} {error}\n')

    return wrapped


@logging
def test1() -> Any:
    print('Trying to divide by zero')
    result = 0 / 0


@logging
def test2() -> Any:
    print('Everything is fine here')


@logging
def test3() -> Any:
    print('Trying to divide a string to number')
    result = '0' / 1


test1()
test2()
test3()





# Homework 2.14.6.4

from collections.abc import Callable
import functools

def counter(func:Callable)->Callable:
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        wrapper.count+=1
        res=func(*args,**kwargs)
        print(f'Function{func.__name__} called {wrapper.count} times:')
        return res

    wrapper.count=0
    return wrapper

@counter
def test():
    print('test')

test()
test()
test()
test()

