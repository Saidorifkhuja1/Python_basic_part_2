
# Homework 2.13.6.1
def gen_fuc(number):
    for i in range(1,number+1):
        yield i**2

user=int(input('Enter number:'))

gen=gen_fuc(user)
for i_elem in gen:
    print(i_elem,end=',')



# Homework 2.13.6.2
import os
from collections.abc import Iterable


def find_dir(folder: str, path: str) -> Iterable[str]:
    print('Current directory', path)
    for i_elem in os.listdir(path):
        current_path = os.path.join(path, i_elem)
        if os.path.isdir(current_path) and i_elem != folder:
            find_dir(folder, current_path)
        elif os.path.isfile(os.path.join(path, i_elem)):
            yield os.path.join(path, i_elem)



user_folder = input('Please enter name of katalog : ')
abs_path = os.path.abspath(os.path.join(os.path.sep))
result = find_dir(folder=user_folder, path=abs_path)
for i_path in result:
    print(i_path)



# Homework 2.13.6.3

import os
from collections.abc import Iterator

def count_lines(dir: str) -> Iterator[int]:
    """
    Generator to count non-empty lines in files
    :param dir: path to file directory
    """
    for root, dirs, files in os.walk(dir):
        for filename in files:
            path = os.path.join(root, filename)
            if path.endswith('.py'):
                with open(path, 'r', encoding='utf-8') as file:
                    for line in file:
                        if not line.strip() or line.strip().startswith('#'):
                            continue
                        else:
                            yield 1
        return


dir = os.path.abspath(input('Enter the path to the file folder: '))
result = 0
for line in count_lines(dir):
    result += line
print(f'In .py files of the directory {dir} total {result} non-empty lines')





# Homework 2.13.6.4

from typing import Optional,Any

class Node:
    def __init__(self,value:Optional[Any]=None,next:Optional['Node']=None)->None:
        self.value=value
        self.next=next

    def __str__(self)->str:
        return f'Node:{str(self.value)}'




class LinkedList:
    def __init__(self)->None:
        self.head:Optional[Node]=None
        self.leanth=0

    def __str__(self)->str:
        if self.head is not None:
            current=self.head
            values=[str(current.value)]
            while current.next is not None:
                current=current.next
                values.append(str(current.value))
            return '[{values}]'.format(values=' '.join(values))
        return 'LinkedList[]'

    def append(self,elem:Any)->None:
        new_node=Node(elem)
        if self.head is None:
            self.head=new_node
            return

        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
        self.leanth+=1

    def remove(self,index)->None:
        cur_node=self.head
        cur_index=0
        if self.leanth ==0 or self.leanth<=index:
            return IndexError

        if cur_node is not None:
            if index==0:
                self.head=cur_node.next
                self.leanth-=1
                return

        while cur_node is not None:
            if cur_index==index:
                break

            prev=cur_node
            cur_node=cur_node.next
            cur_index+=1


        prev.next=cur_node.next
        self.leanth -= 1



my_list=LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(my_list)
print()
my_list.remove(1)
print(my_list)





