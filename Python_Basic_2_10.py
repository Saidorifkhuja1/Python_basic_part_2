
# Homework 2.10.6.1


with open('people.txt', 'r', encoding='utf-8') as peoples:
  result = 0
  count=0
  try:
     for line in peoples:
       count+=1
       clear_line_len = len(line.rstrip())
       result += clear_line_len
       if clear_line_len < 3:
           raise BaseException

  except BaseException:
      print(f'In {count} line symbols less than 3.')

print('Amount of all symbols',result)



# Homework 2.10.6.2


import random
def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


try:
    with open('coordinates.txt', 'r') as file:
     for line in file:
        nums_list = line.split()
        res1 = f(int(nums_list[0]), int(nums_list[1]))
        try:
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            try:
                number = random.randint(0, 100)
                with open('result.txt', 'w') as file_2:
                 my_list = sorted([res1, res2, number])
                 file_2.write(' '.join(my_list))
            except Exception:
                print("Что-то пошло не так")
        except Exception:
            print("Что-то пошло не так со второй функцией")
        finally:
            print(file.closed)
            print(file_2.closed)

except Exception:
    print("Что-то пошло не так с первой функцией")




# Homework 2.10.6.3

def fortuna ():
   if True:
    return Exception
def make_file(number, fail_name) :
   with open (fail_name, 'a+') as out_file:
     out_file.write (number + '\n' )
def lucky_number (out_fail_name, border=777) :
   count = 0
   while count< border:
     user_number = input ('Enter number: ')
     try:
         fortuna
         make_file(user_number, out_fail_name)
         count+=int(user_number)
     except Exception:
        print ('You have failed!')


   if count >= border:
     print('You have successfully fulfilled the condition to exit the vicious cycle! ')


# Homework 2.10.6.4

def chek_fun(data):
    user_data=data.split()
    try:
        for i in user_data:
            if len(user_data)<3:
                raise IndexError('all three poliyas are not present')
            for i_elem in user_data[0]:
                if not i_elem.isalpha():
                    raise NameError('Nmaes not only letters')
            if '@' not in user_data[1]  and '.' not in user_data[1]:
                raise SyntaxError('In e-mail not (@) and (.)')
            if int(user_data[2])<10 or int(user_data[2])>99:
                raise ValueError('the line old not from 10 to 99')
    except(IndexError,NameError,SyntaxError,ValueError) as er:
        return print(f'{data}\t{er}')
    else:
        return print(f'{data}\tall good')

with open('registrations.txt','r',encoding='utf-8') as registration:
    for line in registration:
        chek_fun(line[:-1])


import os

TOKENS_QTY = 3
FIELDS_SEPARATOR = ' '
DEFAULT_ENCODING = 'utf-8'


def get_file_path(out_filename):
    return os.path.join(os.path.abspath('.'), out_filename)


def is_operand_correct(field):
    result = False
    for c in field:
        if not ('0' <= c <= '9'):
            break
    else:
        result = True
    return result


def is_operation_correct(field):
    available_actions = ['/', '//', '+', '-', '%', '*']
    result = False
    for act in available_actions:
        if act == field:
            result = True
            break
    return result


def get_result(operation, operand_1, operand_2):
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    res = 0
    if operation == '/':
        res = operand_1 / operand_2
    elif operation == '//':
        res = operand_1 // operand_2
    elif operation == '+':
        res = operand_1 + operand_2
    elif operation == '-':
        res = operand_1 - operand_2
    elif operation == '%':
        res = operand_1 % operand_2
    elif operation == '*':
        res = operand_1 * operand_2

    return res


def is_filds_persist(fields):
    return len(fields) == TOKENS_QTY


def item_checker(line):
    fields = line.split(FIELDS_SEPARATOR)
    if not is_filds_persist(fields):
        raise ValueError(' '.join(['Не присутствуют все', str(ITEM_FIELDS_QTY), 'поля']))
    if not is_operation_correct(fields[1]):
        raise SyntaxError(' '.join(['Содержится не поддерживаемое действие ', fields[1]]))
    for op_index in [0, 2]:
        if not is_operand_correct(fields[op_index]):
            raise ValueError(' '.join(['Операнд', str(op_index), 'некорректен -', str(fields[op_index])]))


def main(calcs_filename):
    calcs_filepath = get_file_path(calcs_filename)
    with open(calcs_filepath, 'r') as calcs_fd:
        for line in calcs_fd:
            try:
                line = line.strip()
                item_checker(line)

                fields = line.split(FIELDS_SEPARATOR)
                res = get_result(fields[1], fields[0], fields[2])

                print(' '.join([line, '=', str(res)]))
            except Exception as ex:
                print(line)
                print(ex)


main('calc.txt')


# Homework 2.10.6.6

name=input('Enter name:')
while True:
    print('For view text chat enter 1. for send messege enter 2.')
    response=input('>>>')
    if response=='1':
        try:
            with open('chat.txt','r') as file:
                messege=file.readlines()
                print(' '.join(messege))
        except FileNotFoundError:
            print('This file is not exist.')
    elif response=='2':
        new_messege=input('Enter messege:')
        with open('chat.txt','a') as file:
            file.write(f'{name}:{new_messege}\n')
    else:
        print('Program run without mistakes')

