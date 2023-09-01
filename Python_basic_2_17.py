

# Homework 2.17.7.1

floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
print(list(map(lambda x:round(x**3,3),floats)))


names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
names1 = [x for x in names if len(x) >= 5]
print(names1)

numbers = [22, 33, 10, 6894, 11, 2, 1]
numbers1 = 0 if numbers == [] else (lambda F, L : F(F, L))(lambda F, L : L[0] * (1 if len(L)==1 else F(F, L[1:])), numbers)
print(numbers1)




# Homework 2.17.7.1

letters = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
conc = lambda x, y : [x, y]
results = [conc(letters[i], numbers[i]) for i in range(len(letters))]
print(results)




# Homework 2.17.7.3

from collections import Counter

def func(val:str)->bool:
    return len(list(filter(lambda x:x%2,Counter(val).values())))<=2


print(func('ababc'))
print(func('abbbad'))
