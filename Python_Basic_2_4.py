# Homewor 2_4_7_1

#
#The linguist team liked the quality of your programs, so they decided to order a function for a text analyzer that would create a list of vowels in it and count their number.
#
#Write a program that asks the user for text and generates a list of vowels of this material (the string itself is entered in Russian). Print the list itself and its length to the console.
#
#Example:
#
#Enter text: Take the ring to Mordor!
#
#List of vowels: ['y', 'o', 'o', 'e', 'i', 'o', 'o', 'o', 'o']
#
#List length: 9
#More about this source textSource text required for additional translation information
#Send feedback
#Side panels
#History
#Saved
#Contribute


sentence = input ("enter the sentence:")
string = sentence.lower ()
print (string)
list1=[]
list2 = ["a","e", "i", "o", "u"]
count=0
for char in string:
 if char in list2:
    list1.append(char)
    count+=1
print ("The  vowels in given sentence are:" ,list1)
print ("Amount  vowels in given sentence is:" ,count)



# Homewor 2_4_7_2


#The user enters an integer N. You need to write a program that generates a list of numbers from 0 to N (not including N). For example, if N is 5, then you need to work with the list 0, 1, 2, 3, 4.
#
#There is also an additional condition. When filling out the list, you need to do one of two things with each number:
#
#if the index of the number is even (or 0), then instead of the number you need to take 1;
#if the index of a number is odd, then instead of a number, you need to take the remainder of dividing this number by 5 (number % 5).
#Thus, the following algorithm is needed:
#
#loop through numbers
#
#     if the current index is even
#
#         then 1 is added to the list
#
#     if the current index is odd
#
#         then the list is added (number % 5)
#
#The algorithm must be implemented using a list generator (in one line).
#
#Example:
#
#Enter list length: 10
#
#Result: [1, 1, 1, 3, 1, 0, 1, 2, 1, 4]




N=int(input('Enter lenth of list:'))

listt=[(num%5 if(num%2!=0) else 1) for num in range(N)]

print(listt)


# Homewor 2_4_7_3


#We want to test the work of the spreadsheet for the participants of some competitions. There are two lists, that is, two teams, with 20 participants in each. They store the points of each participant - real numbers with two signs after the point, for example 4.03.
#
#A member of one team competes with a member of another team with the same number. That is, the first competes with the first, the second with the second, and so on.
#
#Write a program that generates two lists of participants (20 items each) from random real numbers (from 5 to 10). To do this, find a suitable function from the random module. Then generate a third list that contains only the winners from each pair.
#
#Example:
#
#First team: [7.86, 6.76, 9.97, 9.08, 5.45, 6.9, 8.65, 5.17, 8.17, 5.06, 7.56, 7.1, 7.18, 8.25, 5.53, 7.95, 8.91, 7.11, 8.29, 9.52]
#
#Second team: [7.13, 5.7, 8.89, 5.36, 5.62, 9.46, 5.82, 8.67, 8.41, 7.0, 5.31, 7.8, 9.93, 7.76, 7.4, 8.26, 7.94, 5.71, 7.89, 7.77]
#
#Tour winners: [7.86, 6.76, 9.97, 9.08, 5.62, 9.46, 8.65, 8.67, 8.41, 7.0, 7.56, 7.8, 9.93, 8.25, 7.4, 8.26, 8.91, 7.11, 8.29, 9.52]
#


from random import uniform
group1=[round(uniform(5,10),2) for _ in range(20)]
group2=[round(uniform(5,10),2) for _ in range(20)]
group3=[group1[party] if group1[party]> group2[party]
        else group2[party]
        for party in range(20)]
print(f'First team {group1}')
print(f'Second team {group2}')
print(f'Winner team {group3}')


# Homewor 2_4_7_4

#Given a string that stores the first seven letters of the English alphabet.
#
#alphabet = 'abcdefg'
#
#Write a program that displays ten results like this:
#
#a copy of the string;
#elements of the string in reverse order;
#every second element of the string (including the very first);
#every second element of the string after the first;
#all elements up to the second;
#all elements from the end to the penultimate;
#all elements in the index range from 3 to 4 (not including 4);
#the last three elements of the string;
#all elements in the index range from 3 to 4;
#the same as in the previous paragraph, but in reverse order.
#Use only the print command and slicing to obtain and display results.
#
#The results of the program:
#
#1: abcdefg
#
#2: gfedcba
#
#3: aceg
#
#4: bdf
#
#5:a
#
#6:g
#
#7:d
#
#8:efg
#
#9:de
#
#10:ed



alphabet = 'abcdefg'

print(alphabet)
print(alphabet[::-1])
print(alphabet[::2])
print(alphabet[1::2])
print(alphabet[:1])
print(alphabet[6:])
print(alphabet[4:])
print(alphabet[3::6])



# Homewor 2_4_7_5


#The input to the program is a string in which the letter h occurs at least twice. Implement code that reverses the character sequence between the first and last occurrence of the letter h in reverse order.
#
#Example 1:
#
#Enter string: hqwehrty
#
#Expanded sequence between first and last h: ewq.
#
#Example 2:
#
#Enter string: hh
#
#Expanded sequence between the first and last h:
#
#Example 3:
#
#Enter string: hhqwerh
#
#Expanded sequence between the first and last h: rewqh.
#
#Tips & Tricks
#The index of the desired element can be searched both manually and using ready-made list methods.
#The index method has a "brother" - the rindex method. Unlike the first method, the second method starts the search from the right side (from the end). You can learn more about it in this article.



text = input('Введите строку: ')
start, end = text.find('h'), text.rfind('h')

text = text[:start] + text[end:start:-1] + text[end:]
print('Результат:', text)



# Homewor 2_4_7_6

#Often in programming, you have to write code based on the result that the customer requires. This time, he needs to get a two-dimensional list:
#
#[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
#
#Write a program that generates such a list and displays it on the screen. Use only list comprehensions.



import random
N=int(input('Enter amount of nubers:'))
listt=[random.randint(0,2) for _ in range(N)]
print(listt)
listt2=[]
for x in listt:
    if x!=0:
        listt2.append(x)

print(listt2)




# Homewor 2_4_7_7

#Given a multidimensional list:
#
#nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17 , 18]]]
#
#Write code that expands all nested lists, leaving only the outer list. Use only list comprehensions to solve.
#
#Answer: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]



number=[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

number1=[digit for each_list in number for digit in each_list ]
print(sorted(number1))



# Homewor 2_4_7_8


def fallen_bars(L_i,R_i):
   for i_num in range(L_i-1,R_i):
      bars_list[i_num] = 0
   return bars_list
n_bars=int(input("Number of sticks:"))
bars_list = [1 for _ in range (n_bars) ]
n_throw = int (input ("Number of throws: "))
for i_num in range (n_throw):
    Left_i =int(input(f"Gpocok(i_num+1). Knocked down sticks from the number:"))
    Right_i =int(input('by number :'))
    fallen_bars(Left_i,Right_i)
    bars_list=[0 if (i_num>=Left_i-1)and (i_num<Right_i ) else 1 for i_num in range(n_bars)]
    bars_list=['|' if bars_list[i_num]==1 else '.' for i_num in range(0,len(bars_list))]
print(''.join(bars_list))




# Homewor 2_4_7_9

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

output=[digit for each_list in nice_list for each_list2 in each_list for digit in each_list2 ]
print(output)




# Homewor 2_4_7_10

#Julius Caesar used his own method of encrypting text. Each letter was replaced by the next alphabetically through K positions around the circle. If we take the Russian alphabet and K equal to 3, then in the word that we want to encrypt, the letter A will become the letter G, B will become D, and so on.
#
#The user enters a message and an offset value. Write a program that will change the phrase using the Caesar cipher.
#
#Example:
#
#Enter a message: This is a python.
#
#Enter offset: 3
#
#Encrypted message: axs tlhsr.


def caesar_cipher (string,user_shift):
    char_list=[(alphabet[(alphabet.index(sym)+user_shift)%33] if sym!=' 'else ' ' ) for sym in string]
    new_str=''
    for i_chart in char_list:
        new_str+=i_chart
    return new_str

alphabet = 'абогдеёжзийклмнопрстухичшиьызюя'
input_str=input("Enter word:")
shift = int (input ("Enter step:"))

output_str=caesar_cipher(input_str, shift)
print( 'Encrypted string:', output_str)








