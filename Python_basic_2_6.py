# Homework 2.6.6.1


#We will continue to write an application for convenient listening to music, but now the songs are stored as a dictionary, and not as nested lists. Each song consists of a title and duration to the nearest fraction of a minute.
#
#violator_songs = {
#'World in My Eyes': 4.86
#'Sweetest Perfection': 4.43,
#'Personal Jesus': 4.56,
#'Halo': 4.9,
#'Waiting for the Night': 6.07,
#'Enjoy the Silence': 4.20
#'Policy of Truth': 4.76,
#'Blue Dress': 4.29
#'Clean': 5.83
#}
#Write a program that prompts the user for the number of songs from a list and their names, and displays the total playing time on the screen.



violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83}


x=int(input('How many song do you wont:'))
count=0
for _ in range(x):
    song=input('Enter name of song:')
    if song in violator_songs:
       count+= violator_songs[song]

print(f'Total song time:{round(count,2)} minutes')



# Homework 2.6.6.2




countries={  }

x=int(input('Enter amount of countries:'))
for i in range(1,x+1):
    name=input(f"{i} country:").split()
    for city in name[1:]:
        countries[city]=name[0]

for i in range(3):
    city=input('\n{} city:'.format(i+1))
    country=countries.get(city)
    if country:
        print(f'{city} city is located in country {country} .')
    else:
        print(f'About city {city} not any informations.')




# Homework 2.6.6.3

#When working with the API (application programming interface) of the cryptocurrency exchange website, you received the following data in the form of a dictionary:
#
#data = {
#"address": "0x544444444444",
#"ETH": {
#balance: 444
#"totalIn": 444,
#"totalOut": 4
#},
#"count_txs": 2,
#"tokens": [
#{
#"fst_token_info": {
#"address": "0x44444",
#"name": "fdf",
#decimals: 0
#"symbol": "dsfdsf",
#"total_supply": "3228562189",
#"owner": "0x44444",
#"last_updated": 1519022607901,
#"issues_count": 0,
#"holders_count": 137528,
#"price": False
#},
#balance: 5000
#"totalIn": 0,
#"total_out": 0
#},
#{
#"sec_token_info": {
#"address": "0x44444",
#"name": "gg",
#"decimals": "2",
#"symbol": "fff",
#"total_supply": "250000000000",
#"owner": "0x44444",
#"last_updated": 1520452201,
#"issues_count": 0,
#"holders_count": 20707,
#"price": False
#},
#balance: 500
#"totalIn": 0,
#"total_out": 0
#}
#]
#}
#Now we need to process this data.
#
#Write a program that performs the following algorithm of actions:
#
#List the keys and values of a dictionary.
#Add the total_diff key to ETH with the value 100.
#Inside fst_token_info change the value of the name key from fdf to doge.
#Remove total_out from tokens and assign its value to total_out inside ETH.
#Inside sec_token_info change the price key name to total_price.
#After executing the algorithm, it is not necessary to display the result (dictionary).
#
#Tips & Tricks
#If you get a list from a dictionary by key, you can apply list methods to it.
#For example:
#
#dictionary[“list”].append(123)
#
#Python will take an object from the dictionary with the key "list" and apply the append method to it. The same logic works with other data types. For example, if you got a dictionary from a dictionary, then you can apply dictionary methods to it, and if you got a string, string methods.
#
#In order not to get confused, print out the object that you receive at the moment. You can also print the type of an object:
#print(data)
#print(data['key'], type(data['key']))
#print(data['key'][0], type(data['key'][0]))
#and so on.
#
#So you will always understand what object you are working on at the moment.


data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}
listt=[]
for x in data:
    listt.append(x)
print(listt)



data['ETH'].update({'total_diff':1000})
print(data)

for elem in data.get('tokens'):
    if elem.get('fst_token_info'):
        elem['fst_token_info']['name']='doge'
        print(data['tokens'])

for key in data.get('tokens'):
    if key.get('sec_token_info'):
        key['sec_token_info']['price']==['total_price']
        print(data['tokens'])




# Homework 2.6.6.4

#In the store database, all the necessary information on goods is divided into two dictionaries: the first is responsible for product codes, the second is for lists of the number of various goods in the warehouse:
#
#goods = {
#'Lamp': '12345',
#'Table': '23456',
#'Sofa': '34567',
#'Chair': '45678',
#}
#store = {
#'12345': [
#{'quantity': 27, 'price': 42},
#],
#'23456': [
#{'quantity': 22, 'price': 510},
#{'quantity': 32, 'price': 520},
#],
#'34567': [
#{'quantity': 2, 'price': 1200},
#{'quantity': 1, 'price': 1150},
#],
#'45678': [
#{'quantity': 50, 'price': 100},
#{'quantity': 12, 'price': 95},
#{'quantity': 43, 'price': 97},
#],
#}
#Each entry in the second dictionary displays how many goods were purchased and at what price. The price is for one piece.
#
#Write a program that calculates the total cost of items for each item in the warehouse and displays this information on the screen.
#
#The result of the program:
#
#Lamp - 27 pieces, cost 1134 rubles.
#
#Table - 54 pieces, cost 27,860 rubles.
#
#Sofa - 3 pieces, cost 3550 rubles.
#
#Chair - 105 pieces, cost 10,311 rubles.
#
#
#goods = {'Лампа': '12345','Стол': '23456','Диван': '34567','Стул': '45678',}
#
#store = {'12345': [{'quantity': 27, 'price': 42},],
#    '23456': [{'quantity': 22, 'price': 510},{'quantity': 32, 'price': 520},],
#    '34567': [ {'quantity': 2, 'price': 1200},{'quantity': 1, 'price': 1150},],
#    '45678': [{'quantity': 50, 'price': 100},{'quantity': 12, 'price': 95},
#        {'quantity': 43, 'price': 97},],}

for good in goods:
    thing=goods.get(good)
    total=0
    amount=0
    for i_thing in store[thing]:
        total+=i_thing['quantity']*i_thing['price']
        amount+=i_thing['quantity']

    print(f'{good}-{amount} pieces, cost {total} rubls')
    


    # Homework 2.6.6.5


#You have already written a program for linguists that takes text as input and counts how many times each character occurs in a string. Now the task has changed: you don't need to output the maximum frequency, but you need to write a function that will invert the resulting dictionary. That is, the key will be the frequency, and the value will be a list of characters with this frequency.
#
#As a result, you need to implement the following subtasks:
#
#get the text and create an original frequency dictionary from it;
#create a new dictionary and populate it with the data from the original frequency dictionary, using the number of repetitions as keys and the letters as values, adding them to the storage list.
#Example
#
#Enter text: something is written here
#
#Original frequency dictionary:
#
#: 2
#
#- : 1
#
#W : 1
#
#a : 2
#
#d : 1
#
#e : 1
#
#and : 1
#
#n : 2
#
#about : 3
#
#p : 1
#
#s : 2
#
#t : 2
#
#h : 1
#
#b : 1
#
#Inverted Frequency Dictionary:
#
#1 : ['3', 'd', 'e', 'b', 'h', '-', 'n', 'u']
#
#2 : ['s', ' ', 't', 'n', 'a']
#
#3 : ['o']

    
    
def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        if val not in inv:
            inv[val] = [key]
        else:
            inv[val].append(key)
    return inv


text = input('Enter text: ')
hist = histogram(text)

print('Original Frequency Dictionary:')

for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])
inv_hist = invert_dict(hist)
print('\nInverted Frequency Dictionary:')
for i_sym in sorted(inv_hist.keys()):
    print(i_sym, ':', inv_hist[i_sym])





# Homework 2.6.6.6
#
#One library commissioned you to write a program to digitize synonym dictionaries. The input to the program is N pairs of words. Each word is a synonym for its paired word.
#
#Implement code that builds a dictionary of synonyms (all words in the dictionary are different), then prompts the user for a word and displays its synonym. Provide input control: if there is no such word, throw an error and ask for the word again. In this case, the check should not depend on the case of characters.
#
#Example
#
#Enter the number of pairs of words: 3
#
#First couple: Hello - Hello
#
#Second pair: Sad - Sad
#
#Third pair: Fun - Joyful
#
#Enter a word: interesting
#
#There is no such word in the dictionary.
#
#Enter a word: hello
#
#Synonym: hello



n = input("Enter amount of words? ")
obyekt = {}
for i in range(int(n)):
        key = input(f'#{i + 1} \nkey : ')
        value = input('value : ')
        obyekt[f'{key}'] = f'{value}'
while True:
        name = input("Enter key the synonym of the word you need:")
        if (obyekt[name]):
            print(f"Synonym:  {obyekt[name]}")
        else:
            print("This word is not exist")
        request = input("Dou you wont to keep going (yes/no )? ")
        if (request != 'yes'):
            print('bye...!')
            break






# Homework 2.6.6.7


#What should be done
#The database of the PizzaTime online store stores information about who, what and how much ordered from them in a certain period. You need to structure this information and determine how many pizzas each customer bought in total.
#
#N orders are submitted to enter the program. Each order is a string like "Customer - pizza name - number of ordered pizzas". Implement code that lists customers and their orders in alphabetical order. Keep in mind that one person can order the same pizza several times.
#
#Example
#
#Enter number of orders: 6
#
#First order: Ivanov Pepperoni 1
#
#Second order: Petrov De Luxe 2
#
#Third order: Ivanov Myasnaya 3
#
#Fourth order: Ivanov Mexicanskaya 2
#
#Fifth order: Ivanov Pepperoni 2
#
#Sixth order: Petrov Interesting 5
#
#Ivanov:
#
#Mexican: 2
#
#Meat: 3
#
#Pepperoni: 3
#
#Petrov:
#
#De Luxe: 2
#
#Interesting: 5




orders_count = int(input('Enter amount of order: '))
database = dict()
for i_order in range(orders_count):
    customer, pizza_name, count = \
        input('{} order: '.format(i_order + 1)).split()

    if customer not in database:
        database[customer] = {pizza_name: int(count)}
    else:
        if pizza_name in database[customer]:
            database[customer][pizza_name] += int(count)
        else:
            database[customer].update({pizza_name: int(count)})

for i_customer in database.keys():
    print('{}:'.format(i_customer))
    for j_pizza in database[i_customer].keys():
        print('     {}: {}'.format(j_pizza, database[i_customer][j_pizza]))
        







# Homework 2.6.6.8

#The user enters a string. You need to write a program that determines if this string has a permutation that would make it a palindrome. It should then display the appropriate message.
#
#Example 1
#
#Enter string: aab
#
#Can be made a palindrome
#
#Example 2
#
#Enter string: aabc
#
#Can't be a palindrome


def is_poly(string):
    char_dict={}
    for i in string:
        char_dict[i]=char_dict.get(i,0)+1

    count=0
    for k in char_dict.values():
        if k%2!=0:
            count+=1
    return count<=1

while True:

    my_string=input('Enter string:')
    if is_poly(my_string):
      print('Can be made a palindrome')
    else:
      print('Can not be made a palindrome')

