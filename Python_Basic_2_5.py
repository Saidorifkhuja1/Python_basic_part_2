# Homework 2.5.6.1

#The restaurant ordered you an application that displays a menu to the user in one click. For work, the restaurant has provided you with its own website, where you can find a menu in the form of successive names of dishes.
#
#Write a program that displays a menu on the screen. The input is a string of dish names, separated by the symbol ";", and the output names are listed separated by commas and spaces.
#
#Example:
#
#Available menu: duck fillet; flank steak; banana pie; pilaf.
#
#Now the menu has: duck fillet, flank steak, banana pie, pilaf.


menu= 'утиное филе;фланк-стейк;банановый пирог;плов'
print(f'Menu was:{menu}')
menu=menu.replace(';',',')
print("Menu now",menu)



# Homework 2.5.6.2
#
#The user enters a string containing spaces. Find the longest word in it, output it and its length. If there are several such words, print the first one.
#
#Example 1
#
#Enter a string: I am a string.
#
#Longest word: "string".
#
#The length of this word is 6 characters.
#
#Example 2
#
#Enter the line: a b.
#
#Longest word: "a".
#
#The length of this word is 1 character.
#
#Example 3
#
#Enter a string: b.
#
#Longest word: "b".
#
#The length of this word is 1 character.



def longest_word(text):
    l=0
    w=''
    words=text.split()
    for word in words:
        if (len(word)>l):
            w=word
            l=len(word)
    return (w,l)

text=input('Enter text:')
w,l=longest_word(text)
print(f'Longest word is:{w}')
print(f'lenth longest word :{l}')


# Homework 2.5.6.3


#An IT company has unspoken rules for naming text documents:
#
#The file name cannot begin with one of the special characters: @, #, $, %, ^, &, *, ().
#The file must end with the .txt or .docx extension.
#Write a program that takes the full name of a file as input and checks if it matches these rules.
#
#Example 1
#
#File name: @example.txt.
#
#Error: The name starts with an invalid character.
#
#Example 2
#
#File name: example.ttx.
#
#Error: Invalid file extension. Expected .txt or .docx.
#
#Example 3
#
#File name: example.txt.
#
#The file is named correctly.
#
#Tips & Tricks
#The endswith method (like startswith) can be used to test for multiple endings. Examples of such use.


file=input('Enter name of file:')
print(f'Name of file:{file}')

if file.startswith(('@','№','$','%','^','&','*','()')):
    print("File name must not start with special symbols:")
elif not file.endswith('.txt'or '.docx'):
    print('("File name must  start with {.txt} or {.docx}:")')
else:
    print('File name correct')



# Homework 2.5.6.4

#The user enters a string. Write a program that changes the case of the characters in this string so that the first letter of each word is uppercase and the rest are lowercase.
#
#Example
#
#Enter the line: I think I forgot to turn off the iron.
#
#Result:  I forgot to turn off the iron.

text=input('Enter text:').title()
print(text)



# Homework 2.5.6.5

#
#When registering on the site, in addition to the login, you need to come up with a password. This password must be at least eight characters long, contain at least one capital letter and at least three numbers. Then it will be considered reliable.
#
#Write a program that asks the user to come up with a password until the password is strong. Latin must be used.
#
#Example
#
#Create a password: qwerty.
#
#The password is not secure. Try again.
#
#Create a password: qwerty12.
#
#The password is not secure. Try again.
#
#Create a password: qwerty123.
#
#The password is not secure. Try again.
#
#Create a password: qWErty123.
#
#This is a strong password.


alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    password = input('Enter new password: ')
    upper_count = 0
    num_count = 0
    for i_sym in password:
        if i_sym in alphabet:
            if i_sym.isupper():
                upper_count += 1
        elif '0' < i_sym < '9':
            num_count += 1

    if len(password) < 8 or upper_count < 1 or num_count < 3:
        print('The password is not secure. Try again.')
    else:
        print('The password is secure!')
        break



# Homework 2.5.6.6

#Due to the fact that the volume of data has increased, it was necessary to compress this data, but in such a way as not to lose important information. A special encoding was invented for this: s = 'aaaabbсaa' is converted to 'a4b2с1a2'. That is, groups of identical characters of the source string are replaced by these characters and the number of their repetitions in the string.
#
#Write a program that reads a string, encodes it using the proposed algorithm, and displays the encoded sequence on the screen. The code must be case sensitive.
#
#Example
#
#Enter the string: aaAAbbcaaaA.
#
#Encoded string: a2A2b2c1a3A1.


string=input('Enter text:')
new_string=''
count=1
for i in range(len(string)-1):
    if string[i]==string[i+1]:
        count+=1
    else:
        new_string+=string[i]+str(count)
        count=1
print(new_string)



# Homework 2.5.6.7

#When writing a client-server application, you often need to work with IP addresses. As you already know, an IP address consists of four integers ranging from 0 to 255, separated by dots.
#
#The user enters a string. Write a program that determines if a given string is indeed a valid IP address. Provide input control that provides for the addition of integers from 0 to 255 and dots in between.
#
#Example 1
#
#Enter IP: 128.16.35.a4
#
#a4 is not an integer.
#
#Example 2
#
#Enter IP: 240.127.56.340
#
#340 is greater than 255.
#
#Example 3
#
#Enter IP: 34.56.42.5
#
#An address is four numbers separated by dots.
#
#Example 4
#
#Enter IP: 128.0.0.255
#
#The IP address is correct.



while True:
    check = False
    ip_addr = input('Enter your IP address: ').split('.')
    if len(ip_addr) != 4:
      print('An IP address can only contain four numbers divided by "." symbol')
      continue

    for i in range(len(ip_addr)):
        if not ip_addr[i].isdigit():
            print('An IP address can only contain digits')
            check = True
            break
    if check:
      continue


    for i in range(len(ip_addr)):
      if int(ip_addr[int(i)]) > 255:
          print('The IP address octet can\'t be more than "255"')
          check = True
          break
    if check:
     continue
    print('IP address is correct')
    break
print( 'Done. ')




# Homework 2.5.6.8


#В одной из практических работ вы писали программу для табло, которая циклически сдвигает элементы списка чисел вправо на K позиций. В этот раз вы работаете с двумя строками. Возможно, одна из строк немного сдвинута. Нужно проверить, не равна ли первая строка второй.
#
#Пользователь вводит две строки. Напишите программу, которая определяет, можно ли получить первую строку из второй циклическим сдвигом.
#
#По желанию: если строку получить можно, выведите значение сдвига.
#
#Пример 1
#
#Первая строка: abcd.
#
#Вторая строка: cdab.
#
#Первая строка получается из второй со сдвигом 2.
#
#Пример 2
#
#Первая строка: abcd.
#
#Вторая строка: cdba.
#
#Первую строку нельзя получить из второй с помощью циклического сдвига.





first_string = input('First string: ')
second_string = input('Second string: ')

pos = (first_string + first_string).find(second_string)

if pos > -1:
    print(f'The first row is obtained from the second with a shift {pos}.')
else:
    print('The first row cannot be obtained from the second using a circular shift.')




# Homework 2.5.6.9

#Context
#You are developing a program that analyzes text written by a user and returns statistics on the use of uppercase and lowercase letters.
#
#This can be useful, for example, when analyzing social media comments or processing text data for research.
#
#Task
#Write a program that reads a string and outputs the number of uppercase and lowercase letters in the string using the string methods.
#
#The program must do this in one pass along the line.
#
#The solution should be formatted as a function that takes a text string as input, and returns two numbers as output (the number of uppercase and lowercase letters).
#
#Example:
#
#text = input("Enter string to parse: ")
#uppercase, lowercase = count_uppercase_lowercase(text)
#print("Number of uppercase letters:", uppercase)
#print("Number of lowercase letters:", lowercase)
#Console output:
#
#Enter a string to parse: Hello World!
#Number of capital letters: 2
#Number of lowercase letters: 8
#Adviсe
#Recall the string methods you learned. Choose from them those that will help you check the letter (whether it is capital or not).
#To return multiple elements from a function, list them separated by commas:
#return a, b




def reserve_word(string):
    new_string=' '
    temp_string=' '
    temp_sym=' '
    for l in string:
        for sym in l:
            if sym.isalpha():
                temp_string+=sym
            else:
                temp_sym+=sym
        new_string+=temp_string[::-1]+temp_sym+' '
        temp_string=''
        temp_sym=''
    print(new_string)

messege=input("Enter messeges:").split()
reserve_word(messege)



