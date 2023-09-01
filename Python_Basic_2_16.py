
# Homework 2.16.6.1

import functools
from typing import Callable
def check_permission(name: str, func: Callable) -> Callable:
    user_permissions = ['admin']

    def check_permission_decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapped(func: Callable) -> Callable:
            result = func()
            return result

        return wrapped

    if name in user_permissions:
        return check_permission_decorator
    else:
        raise PermissionError(f'he user does not have enough rights to execute the function {func.__name__}')


@check_permission('admin')
def delete_site():
    print('Delete site')


@check_permission('user_1')
def add_comment():
    print('Add comment')


delete_site()
add_comment()






# Homework 2.16.6.2

from typing import Callable, Optional
from functools import wraps

app = dict()


def callback(_name_function: Optional[Callable] = None, *, route: str = None) -> Callable:
    def decorator_callback(name_function: Callable) -> Callable:

        app[route] = name_function

        @wraps(name_function)
        def wrapper(*args, **kwargs):
            function_call = name_function(*args, **kwargs)
            return function_call

        return wrapper

    if _name_function is None:
        return decorator_callback
    return decorator_callback(_name_function)


@callback(route='//')
def example() -> str:
    print('An example of a function that returns a server response')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Answer:', response)
else:
    print('This path not exist')

print(app)





# Homework 2.16.6.3

import time
from datetime import datetime


def timer(cls, func, date_format):
    def wrapped(*args, **kwargs):
        format = date_format
        for sym in format:
            if sym.isalpha():
                format = format.replace(sym, '%' + sym)

        print(f"Is running '{cls.__name__}.{func.__name__}'. Start date and tim: {datetime.now().strftime(format)}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Completion '{cls.__name__}.{func.__name__}', work time = {round(end - start, 3)} sec.")
        return result

    return wrapped


def log_methods(date_format):
    def decorate(cls):
        for method in dir(cls):
            if not method.startswith('__'):
                current_method = getattr(cls, method)
                decorated_method = timer(cls, current_method, date_format)
                setattr(cls, method, decorated_method)
        return cls

    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Heir test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()






# Homework 2.16.6.1

import functools

def singleton(cls):
    @functools.wraps(cls)
    def wrapper_singleton(*args,**kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance=cls(*args,**kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance=None
    return wrapper_singleton


@singleton
class Example:
    pass


my_obj=Example()
my_obj1=Example()

print(id(my_obj))
print(id(my_obj1))

print(my_obj is my_obj1)
