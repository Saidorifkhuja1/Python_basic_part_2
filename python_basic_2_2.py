
 #  Homework 2_2_6_1




number = int(input('Enter number:'))
numbers = []
for n in range(1, number + 1, 2):
   numbers.append(n)
print(numbers)


  # Homework 2_2_6_2



#For two days of volleyball competitions, it is necessary to form a tournament grid of eight people. On the first day, they decided to choose every second from the list of participants.
#
#A list of eight names is given: Artemy, Boris, Vlad, Gosha, Dima, Eugene, Zhenya, Zakhar. Write a program that displays the list elements only with even indexes.
#
#Example:
#
#First day: ['Artemy', 'Vlad', 'Dima', 'Zhenya']


names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
names2 = []
names3 = []
names2.append(names[0])
names2.append(names[2])
names2.append(names[4])
names2.append(names[6])
print(f'First day:{names2}')
names3.append(names[1])
names3.append(names[3])
names3.append(names[5])
names3.append(names[7])
print(f'Second day:{names3}')


  # Homework 2_2_6_3
amount = int(input('Enter amount of cells:'))
cells = []
for x in range(amount):
    print('\nEfficiency of', x + 1, 'cell')
    y = int(input('>>>'))
    if x > y:
        print('Invalid value:', y, end='\n')


#Homework 2_2_6_4

#In the database of the electronics store there is a list of video cards of NVIDIA of different generations. Instead of full names, only numbers are stored that indicate the model and generation of the video card. Recently, the company has released a new line of video cards. The oldest generations were dismantled in a couple of days.
#
#Write a program that removes the largest elements from the list of video cards.
#
#Example:
#
#Number of video cards: 5
#
#Video card 1: 3070
#
#Video card 2: 2060
#
#Video card 3: 3090
#
#Video card 4: 3070
#
#Video card 5: 3090
#
#
#
#Old list of video cards: [3070 2060 3090 3070 3090]
#
#New list of video cards: [3070 2060 3070]


amount=int(input('Enter amount of cards:'))
oldCards=[]
for x in range(amount):
    cards=int(input('Enter card:'))
    oldCards.append(cards)
print(f'Old list of cards:{oldCards}')
oldCards.remove(max(oldCards))
print(f'New list of cards:{oldCards}')




#Homework 2_2_6_5

#What should be done
#Ilya went to an amateur movie site on which users leave reviews of films. Their list:
#
#FILMS = [‘Strong nut’, ‘back to the future’, ‘taxi driver’, ‘Leon’, ‘Bohemian Ropsody’, ‘City of Sins’, ‘Memento’, ‘Speaker’, ‘Village’]
#
#Ilya on the site for the first time. He wants to register and immediately add some of the films to the list of loved ones in order to read the reviews on them later.
#
#Write the program in which the user introduces the film. If the film is in the list, then it is added to the list of loved ones. If it is not, then an error is displayed. At the end, bring the entire list of your favorite films.
#
#Example:
#
#How many films do you want to add? 3
#
#Enter the name of the film: Leon
#
#Enter the name of the film: Mad Max
#
#Error: we don't have a crazy max film :(
#
#Enter the name of the film: Memento
#
#Your list of favorite films: Leon, Memento


movies=['Крепкий орешек','Назад в будущее','Таксист','Леон','Богемская рапсодия','Город грехов','Мементо','Отступники','Деревня']
lovelyFilms=[]
x=int(input('How many films do you wot to add:'))
for i in range(x):
    film=input('Enter name of movie:')
    if film not in movies:
        print('Sorry we dont have movie:',film)
    else:
        lovelyFilms.append(film)
print(f'List of your favorite movies:{lovelyFilms}')




#Homework 2_2_6_7

#The containers in the warehouse are in the row in the order of non -growing (less or equal) in kilograms. Another container was brought to the warehouse, which also needs to be put in a certain place.
#
#Write a program that receives an irrepressive sequence of natural numbers to the entrance. They mean the mass of each container in a row. After that, the number X is introduced - the mass of the new container. The program displays a number under which a new container will lie. If in the row there are containers with mass, like a new one, then it needs to be put after them.
#
#Provide the input control: all numbers do not exceed 200.
#
#Example:
#
#Number of containers: 8
#
#Enter the weight of the container: 165
#
#Enter the weight of the container: 163
#
#Enter the weight of the container: 160
#
#Enter the weight of the container: 160
#
#Enter the weight of the container: 157
#
#Enter the weight of the container: 157
#
#Enter the weight of the container: 155
#
#Enter the weight of the container: 154
#
#Enter the weight of the new container: 162
#
#The number that will receive a new container: 3

amount=int(input('Eter amount of conteiners:'))
list1=[]
list2=[]
for x in range(amount):
    contr=int(input('Enter weight of conteiner (under 200):'))
    list1.append(contr)
print()
contr1=int(input('Enter weight of new conteiner (under 200):'))
list1.append(contr1)
sorted(list1,reverse=True)

print('the point of new conteiner',list1.index(contr1))



#Homework 2_2_6_8

#You write a program for a small scoreboard, in which the same text or number is cyclically repeated, for example, as in the subway, buses or trams.
#
#A list of n elements and an integer number K. Write a program that cyclically shifts the list elements to the right to K positions. Use the minimum possible number of assignment operations.
#
#Example 1:
#
#Shift: 1
#
#Initial list: [1, 2, 3, 4, 5]
#
#Sloven list: [5, 1, 2, 3, 4]
#
#Example 2:
#
#Shift: 3
#
#Original list: [1, 4, –3, 0, 10]
#
#Sloven list: [–3, 0, 10, 1, 4]

numbers=[1,2,3,4,5]
while True:
 x=int(input('Enter number of circle(from 1 to 5):'))

 if x==1:
    print(numbers)
    print([5,1,2,3,4])
 elif x==2:
    print(numbers)
    print([4,5, 1, 2, 3])
 elif x==3:
    print(numbers)
    print([3,4, 5, 1, 2])
 elif x==4:
    print(numbers)
    print([2,3, 4, 5, 1])
 elif x==5:
    print(numbers)
    print([1,2, 3, 4, 5, ])



#Homework 2_2_6_9

#Continue to write analyzers for the text. Now it is necessary to realize the code by which the palindromes can be determined, that is, the words that are read the same from left to right and right to left.
#
#Write such a program.
#
#Example 1:
#
#Enter the word: Madame
#
#The word is a palindrome
#
#Example 2:
#
#Enter the word: ABCCBA
#
#The word is a palindrome
#
#Example 3:
#
#Enter the word: abbd
#
#The word is not a palinding

s=input('Enter the value:')
reserve=s[::-1]
if s==reserve:
    print('It is palindrome')
else:
    print('It is not palindrome')



#Homework 2_2_6_10

amount=int(input('How many number do you wont to add:'))
numbers=[]
for x in range(amount):
    x=int(input('Enter number:'))
    numbers.append(x)
print(numbers)
print(sorted(numbers))




