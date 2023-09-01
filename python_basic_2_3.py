
#  Homework 2.3.5.1

#Your friend, who also began to study Python, the teacher gave the following task: there is one main ('a') and two side lists ('b' and 'c'), mainly elements are [1, 5, 3], and in side - [1, 5, 1, 5] and [1, 3, 1, 5, 3, 3], respectively.
#
#The program adds elements of the side list ‘B’ to the main one, and then counts the number of digits 5. This number is displayed on the screen, and after that the numbers 5 are removed from the main list. Then the program adds to the main list the elements of the ‘C’ list, considers the number of digits 3 and displays this number per screen. At the end, the list itself appears.
#
#Here is the code itself:


#a = [1, 5, 3]
#b = [1, 5, 1, 5]
#c = [1, 3, 1, 5, 3, 3]
#for i in b:
#a.append(i)
#t = 0
#for i in a:
#if i == 5:
#t += 1
#print(t)
#d = []
#for i in a:
#if i != 5:
#d.append(i)
#for i in c:
#d.append(i)
#t = 0
#for i in d:
#if i == 3:
#t += 1
#print(t)
#print(d)

#Using knowledge about lists, as well as programming style, help a friend rewrite the program. Do not use additional lists.
#
#The result of the program:
#
#Number of digits 5 at the first association: 3
#
#Number of digits 3 in the second association: 4
#
#The final list: [1, 3, 1, 1, 1, 3, 1, 5, 3, 3]


a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
t=0
l=0
for i in a:
    if i==5:
        t+=1
for x in c:
    if x==3:
        l+=1
a.extend(c)
print(f'Amount of number 5 in first list:{t}')
print(f'Amount of number 3 in first list:{l}')
print(a)




#  Homework 2.3.5.2


#Context
#You are working in a software development team for a company that is engaged in processing and data analysis. Your team receives data from various sources, you need to combine them into one sorted list for further processing. However, data sources return sorted lists with possible duplicates, and your task is to create a program that will combine these lists into one sorted list without duplicates.
#
#Task
#Write a program that combines two sorted list of integers into one sorted list without duplicates.
#
#Example
#
#list1 = [1, 3, 5, 7, 9]
#list2 = [2, 4, 5, 6, 8, 10]
#merged = merge_sorted_lists(list1, list2)
#print(merged)
#
#Conclusion in the console:
#
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



firstGroup=[]
secondGroup=[]
firstGroup.append(list(range(160,176+1,2)))
secondGroup.append(list(range(162,180+1,3)))
firstGroup.extend(secondGroup)
print(firstGroup)


#  Homework 2.3.5.3


#In the database of the store of all sorts of things, a list of names of details and their costs is stored:
#
#Shop = ['carriage', 1200], ['connecting rod', 1000], ['saddle', 300], ['pedal', 100], ['saddle', 1500], ['frame', 12000] , ['rim', 2000], ['Shatun', 200], ['saddle', 2700]]]
#
#The seller decided that it was inconvenient to manually consider the number and cost of parts, so he decided to ask the programmer to optimize this process.
#
#Write a program that requests a detail from the user, considers their number and total cost.
#
#Example:
#
#Detail Title: Sadol
#
#Number of details: 3
#
#Total cost: 4500

shop =[['karetka',1200],['shatun',234],['karetka',1200],['karetka',1200]]
nom=input('Maxsulot nomini kiriting: ')
def shopF(nom):
    n=0
    sum=0
    for i in shop:
        if i[0]==nom:
            n+=1
            sum+=i[1]
    print(f'maxsulot nomi {nom}')
    print(f'soni {n}')
    print (f'umumiy narxi {sum}')
shopF(nom)






#  Homework 2.3.5.4


#In honor of his birthday, Artyom decided to throw a party in his country house. He did not send the invitations, but simply informed everyone: "If you want, come and call your friends too." During the party, people came and left, not all remained to spend the night. In addition, only six people are placed in the country.
#
#The initial list of guests is given - the names of those who came to the beginning:
#
#guests = [‘Petya’, ‘Vanya’, ‘Sasha’, ‘Lisa’, ‘Katya’]
#
#Write a program that asks the user if a person left and whether a new guest has come, and, based on the answer, adds to the list or delete the right name from it. At the same time, guests can be no more than six. The names are requested until the user enters the message “It's time to sleep”.
#
#Example:
#
#Now at the party there are 5 people: [‘Petya’, ‘Vanya’, ‘Sasha’, ‘Lisa’, ‘Katya’]
#
#Did the guest come or left? Came
#
#Guest's name: Alex
#
#Hi Alex!
#
#
#Now at the party 6 people: [‘Petya’, ‘Vanya’, ‘Sasha’, ‘Lisa’, ‘Katya’, ‘Alex’]
#
#Did the guest come or left? Came
#
#Guest's name: Gosha
#
#Sorry, Gosha, but there are no places.
#
#
#Now at the party 6 people: [‘Petya’, ‘Vanya’, ‘Sasha’, ‘Lisa’, ‘Katya’, ‘Alex’]
#
#Did the guest come or left? gone
#
#Guest's name: Vanya
#
#So far, Vanya!
#
#
#Now there are 5 people at the party: [‘Petya’, ‘Sasha’, ‘Lisa’, ‘Katya’, ‘Alex’]
#
#Did the guest come or left? It's time to sleep
#
#The party was over, everyone went to bed.


guests=['Петя','Ваня','Саша','Лиза','Катя']
x=0
for i in guests:
    x+=1
c = True
while c:

 print(f'\nNow in party {x} people:{guests}')
 z=input('Guest come or gone:')
 y=input('Name guest:')
 if z=='come':
    if x>=6:
        print(f'Sorry {y} we dont have place')
    else:
       guests.append(y)
       print('Hello,',y)
       x+=1
 if z=='gone':
    guests.remove(y)
    print('Bye,',y)
    x-=1
 if z=='time to sleep':
     c=False
print('Party finishid,every one go to bed.')




#  Homework 2.3.5.5


#We write an application for convenient listening to music. Vanya has a list of nine songs of the Depeche Mode group. Information about each track includes the name and duration with an accuracy to a degree of minutes:
#
#violator_songs = [
#
#['World in my eyes', 4,86],
#
#['Sweetest Perfection', 4,43],
#
#['Personal jesus', 4,56],
#
#['Halo', 4,9],
#
#['Waiting for the Night', 6,07],
#
#['Enjoy The Silence', 4,20],
#
#['Policy of Truth', 4,76],
#
#['Blue Dress', 4,29],
#
#['Clean', 5.83]
#
#]
#
#From this list, Vanya wants to choose n songs and add them to a special playlist with other tracks. At the same time, it is important for him how much time in the sum of these n songs will sound.
#
#Write a program that requests the user the number of songs from the list and their name, and displays the total time of their sound on the screen.
#
#Example:
#
#How many songs to choose? 3
#
#Title 1st Song: Halo
#
#Title of the 2nd Song: Enjoy The Silence
#
#Title of the 3rd Song: Clean
#
#The total time of the sound of songs is 14.93 minutes




violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
amount_song = int( input( 'Amount of songs:'))
my_list=[]
summ=0

for i in range( 1,amount_song+1) :
    print( "Name",i,"song:",end='' )
    song = input()
    my_list. append( song)
for j in violator_songs:
  if j[0] in my_list:
    summ += j[1]
    print ( summ)
print( 'Total song time:', summ,"minutes" )


#  Homework 2.3.5.6

#
#The private office gives rollers of various sizes. A person can only wear videos of his size.
#
#The user introduces two sizes: n sizes of skates and k sizes of people. Implement the code that determines how the largest number of a person can simultaneously take videos and go to ride.
#
#Example:
#
#Number of skates: 4
#
#The size of the pair is 1: 41
#
#The size of the pair is 2: 40
#
#The size of the pair 3: 39
#
#The size of the pair 4: 42
#
#
#Number of people: 3
#
#Human foot size 1: 42
#
#Human foot size 2: 41
#
#Human foot size 3: 42
#
#The largest number of people who can take videos: 2



firstList=[]
secondList=[]

for x in range(1,3+1):
    y=int(input(f'Enter {x}-number for first list:'))
    firstList.append(y)

for z in range(1,7+1):
    a = int(input(f'Enter {z}-number for second list:'))
    secondList.append(a)

print(firstList)
print(secondList)
secondList.extend(firstList)
b=list(set(secondList))
print(b)


#  Homework 2.3.5.7





people=[]
rolik=[]
all=[]
a=int(input('Enter amount of roliks:'))
for i in range(1,a+1):
    k=int(input(f'Enter size of {i} pairs:'))
    rolik.append(k)

b=int(input('\nEnter amount of people:'))
for j in range(1,b+1):
    c=int(input(f'Enter size of {j} people:'))
    people.append(c)
for number in people:
    if number in rolik:
        if number not in all:
            all.append(number)
count=0
for l in all:
    count+=1
print(f'Amouny of people who can take roliks: {count}')



#  Homework 2.3.5.8

#
#N a person numbered by numbers from 1 to N, stand in a circle. They begin to play a counting count. Each k-th by the expense of a person leaves the circle, after which the account continues with the following person.
#
#The number of people n and number K are submitted to the input. Write a program that displays a number from 1 to N - this is the number of a person who will remain in the circle last.
#
#Example:
#
#Number of people: 5
#
#What is the number in the count? 7
#
#So, every 7th person is being left
#
#
#The current circle of people: [1, 2, 3, 4, 5]
#
#The beginning of the account with number 1
#
#A man is being trained at number 2
#
#
#The current circle of people: [1, 3, 4, 5]
#
#Start of account with number 3
#
#A person who retires under number 5
#
#
#The current circle of people: [1, 3, 4]
#
#The beginning of the account with number 1
#
#A person who retires under number 1
#
#
#The current circle of people: [3, 4]
#
#Start of account with number 3
#
#A man is being trained at number 3
#
#
#There was a man under number 4



peoples_amt = int (input('Amount of people: '))
count_num = int (input ('What is the number in the counter? '))
print (f'So every  {count_num}-people leaves')
peoples = list (range (1, peoples_amt + 1))
start_index = 1
for _ in range (len (peoples) - 1) :
  print('\ncurrent circle of people:', peoples)
  print ('Start counting from a number', peoples[(start_index - 1) % len (peoples)])
  lost_people_index = (count_num + start_index - 1) % len (peoples)
  print ('The person leaves numbered', peoples[lost_people_index- 1])
  lost_people = peoples[lost_people_index - 1]
  start_index = peoples. index (lost_people) + 1
  peoples .remove (lost_people)
print ('\nThe person left numbered', peoples [0])


#  Homework 2.3.5.9
x=int(input('Enter amount of friends: '))
y=x=int(input('Enter amount of receipts: '))
count=0
for i in range(1,y+1):
    z=int(input("\nFrom:"))
    c=int(input("To:"))
    a=int(input("How much:"))
    count+=a
print(f'Balans of first friend {-1*count}')
print(f'Balans of second friend {count}')



#  Homework 2.3.5.10


def is_palindrome(num_list):
  reverse_list=[]
  for i_num in range(len(num_list)-1,-1,-1):
     reverse_list.append(num_list[i_num])
  if num_list==reverse_list:
     return True
  else:
     return False

nums=[1,2,3,4,5]
new_nums=[]
answer=[]
for i_nums in range(0,len(nums)):
  for j_elem in range(i_nums, len(nums)):
     new_nums.append(nums[j_elem])
  if is_palindrome(new_nums):
    for i_answer in range(0,i_nums):
      answer.append(nums[i_answer])
    answer.reverse()
    break
  new_nums=[]
print ('Исходный список:' , nums)
print('Нужно чисел для палиндрока:',len(answer))
print('Список этих чисел:',answer)




