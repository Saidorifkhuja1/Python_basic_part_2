# Homework 2.7.8.1


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}




for key,info in students.items():
    for value in info:
        if value=='age':
          print('ID student--old:',key,',',info[value])


def f(dict):
    lst = []
    string = ''
    for i in dict:
        lst += (dict[i]['interests'])
        string += dict[i]['surname']
    cnt = 0
    for s in string:
        cnt += 1
    return lst, cnt

my_lst = f(students)[0]
l = f(students)[1]
print('Full list of interests of all students:',my_lst)
print(f'The total length of all students\' last names: {l}')

# Homework 2.7.8.2

def crypto(objects):
    return[i_elem for index,i_elem in enumerate(objects) if is_prime(index)==True]

def is_prime(number):
    if number==0 or number==1:
        return False
    d=2
    while number%d!=0:
        d+=1
    return d==number

print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))


# Homework 2.7.8.4

players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

players1=players.items()
players3=list(players1)
print(players3)



# Homework 2.7.8.5

families= {' Сидоровa Hикита': 35,' Сидорова Алина': 34,
                 'Cидоров Павел': 10,'Шишкин Hикита': 29,
                 'Шишкина Елизавета': 27,}

while True:
 name=input('Enter surname:').lower()

 def search(second_name):
    for i_family,age in families.items():
        name_list=i_family.split()
        if second_name[:-1] in name_list[0].lower()\
            and (len(second_name)==len(name_list[0])or len(second_name)-len(name_list[0])==abs(1)):
         print(i_family,age)

 search(name)



 # Homework 2.7.8.7
def tpl_sort(number):
    number=tuple(sorted(number))
    return number


numbers=(6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(numbers))


# Homework 2.7.8.8

contacts = {}

while True:
    x=input(f'If you wont add people enter 1.'
            f'\nIf you search add people enter 2>>>')
    if x=='1':
       name = input("Enter name : ")
       surname = input("Enter first name: ")
       name_n_surname = (name, surname)
       if name_n_surname not in contacts:
        contacts[name_n_surname] = int(input("Enter phone number: "))
       else:
        print("This name is already have!")
       print(contacts)
    elif x=='2':
        search=input('Enter name of people'
                     '\n which you are searching>>>')
        if search in contacts.items():
             print(search)
        else:
            print('This person is not in contacts:')




# Homework 2.7.8.9
amount=int(input('How many records are included in the protocol:'))
player_dict=dict()
winners=[]

for record in range(1,amount+1):
    attemt=input(f'{record}-records:')
    name=attemt.split()[1]
    score=int(attemt.split()[0])
    if not name in player_dict:
        player_dict[name]=score
    elif player_dict[name]<score:
        player_dict[name] = score

winners=sorted(tuple(zip(player_dict.values(),player_dict.keys())),reverse=True)

for place in range(3):
    print(f'{place+1}-place  {winners[place][1]},{winners[place][0]}')



#  Homework 2.7.8.10
def shortest_s_r(string,tpl):
    return min(len(string),len(tpl))


syms_str='abc'
nums_tpl=(10,20,30,40)

pairs=((syms_str[i_elem],nums_tpl[i_elem])
        for i_elem in range(shortest_s_r(syms_str,nums_tpl)))

print(pairs)
for i_elem in pairs:
    print(i_elem)
print(zip(syms_str,nums_tpl))
