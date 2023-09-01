
#Homework 2.11.6.1

import random


class Warrior:
  def __init__(self,health):
    self.health = health

  def hit(self,target,target1):
    while target.health > 0:
      target.health -= 20
      if target1 == warrior1:
        target1 = "Warrior1"
      if target1 == warrior2:
        target1 = "Warrior2"
      print(target1, " has attacked")
      print(target.health, " left")
    if target.health == 0:
      print(target1, " has won")


warrior1 = Warrior(100)
warrior2 = Warrior(100)


q = int(input("Enter 1 to let some warrior attack. Enter 2 to stop program:"))

while q != 2:
  if q == 1:
    j = random.randint(1,3)
    if j % 2 == 0:
      warrior1.hit(warrior2,warrior1)
      q = int(input("Enter 1 to let some warrior attack:"))
    else:
      warrior2.hit(warrior1,warrior2)
      q = int(input("Enter 1 to let some warrior attack:"))
  else:
    print("Wrong input.")
    break


#Homework 2.11.6.2

class Students:
    def __init__(self,name,family,group,score):
        self.name=name
        self.family=family
        self.group=group
        self.score=score
    def info(self):
        print(f'\nName:{self.name}\nFamily:{self.family}\nGroup number:{self.group}\nScore:{self.score}')

student1=Students('Tom','Aleks',12,4)
student1.info()

student2=Students('Bill','Holland',11,5)
student2.info()

student3=Students('Tom','Hanks',10,4)
student3.info()

student4=Students('Toni','Kross',12,5)
student4.info()


student5=Students('Luka','Modrich',10,5)
student5.info()

student6=Students('Ali','Hakim',8,3)
student6.info()

student7=Students('Garry','Potter',7,4)
student7.info()

student8=Students('Frenk','Stark',11,3)
student8.info()

student9=Students('Anna','Kross',12,5)
student9.info()

student10=Students('Isco','Tomson',10,3)
student10.info()



#Homework 2.11.6.3

class Circle:
     pi = 3.14159
     def __init__(self, x=0, y=0, r=1):
            self.x = x
            self.y = y
            self.r = r

     def get_area(self):
            return self.r * self.r * self.pi

     def get_perimeter(self):
            return 2 * self.r * self.pi

     def scale(self, k):
            self.r *= k

     def is_intersect(self, other):
            return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2




#Homework 2.11.6.4


class Parents:
    name='Piter'
    old=45
    number_kids=1
    can='feed baby'
    can2='soothe child'

    def info(self):
        print(f'My name {self.name}\nI am {self.old} years old.\nI have {self.number_kids} child')
    def __add__(self, other):
        if isinstance(other,Child):
            print('\nDo not cry bybe now i feed you ')
        else:
            return None
class Child:
    name='Tommy'
    old=4
    state_calm='crying'
    state_hunger='hungery'

    def info(self):
        print(f'\nName:{self.name}\nOld:{self.old}\nState of calm:{self.state_calm}\nState of hunger:{self.state_hunger}')

parent=Parents()
parent.info()
print('\n This is my son ')
child=Child()
child.info()
print(parent+child)




#Homework 2.11.6.5
class Gardener:

    def __init__(self, name='Вася', garden_bed=None):
        self.name = name
        self.garden_bed = garden_bed

    def take_care_garden_bed(self):
        self.garden_bed.grow_all()

    def about_me(self):
        print(f'Я садовник - {self.name}, я ухаживаю за {self.garden_bed.name}, на ней растет:')
        for potatos in self.garden_bed.potatos:
            print(f'{potatos.name}, номер {potatos.index}, статус {Potato.states[potatos.state]}')
        if len(self.garden_bed.potatos) == 0:
            print('а ничего уже не растет')

    def harvest(self):
        self.garden_bed.potatos.clear()
        print('картошка собрана!')


class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.name = 'картошка'
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(f'Картошка {self.index} сейчас {Potato.states[self.state]}')


class Gardenbed:
    def __init__(self, count):
        self.name = 'грядка'
        self.potatos = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает')
        for i_potato in self.potatos:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatos]):
            print('Картошка еще не созрела!\n')
        else:
            print('Вся картошка созрела, можно собирать!\n')


my_garden = Gardenbed(5)
my_garden.are_all_ripe()
my_gardener = Gardener(name='Боря', garden_bed=my_garden)
my_gardener.take_care_garden_bed()
my_gardener.about_me()
my_gardener.take_care_garden_bed()
my_gardener.harvest()
my_gardener.about_me()




#Homework 2.11.6.6

class Water:
    def __str__(self):
        return 'Water'
    def __add__(self, other):
        if isinstance(other,Air):
            return Storm()
        elif isinstance(other,Fire):
            return Vapor()
        elif isinstance(other,Earth):
            return Dirt()
        else:
            return None



class Air:
    def __str__(self):
        return 'Air'
    def __add__(self, other):
        if isinstance(other,Water):
            return Storm()

class Fire:
    def __str__(self):
        return 'Fire'

class Earth:
    def __str__(self):
        return 'Earth'


class Storm:
    def __str__(self):
        return 'Storm'


class Vapor:
    def __str__(self):
        return 'Vapor'


class Dirt:
    def __str__(self):
        return 'Dirt'

water=Water()
air=Air()
fire=Fire()
earth=Earth()
print(air+water,water+fire,water+earth)


#Homework 2.11.6.7

import random

class Gamer:
    def __init__(self,name,food,satiety,money):
        self.name=name
        self.food=food
        self.satiety=satiety
        self.money=money

gamer=Gamer('Tom',50,50,0)

print('Hi its Tom')

number= int(input("Enter 1 to start game. Enter 2 to stop program:"))

while number!=2:
    if number==1:
       if gamer.money>=50:
        print('\nGo to work.')
        gamer.satiety-=30
        print(f'Satiety={gamer.satiety}')
        gamer.money+=10
        print(f'Money={gamer.money}')
       elif  gamer.satiety<=20:
        print('\nGo to eat')
        gamer.satiety+=20
        print(f'Satiety={gamer.satiety}')
        gamer.food-=30
        print(f'Food={gamer.food}')
       elif gamer.food<=10:
        print('\nGo to shop')
        gamer.money-=10
        print(f'Money={gamer.money}')
        gamer.food+=10
        print(f'Food={gamer.food}')
       elif  gamer.satiety==0:
        print('\nUfortunately Tom is dead ')
        break
    else:
      print("Wrong input.")
      break




#Homework 2.11.6.8

import random
from termcolor import cprint

class Card:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self):
        # *Формирование новой колоды*
        # Карты имеют такие «ценовые» значения:
        # от двойки до десятки — от 2 до 10 соответственно;
        # у туза — 1 или 11 (11 пока общая сумма не больше 21, далее 1);
        # у «картинок» (король, дама, валет) — 10.
        values_simple = ['двойка', 'тройка', 'четвёрка', 'пятёрка', 'шестёрка', 'семёрка', 'восьмёрка', 'девятка',
                         'десятка']
        values_picture = ['валет', 'дама', 'король']
        deck_suits = ['черви', 'пики', 'трефы', 'бубны']

        self.cards = ([Card(values_simple[k - 2], deck_suits[i], k) for k in range(2, 11) for i in range(0, 4)] +
                      [Card(values_picture[k], deck_suits[i], 10) for k in range(0, 3) for i in range(0, 4)] +
                      [Card('туз', deck_suits[i], 11) for i in range(0, 4)])
        random.shuffle(self.cards)

    def cards_print(self):
        print('Карты в колоде')
        i = 1
        for card in self.cards:
            output = str(i) + '. ' + str(card.name) + ' ' + str(card.suit) + ' ' + str(card.value)
            i += 1
            print(output)


class Player:
    def __init__(self, name, own_deck):
        self.name = name
        self.sum = 0
        self.deck = own_deck
        self.hand = []
        self.computer_hand = []
        self.computer_sum = 0

        for _ in range(0, 2):
            player_card = self.deck.cards.pop(0)
            self.hand.append(player_card)
            if player_card.name == 'туз':
                if self.sum >= 21:
                    player_card.value = 1
            self.sum += player_card.value

            computer_card = self.deck.cards.pop(0)
            self.computer_hand.append(computer_card)
            if computer_card.name == 'туз':
                if self.sum >= 21:
                    computer_card.value = 1
            self.computer_sum += computer_card.value

    def take_card(self):
        player_card = self.deck.cards.pop(0)
        self.hand.append(player_card)
        if player_card.name == 'туз':
            if self.sum >= 21:
                player_card.value = 1
        self.sum += player_card.value

    def hand_print(self):
        print('Карты у Вас на руках, Очков: {}'.format(self.sum))
        i = 1
        for card in self.hand:
            output = str(i) + '. ' + str(card.name) + ' ' + str(card.suit) + ' ' + str(card.value)
            i += 1
            print(output)

    def computer_hand_print(self):
        print('Карты на руках у компьютера, Очков: {}'.format(self.computer_sum))
        i = 1
        for card in self.computer_hand:
            output = str(i) + '. ' + str(card.name) + ' ' + str(card.suit) + ' ' + str(card.value)
            i += 1
            print(output)

player_name = str(input('Введите Ваше имя: '))
round_count = 0
scores = [0, 0]

while True:
    round_count += 1
    cprint('Игра началась. Раунд номер {}'.format(round_count), color='yellow')
    player = Player(player_name, Deck())

    player.hand_print()

    while True:
        if player.sum == 21:
            break
        elif player.sum > 21:
            break
        elif 'n' in str(input('Еще y/n? ')).lower():
            break
        else:
            player.take_card()
            print('')
            player.hand_print()
        print('')

    player.computer_hand_print()

    if player.sum == 21:
        cprint('{}, Вы выиграли'.format(player.name), color='green')
        scores[0] += 1
    elif player.sum > 21:
        cprint('{}, Вы проиграли'.format(player.name), color='red')
        scores[1] += 1

    elif player.sum == player.computer_sum:
        print('Ничья')
        scores[0] += 1
        scores[1] += 1

    elif player.sum > player.computer_sum:
        cprint('{}, Вы выиграли'.format(player.name), color='green')
        scores[0] += 1

    else:
        cprint('{}, Вы проиграли'.format(player.name), color='red')
        scores[1] += 1

    if 'n' in str(input('Сыграем еще y/n? ')).lower():
        break
    print('')

print('')
cprint('Сыграно {} раундов'.format(round_count), color='yellow')
cprint('Общий счёт: {} : {}'.format(scores[0], scores[1]), color='yellow', end='. ')
if scores[0] > scores[1]:
    cprint('В Вашу пользу.', color='green')
elif scores[1] > scores[0]:
    cprint('В пользу компьютера.', color='red')
else:
    cprint('Ничья.', color='yellow')






#Homework 2.11.6.9


table = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

def print_table(tab):
    for i_str in range(0, 9, 3):
        print('-' * 18)
        print(f'| {tab[i_str + 1]}  |  {tab[i_str + 2]}  |  {tab[i_str + 3]}  |')
    print('-' * 18)


def tic_toc(counter):
    if counter % 2:
        return 'X'
    return 'O'


def play(tab):
    count = 0
    while True:
        print_table(tab)
        count += 1
        tic = tic_toc(count)
        while True:
            temp = input(f'Выберите номер клетки для {tic}: ')
            if not temp.isdigit():
                print('Вы не ввели число. Попробуйте снова.')
            else:
                if not 0 < int(temp) < 10:
                    print('Клетки имеют номера с 1 по 9. Попробуйте снова.')
                elif str(tab[int(temp)]) in 'XO':
                    print('Эта клетка уже занята. Попробуйте снова.')
                else:
                    tab[int(temp)] = tic
                    break
        if count > 8:
            print('Ничья! Игра окончена')
            break
        if is_win(tab):
            print_table(tab)
            break


def is_win(tab):
    win_table = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
    for i_comb in win_table:
        cell_1, cell_2, cell_3 = i_comb
        comb = ''.join([str(tab[cell_1]), str(tab[cell_2]), str(tab[cell_3])])
        if comb == 'XXX':
            print('X - выйграли!')
            return True
        elif comb == 'OOO':
            print('O - выйграли!')
            return True
    return False

play(table)

