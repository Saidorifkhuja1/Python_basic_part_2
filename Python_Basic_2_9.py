# Homework 2.9.6.1

myfile='numbers.txt'
summ=0
with open(myfile) as fh:

    for n in fh:
     n=n.strip()
     summ=summ+int(n)
print(summ)

# Homework 2.9.6.2

reader = open('zen.txt', 'r')
lines = [line for line in reader]
print(*reversed(lines), sep='')


# Homework 2.9.6.3

import os

reader = open('zen.txt', 'r')
word_cnt = sym_cnt = line_cnt = 0
sym_dict = dict()

for line in reader:
    line = line.replace('--', '').lower()
    word_cnt += len(line.split())
    for sym in line:
        if sym.isalpha():
            sym_cnt += 1
            if sym in sym_dict:
                sym_dict[sym] += 1
            else:
                sym_dict[sym] = 1
    line_cnt += 1

print(f'Число слов: {word_cnt}', f'Число символов: {sym_cnt}', f'Число строк: {line_cnt}', sep='\n')
for res in sorted(sym_dict, key=sym_dict.get):
    print('Самая редкая буква: {} - {}'.format(res, sym_dict[res]))
    break


# Homework 2.9.6.4

import os
def information(link,folder_c=0,file_c=0,size=0):
    for i in os.listdir(link):
        total=os.path.join(link,i)
        if os.path.isfile(total):
            size+=os.path.getsize(total)
            file_c+=1
        elif os.path.isdir(total):
            folder_c+=1
            information(total,folder_c,size,file_c)
    return (folder_c,file_c,size/1024)


folder,size,file=information(input('Enter link:'))
print(f'Directory size :{size}')
print(f'Size files:{file}')
print(f'Amount folders:{folder}')




# Homework 2.9.6.5
import os
name=input('Enter file name:')
place=input('Where do you wont to save:')
file=' '.join(f'{place}{name}')
print('File sucsesfully saved')
print(f'File contents:{name}')



# Homework 2.9.6.6
import os
shift=1
cipher_text=''
cipher_sym=''
cipher_list=[]
alhabet='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
file_text=open('text.txt', 'r' )
for i in file_text:
    cipher_text=''
    shift+=1
    for sym in i:
        cipher_sym=alhabet[(alhabet.find(sym)+shift)%52]
        cipher_text=cipher_text+cipher_sym
    print(cipher_list)


# Homework 2.9.6.7
k=int(input('Enter maximum score:'))
dict_player=dict()
while True:
    player=input('Enter familiy name,name and amount of scores with space: ')
    if player!='stop':
        if len(player)!=3:
            print('Error')
        else:
            new_list=list()
            for i in range(len(player)-1):
                new_list.append(player[i])
            tup=tuple(new_list)
            dict_player[tup]=player[2]
            print(dict_player)
    else:
        break

print(dict_player)


# Homework 2.9.6.8

open_text = open('text.txt', 'r')
sym_list = [sym.lower () for sym in open_text.read() if sym. isalpha()]
sym_dict = {}
for sym in sym_list:
   sym_dict[sym] = sym_dict.get(sym, 0) + 1
new_string =''
for key, value in sym_dict.items():
  sym_dict [key] = (round (value/len (sym_list), 3))

for key, value in sorted(sym_dict. items()):
  print(key, value)


  
# Homework 2.9.6.9

import collections
import zipfile

def unzip(archive):
    zfile=zipfile.ZipFile(archive,'r')
    for i_file_name in zfile.namelist():
        zfile.extract(i_file_name)
    zfile.close()


def collect_stats(file_name):
    result={}
    if file_name.endswith('.zip'):
        unzip(file_name)
        file_name=''.join((file_name[:-3], 'txt'))
    text_file=open(file_name, 'r',encoding='utf-8')
    for i_line  in text_file:
        for j_char in i_line:
            if j_char.isalpha():
             if j_char not in result:
                 result[j_char]=0
             result[j_char]+=1
    text_file.close()
    return result


def print_stats(stats):
    print('+{:-^19}+'.format('+'))
    print('|{: ^9}|{: ^9}|'.format('буква',' частота'))
    print('+{:-^19}+'.format('+'))
    for char,count in stats.items():
        print('|{: ^9}|{: ^9}|'.format(char,count))
    print('+{:-^19}+'.format('+'))



def sort_by_frequency(stats_dict):
    sorted_values=sorted(stats_dict.values(),reverse=True)
    sorted_dict=collections.OrderedDict()
    for i_value in sorted_values:
        for j_key in stats_dict.keys():
            if stats_dict[j_key]==i_value:
                sorted_dict[j_key]=stats_dict[j_key]
    return sorted_dict


file_name='voyna-i-mir.zip'
stats=collect_stats(file_name)
stats=sort_by_frequency(stats)
print_stats(stats)


