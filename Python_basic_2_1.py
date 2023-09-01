# Homework 2_1_8_1
info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(),
    sys.version,
    platform.architecture(),
)
print(info)

with open('os_info.txt', 'w', encoding='utf8') as file:
    file.write(info)


# Homework 2_1_8_2



print("Enter first point:")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nEnter second point:")
x2 = float(input('X: '))
y2 = float(input('Y: '))

print("The equation of a straight line passing through these points:")
x_diff = x1 - x2
y_diff = y1 - y2
if x_diff == 0:
    print("x = ", x1)
elif y_diff == 0:
    print("y = ", y1)
else:
    k = y_diff / x_diff
    b = y2 - k * x2
    print("y = ", k, " * x + ", b)


# Homework 2_1_8_3

def summN(number,summ):
    summ=0
    while number!=0:
      last_digit=number%10
      summ=summ+last_digit
      number//=10
    print(summ)
    return summ

def countN(number,dig):
    count=number
    while count!=0:
        dig+=1
        count//=10
    print(dig)
    return dig

summ=0
dig=0
number=int(input('Enter number:'))

print('Difference betwin summ and dig:',summN(number,summ)-countN(number,dig))


# Homework 2_1_8_4

def reverse(number):
  rev_number =''
  while number!=0:
    rev_number +=str(int(number%10))
    number //= 10
  return str(rev_number)


num_1 = float(input('Enter first number: '))
num_2 = float(input('Enter second number: '))
rev_num_1 = reverse(num_1)
rev_num_2 = reverse(num_2)

summ_num = float(rev_num_1) + float(rev_num_2)
print("\nfirst number reserve: ", rev_num_1)
print("second number reserve: ", rev_num_2, '\n')
print('summ: ', summ_num)

# Homework 2_1_8_5

n=int(input('Enter number:'))
x=n
while x>1:
    if n%x==0 :
        num=x

    x-=1
print('The smallest divisor other than one:',num)

# Homework 2_1_8_6

def main( ):
    x=float( input( 'Enter coordination  х: ' ))
    y= float(input('Enter coordination y:'))
    radius=int(input('Enter radius:'))
    if  x+y<=radius:
       print("Coin here somewhere")
       print( )
    else:
       print( 'Coin is not near')
       print()
main()

# Homework 2_1_8_7


first_year = int(input('Введите первый год: '))
second_year = int(input('Введите второй год: '))

print('Годы от', first_year, 'до', second_year, 'с тремя одинаковыми цифрами:')
for i_year in range(first_year, second_year + 1):
    digit_1 = i_year % 10
    digit_2 = i_year // 10 % 10
    digit_3 = i_year // 100 % 10
    digit_4 = i_year // 1000
    if digit_1 == digit_2 == digit_3 \
            or digit_1 == digit_2 == digit_4 \
            or digit_2 == digit_3 == digit_4\
            or digit_1 == digit_3 == digit_4:  # в лоб
        print(i_year)



