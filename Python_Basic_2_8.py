# Homework 2.8.8.1
def number(number):
    for i in range(1,number+1):
        print(i)



num=int(input('Enter number:'))
number(num)

# Homework 2.8.8.2

def zip_2(fst, scd, x=0):
    if x == len(fst) or x == len(scd):
        return zip_list
    zip_list.append((fst[x], scd[x]))
    return zip_2(fst, scd, x + 1)


first = (1, 3, 6, 8, 13)
second = 'what'
zip_list = []

zip_2(first, second)
print(zip_list)


# Homework 2.8.8.3

def something(number):
    f1=1
    f2=1
    for i in range(2,number):
        f1,f2=f2,f1+f2
    print(f2)


num=int(input('Enter number:'))
something(num)



# Homework 2.8.8.4


site = {'html': {'head': {'title': 'Мой сайт'},
                 'body': {'h2': 'Здесь будет мой заголовок','div': 'Тут, наверное, какой-то блок',
                 'p': 'А вот здесь новый абзац'}}}

def search(site_tree,key):
    if site_tree.get(key):
      return site_tree[key]
    for content in site_tree.values():
        if isinstance(content, dict):
            result = search(content, key)
            if result:
             break
    else:
        result = None
    # if result:

    return result

name=input('Enter key word:')
print(search(site,name))


# Homework 2.8.8.5
def calculating_math_func(data):
    numbers={}
    if data in numbers:
        print(data)
    else:
        factorial=1
        for i in range(1,data+1):
            factorial*=i
        factorial/=data**3
        factorial=factorial**10

        return factorial
        numbers.update('data',':', 'factorial')



number=int(input('Enter number:'))
print(calculating_math_func(number))



# Homework 2.8.8.6

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

def name(name):

     site['html']['head']['title'] = 'Куплю/продам {} недорого'.format(name)
     print(site)


while True:

    title=input('For which product do you wont to site:').title()
    name(title)




# Homework 2.8.8.7


def summa(*args,):
    total=[]
    for index,nums in enumerate(args):
        if isinstance(nums,list):
            for i in nums:
                if isinstance(i,int) or isinstance(i, float):
                   total.append(i)
                else:
                    total.extend(summa(i))
        else:
            total.append(nums)



    return total


print(sum(summa([[1, 2, [3]], [1], 3])))




# Homework 2.8.8.9
def move(n, start, finish):
    if n > 0:
        temp = 6 - start - finish
        move(n - 1, start, temp)
        print("Transfer disk", n, "from the rod", start, "to the rod", finish)
        move(n - 1, temp, finish)


n = int(input('Enter number of disks: '))
move(n, 1, 3)
