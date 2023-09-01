
# Homework 2.12.6.1

class Property:
    def __init__(self,worth):
        self.worth=worth

    def tax(self):
        pass

class Apartment(Property):
    def __init__(self,worth):
        super().__init__(worth)
    def tax(self):
        return self.worth/1000

class Car(Property):
    def __init__(self,worth):
        super().__init__(worth)
    def tax(self):
        return self.worth/200


class CountryHouse(Property):
    def __init__(self,worth):
        super().__init__(worth)
    def tax(self):
        return self.worth/500


print('Counting taxes')
money=int(input('\nEnter amount of money:'))
print('\nEnter property value:')

worth_1=float(input('\nAppartment:'))
appartmant=Apartment(worth_1)
print(f'Tax for Appartment:{appartmant.tax()}')


worth_2=float(input('\nCar:'))
car=Car(worth_2)
print(f'Tax for Car:{car.tax()}')


worth_3=float(input('\n:CountryHouse:'))
country=CountryHouse(worth_3)
print(f'Tax for CountryHouse:{country.tax()}')

sum_tax=country.tax()+car.tax()+appartmant.tax()

if sum_tax>money:
    print(f'Summ of all taxes:{sum_tax}'
          f'\nYou dont have enough money')
else:
    print(f'Summ of all taxes:{sum_tax}'
          f'\nYou  have enough money')
    




# Homework 2.12.6.2

import random

class KillError(Exception):
    """
    An exception describing karmic consequences. Called when a kill is performed..
    """
    pass


class DrunkError(Exception):
    """
    An exception describing karmic consequences. Called when abused
    alcohol.
    """
    pass


class CarCrashError(Exception):
    """
    An exception describing karmic consequences. Called when involved in an accident.
    """
    pass


class GluttonyError(Exception):
    """
    An exception describing karmic consequences. Called when overeating.
    """
    pass


class DepressionError(Exception):
    """
    An exception describing karmic consequences. Triggered by depression.
    """
    pass


errors = (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError)


def one_day() -> int:
    """
    A function that describes one day of life. Returns karma if no mistakes were made.

    :return: karma (from 1 tо 7 units)
    :rtype: int
    :raise KillError: triggered when committing a murder.
    :raise DrunkError: caused by alcohol abuse.
    :raise CarCrashError:triggered when involved in an accident .
    :raise GluttonyError: triggered by overeating.
    :raise DepressionError:triggered by depression .
    """
    print('A new day begins.')
    if random.randint(1, 10) == 1:
        raise random.choice(errors)
    else:
        karma = random.randint(1, 7)
        print(f'Earned {karma} karma points.')
        return karma


total_karma = 0
while total_karma < 500:
    try:
        total_karma += one_day()
        print(f':Current Karma {total_karma}')
    except Exception as e:
        print(f'An error has occurred {type(e).__name__}! Today there will be no karma.')
    finally:
        print()

print('Enlightenment achieved!')





# Homework 2.12.6.3


class MyDict(dict):
    def __init__(self, *args, **kw):
        super(MyDict, self).__init__(*args, **kw)

    def __get__(self, instance, owner):
        return 0


mydict = MyDict()
mydict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}




# Homework 2.12.6.4

from random import randint, choice
NAMES = ['Aleks', 'Tom', 'Hardy', 'Lena ', 'Cric', 'Аnn', 'Мikel']
SURNAMES = ['Holland', 'Joshua', 'Garry', 'Snape', 'Vinni']

#generate randon name, surname, age from constants arrays above
def generate_person():
    name = choice(NAMES)
    surname = choice(SURNAMES)
    age = randint(20, 50)
    return name, surname, age

class Person:
    def __init__(self,name ,family,age):
        self.__name=name
        self.__family=family
        self.__age=age

    def __str__(self):
        return f'Name:{self.__name}\nFamily:{self.__family}\nAge:{self.__age}'

class Empleyee(Person):
    def calc_salary(self):
        raise Exception('This method must be overriden')

    def __str__(self):
        return super().__str__()+f'\nMy salary:{self.calc_salary()}'



class Manager(Empleyee):
    def calc_salary(self):
        return 13000

class Agent(Empleyee):
    sales:int
    def calc_salary(self):
        return 5000+0.05*self.sales


class Worker(Empleyee):
    hours:int
    def calc_salary(self):
        return 100*self.hours


if __name__ == '__main__':
    employees = list()

    # managers
    for _ in range(3):
        employees.append(Manager(*generate_person()))

    # agents
    for _ in range(3):
        agent = Agent(*generate_person())
        agent.sales = randint(2000, 10000)
        employees.append(agent)

    # workers
    for _ in range(3):
        worker = Worker(*generate_person())
        worker.hours = randint(20, 50)
        employees.append(worker)

    # logging out
    for emp in employees:
        print(emp)




# Homework 2.12.6.5

import math
class Car:

    def __init__(self, x, y, fi):
        self.x = x
        self.y=y
        self.fi=fi

    def move(self, dist):
        self.x = self.x + dist * math.cos(self.fi)

        self.y = self.y + dist * math.sin(self.fi)


class Bus(Car):
    PAY_COEFF = 0.01

    MAX_PASSANGERS = 60

    def __init__(self, x, y, direction):

        super().__init__(x, y, direction)

        self.passengers = 0

        self.money = 0

    def move(self, distance):

        self.money += Bus.PAY_COEFF * self.passengers * distance

        super().move(distance)

    def enter(self, passengers):

        if passengers + self.passengers > Bus.MAX_PASSANGERS:
            print('Bus capacity reached')

            print(f'Could only leave:{Bus.MAX_PASSANGERS - self.passengers}')

            print(f'left:{passengers - (Bus.MAX_PASSANGERS - self.passengers)}')

            passengers = Bus.MAX_PASSANGERS - self.passengers

        return passengers

    def exit(self, passengers):

        if passengers > self.passengers:
            print('Everyone got off the bus.')

            passengers = self.passengers

        return passengers




# Homework 2.12.6.6

from random import randint

from os.path import exists, abspath

from os import remove





class House:

    ref_f = 50  # fridge

    nig_m = 100  # nightstand with money

    food_for_pets = 30  # cat food

    amount_of_dirt = 0  # level of dirt in the house

    count_mony = 0

    count_coat = 0

    count_food = 0



    def add_dirty(self):

        self.amount_of_dirt += 5





class Citiez:

    deg_s = 30

    flag_life = True

    action_in_day = False



    def __init__(self, name, house):

        self.house = house

        self.name = name



    def eat(self):

        koef = randint(10, 30)

        if self.house.ref_f > koef:

            self.house.ref_f -= koef

            self.deg_s += koef

            self.house.count_food += koef

        else:

            self.deg_s += self.house.ref_f

            self.house.count_food += self.house.ref_f

            self.house.ref_f = 0

        return ' to eat\n'





class Human(Citiez):

    happy_s = 100



    def pet_the_cat(self):

        self.happy_s += 5

        self.deg_s -= 10

        return ' petting a cat\n'



    def talking_parrot(self):

        self.happy_s += 5

        self.deg_s -= 10

        return ' talking to a parrot\n'



    def happy_in_dirt(self):

        if self.house.amount_of_dirt >= 90:

            self.happy_s -= 10





class Husband(Human):

    def __init__(self, name, house):

        super(Husband, self).__init__(name=name, house=house)



    def __str__(self):

        return 'Husband\'s happiness: {hh}\nSatiety husband: {dh}\n'.format(

            hh=self.happy_s,

            dh=self.deg_s

        )



    def work(self):

        self.deg_s -= 10

        self.house.nig_m += 150

        self.house.count_mony += 150

        return ' working\n'

        # 0 if satiety < koef_a else satiety - koef_a, money + koef_a if satiety > koef_a else money + satiety



    def play(self):

        koef = randint(1, 20)

        self.happy_s += 20

        return ' playing\n'



    def action(self):

        st_life = ''

        try:

            if self.deg_s < 0:

                st_life += 'Husband starved to death\n'

                self.flag_life = False

            elif self.happy_s < 10:

                st_life += 'Husband died of depression\n'

                self.flag_life = False

            else:

                if self.deg_s < 15 and self.house.ref_f > 0:

                    st_life += 'Husband ' + self.eat()

                elif self.house.nig_m <= 20:

                    st_life += 'Husband ' + self.work()

                elif self.happy_s <= 15:

                    st_life += 'Husband ' + self.play()

                elif self.house.nig_m < 350:

                    st_life += 'Husband ' + self.work()

                elif randint(1, 10) % 2 == 0:

                    st_life += 'Husband ' + self.pet_the_cat()

                elif randint(1, 4) % 2 == 1:

                    st_life += 'Husband ' + self.talking_parrot()

                else:

                    st_life += 'Husband ' + self.work()

                if self.house.amount_of_dirt > 90:

                    self.happy_s -= 10

            with open('log_life.log', 'a', encoding='utf8') as log_life:

                log_life.write(st_life)

        except BaseException as e:

            print(st_life, str(e))





class Wife(Human):

    def __init__(self, name, house):

        super(Wife, self).__init__(name=name, house=house)



    def __str__(self):

        return 'Wife\' happines: {hh}\nSatiety wife: {dh}\n'.format(

            hh=self.happy_s,

            dh=self.deg_s

        )



    def action(self):

        st_life = ''

        try:

            if self.deg_s < 0:

                st_life += 'Wife starved to death\n'

                self.flag_life = False

            elif self.happy_s < 10:

                st_life += 'Wife died of depression'

                self.flag_life = False

            else:

                if self.house.ref_f < 10 and self.deg_s >= 50:

                    st_life += 'Wife ' + self.go_shopping()

                elif self.deg_s < 15 and self.house.ref_f > 0:

                    st_life += 'Wife ' + self.eat()

                elif self.house.ref_f <= 30 or self.house.food_for_pets < 10:

                    st_life += 'Wife ' + self.go_shopping()

                elif self.house.amount_of_dirt >= 90:

                    st_life += 'Wife ' + self.clean_the_house()

                elif self.house.nig_m >= 360 and self.house.amount_of_dirt < 50:

                    st_life += 'Wife ' + self.buy_a_fur_coat()

                elif self.happy_s <= 20:

                    st_life += 'Wife ' + self.pet_the_cat()

                elif self.house.amount_of_dirt > 50:

                    st_life += 'Wife ' + self.clean_the_house()

                elif self.house.ref_f < 60:

                    st_life += 'Wife ' + self.go_shopping()

                elif self.house.amount_of_dirt > 0:

                    st_life += 'Wife ' + self.clean_the_house()

                elif randint(1, 10) % 2 == 0:

                    st_life += 'Wife ' + self.talking_parrot()

                else:

                    st_life += 'Wife ' + self.pet_the_cat()

                if self.house.amount_of_dirt > 90:

                    self.happy_s -= 10

            with open('log_life.log', 'a', encoding='utf8') as log_life:

                log_life.write(st_life)

        except BaseException as e:

            print(st_life, str(e))



    def go_shopping(self):

        self.deg_s -= 10

        self.house.nig_m -= 50

        self.house.ref_f += 50

        if self.house.food_for_pets <= 30:

            self.house.food_for_pets += 30

            self.house.nig_m -= 30

        return ' going to the shop\n'



    def buy_a_fur_coat(self):

        self.deg_s -= 10

        self.house.nig_m -= 350

        self.happy_s += 60

        self.house.count_coat += 1

        return ' buys a fur coat\n'



    def clean_the_house(self, koef=0):

        self.deg_s -= 10

        if koef == 0:

            koef = randint(50, 90)

        self.house.amount_of_dirt = 0 if koef > self.house.amount_of_dirt else self.house.amount_of_dirt - koef

        return ' cleaning\n'





class Cat(Citiez):

    def __str__(self):

        return 'Satiety of a cat: {dh}\n'.format(

            dh=self.deg_s

        )



    def eat(self):

        koef = randint(1, 10)

        if self.house.food_for_pets > koef:

            self.house.food_for_pets -= koef

            self.deg_s += koef * 2

            self.house.count_food += koef

        else:

            self.deg_s += self.house.food_for_pets * 2

            self.house.count_food += self.house.food_for_pets

            self.house.food_for_pets = 0

        return ' to eat\n'



    def sleep(self):

        self.deg_s -= 10

        return 'sleeping\n'



    def tell_wallpaper(self):

        self.deg_s -= 10

        self.house.amount_of_dirt += 5

        return ' tearing wallpaper\n'



    def action(self):

        st_life = ''

        try:

            if self.deg_s < 0:

                st_life += 'The cat died of starvation\n'

                self.flag_life = False

            else:

                if self.deg_s <= 15 and self.house.food_for_pets > 0:

                    st_life += ' cat' + self.eat()

                elif randint(1, 10) % 2 == 0:

                    st_life += 'cat' + self.sleep()

                else:

                    st_life += 'cat ' + self.tell_wallpaper()

            with open('log_life.log', 'a', encoding='utf8') as log_life:

                log_life.write(st_life)

        except BaseException as e:

            print(st_life, str(e))



class Parrot(Citiez):

    happy_s = 100

    def __str__(self):

        return 'Satiety parrot: {dh}\n'.format(

            dh=self.deg_s

        )



    def eat(self):

        koef = randint(1, 10)

        if self.house.food_for_pets > koef:

            self.house.food_for_pets -= koef

            self.deg_s += koef * 2

            self.house.count_food += koef

        else:

            self.deg_s += self.house.food_for_pets * 2

            self.house.count_food += self.house.food_for_pets

            self.house.food_for_pets = 0

        return ' to eat\n'



    def sleep(self):

        self.deg_s -= 10

        return ' slesping\n'



    def fly(self):

        self.deg_s -= 10

        self.happy_s += 30

        self.house.amount_of_dirt += 3

        return ' flying\n'



    def talking(self):

        self.deg_s -= 10

        self.happy_s += 5

        return ' speeking\n'



    def action(self):

        st_life = ''

        try:

            if self.deg_s < 0:

                st_life += 'parrot starved to death\n'

                self.flag_life = False

            elif self.happy_s < 10:

                st_life += 'parrot died of depression\n'

                self.flag_life = False

            else:

                if self.deg_s <= 15 and self.house.food_for_pets > 0:

                    st_life += 'parrot ' + self.eat()

                elif self.happy_s < 15:

                    st_life += 'parrot' + self.fly()

                elif self.happy_s < 50:

                    st_life += 'parrot ' + self.talking()

                else:

                    st_life += 'parrot ' + self.sleep()

            with open('log_life.log', 'a', encoding='utf8') as log_life:

                log_life.write(st_life)

        except BaseException as e:

            print(st_life, str(e))





class Child(Human):

    def __init__(self, name, house):

        super(Child, self).__init__(name=name, house=house)



    def __str__(self):

        return 'Child happiness: {hh}\nChild satiety: {dh}\n'.format(

            hh=self.happy_s,

            dh=self.deg_s

        )



    def eat(self):

        koef = randint(10, 15)

        if self.house.ref_f > koef:

            self.house.ref_f -= koef

            self.deg_s += koef

            self.house.count_food += koef

        else:

            self.deg_s += self.house.ref_f

            self.house.count_food += self.house.ref_f

            self.house.ref_f = 0

        return ' to eat\n'



    def play_cat(self):

        self.happy_s += 10

        self.deg_s -= 5

        return ' playing with a cat.\n'



    def play_parrot(self):

        self.happy_s += 15

        self.deg_s -= 5

        return ' playing with a parrot\n'



    def play_mom(self):

        self.happy_s += 30

        self.deg_s -= 5

        return ' играет с матерью\n'



    def play_pap(self):

        self.happy_s += 30

        self.deg_s -= 5

        return ' playing with his father\n'



    def play(self):

        koef = randint(1, 20)

        self.happy_s += 10

        return ' playing\n'



    def action(self):

        st_life = ''

        try:

            if self.deg_s < 0:

                st_life += 'The child died of starvation\n'

                self.flag_life = False

            elif self.happy_s < 10:

                st_life += 'The Child died of depression\n'

                self.flag_life = False

            else:

                rand_fam = randint(0, len(family) - 2)

                if self.deg_s < 10 and self.house.ref_f > 0:

                    st_life += 'Child' + self.eat()

                elif family[rand_fam].flag_life:

                    if isinstance(family[rand_fam], Wife):

                        st_life += 'Child ' + self.play_mom()

                    elif isinstance(family[rand_fam], Husband):

                        st_life += 'Child ' + self.play_pap()

                    elif isinstance(family[rand_fam], Cat):

                        st_life += 'Child ' + self.play_cat()

                    elif isinstance(family[rand_fam], Wife):

                        st_life += 'Child ' + self.play_parrot()

                elif self.happy_s <= 15:

                    st_life += 'Child ' + self.play()

                elif randint(1, 10) % 2 == 0:

                    st_life += 'Ребенок ' + self.pet_the_cat()

                elif randint(1, 4) % 2 == 1:

                    st_life += 'Child ' + self.talking_parrot()

                else:

                    st_life += 'Child ' + self.play()

                if self.house.amount_of_dirt > 90:

                    self.happy_s -= 10

            with open('log_life.log', 'a', encoding='utf8') as log_life:

                log_life.write(st_life)

        except BaseException as e:

            print(st_life, str(e))







def recording_indicators(num_day):

    with open('log_life.log', 'a', encoding='utf8') as log_life:

        log_life.write('{dn}\n{nh}\n{fr}\n{fc}\n{dl}\n'.format(

            dn='Days ' + str(num_day),

            nh='Money in the family' + str(house.nig_m),

            fr='Food in the fridge' + str(house.ref_f),

            fc='Cat food' + str(house.food_for_pets),

            dl='Dirt level' + str(house.amount_of_dirt)

        ))

        st_life = ''

        for i_fam in family:

            log_life.write(str(i_fam))





if exists(abspath('log_life.log')):

    remove(abspath('log_life.log'))



house = House()

family = [Wife(input('What is the wife\'s name? '), house), Husband(input('What is the husband\'s name? '), house),

          Cat(input('What is the cot\'s name? '), house), Parrot(input('What is the parrot\'s name? '), house),

          Child(input('What is the Child\'s name? '), house)

          ]

for i_fam in family:

    i_fam.house = house



for i_day in range(365):

    recording_indicators(i_day)

    for j_fam in family:

        j_fam.action()

    # for j_fam in range(len(family)):

    #     if not family[j_fam].flag_life:

    #         family.pop(j_fam)

    #         print(j_fam)

    house.add_dirty()

print('Money earned ', house.count_mony)

print('Food eaten ', house.count_food)

print('Purchased fur coats ', house.count_coat)

for i_fam in family:

    if not i_fam.flag_life:

        print(i_fam.name, 'Dead ')





# Homework 2.12.6.7

class Stack:
    def __init__(self):
        self.__st=[]

    def __str__(self):
        return ';'.join(self.__st)


    def push(self,elem):
        self.__st.append(elem)


    def pop(self):
        if len(self.__st)==0:
            return None
        return self.__st.pop()

class TaskManager:
    def __init__(self):
        self.task=dict()

    def __str__(self):
        diplay=[]
        if self.task:
            for i_priority in sorted(self.task.keys()):
                diplay.append(f'{str(i_priority)} {self.task[i_priority]}\n')
        return ''.join(diplay)

    def new_task(self,task,priority):
        if priority not in self.task:
            self.task[priority]=Stack()
        self.task[priority].push(task)

manager=TaskManager()
manager.new_task('do cleaning',4)
manager.new_task('wash dishes',4)
manager.new_task('relax',1)
manager.new_task('to eat',2)
manager.new_task('hand over dz',2)
print(manager)
