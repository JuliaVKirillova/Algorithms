import math
from itertools import product


""" Вывести значение функции в точке х """
def function_value():
    a, x, b, c = map(int, input().split()) 
    y = a * x ** 2 + b * x + c
    print(y)

#function_value()


""" Вывести из каких k-вузов присутствует больше всего гостей  """
def conference_lovers():
    colleges = list(map(int, input().split()))
    k = int(input())
    d = {}
    for e in colleges:
        d[e] = colleges.count(e)
    d = list(d.items()) 
    d.sort(key=lambda i: i[1], reverse=True)
    d = d[:k]
    for x in d:
        print(x[0], end=' ')

#conference_lovers()


""" Вывести списочную форму числа Х + К, 123 -> [1, 2, 3] """
def list_form():
    n = int(input())
    x = list(map(int, input().split()))
    k = int(input())
    x = (''.join(map(str, x)))
    x_k = int(x) + k
    for i in str(x_k): 
        print(''.join(i), end=' ')

#list_form()


""" Удалить нули из строки """
def remove_zeros():
    n = int(input())
    days = input().split()
    while '0' in days:
        days.remove('0')
    print(*days)  

#remove_zeros() 


""" Вывести двоичное представление числа """
def binary_system():
    x = int(input())
    num = ''
    while x > 0:
        num = str(x % 2) + num
        x //= 2
    print(num)

#binary_system()


""" Вывести повторяющееся число """
def find_duplicate():
    n = int(input())
    ids = list(map(int, input().split()))
    for i in ids:
        if ids.count(i) != 1:
            print(i)
            break

#find_duplicate()            


""" Проверить, являются ли слова анаграммами """
def is_anagramma():
    word1, word2 = input(), input()
    counter = 0
    for l in word1:
        if l in word2:
            counter += 1
    if counter == len(word1):
        print('True')
    else:    
        print('False')

#is_anagramma()


""" Проверить, является ли фраза палиндромом """
def is_palindrome():
    s = input().lower()
    new_s = ''
    for l in s:
        if l.isalpha():
            new_s += l
    if new_s == new_s[::-1]:
        print('True')
    else:
        print('False')           
                
#print(is_palindrome())


""" Вывести сумму двоичных чисел """
def sum_of_binary_numbers():
    x, y = input(), input()
    s = ''
    tmp = '0'
    if len(x) > len(y):
        dif = len(x) - len(y)
        y = '0' * dif + y
    elif len(x) < len(y):
        dif = len(y) - len(x)
        x = '0' * dif + x
    for i in range(len(x) - 1, -1, -1):
        if x[i] == '0' and y[i] == '0':
            s += tmp + '0'
        elif (x[i] == '0' and y[i] == '1') \
            or (x[i] == '1' and y[i] == '0') and tmp == '0':
            s += '1'
        elif (x[i] == '0' and y[i] == '1') \
            or (x[i] == '1' and y[i] == '0') and tmp == '1':
            s += '0'
            tmp = '1'
        elif x[i] == '1' and y[i] == '1' and tmp == '0':
            s += '0'
            tmp = '1'
        else:
            s += '1'
            tmp = '1'
    if s[0] == '0':
        s = s[1:]    
    print(s)

#sum_of_binary_numbers()                                    


""" Вывести число, которое встречается 1 или больше 2 раз """
def find_unique_id():
    n = int(input())
    ids = list(map(int, input().split()))
    for i in ids:
        if ids.count(i) != 2:
            print(i)
            break

#find_unique_id()


""" Вывести сколько единиц встречается в двоичной записи числа """
def find_one():
    n = int(input())
    num = ''
    while n > 0:
        num = str(n % 2) + num
        n //= 2
    n = num.count('1')
    print(n)

#find_one()


""" Вывести лишнюю букву """
def find_unique_letter():
    s, t = list(input()), list(input())
    if len(s) > len(t):
        for i in s:
            if i not in t:
                print(i)
                break
            else:
                t.remove(i)
    else:
        for j in t:
            if j not in s:
                print(j)
                break
            else:
                s.remove(j)

#find_unique_letter()


""" Вывести строку, в которой символы отсортированы в порядке убывания частотности """
def find_frecuencies():
    s = input()
    f = {}
    for i in s:
        f[i] = s.count(i)
    f = list(f.items())
    s = ''
    f.sort()
    for j in f:
        s += str(j[0]) * int(j[1])
    print(s)

#find_frecuencies()


""" Определить, является ли число степенью четверки """
def power_of_four():
    n = int(input())
    if (math.log(n, 4)).is_integer():
        print('True')
    else:
        print('False')

#power_of_four()


""" Объединить два списка и отсортировать их по возрастанию """
def merge_sort():
    x = list(map(int, input().split()))
    m, k = int(input()), int(input())
    y = list(map(int, input().split()))
    x = x[:m]
    x = x + y
    x.sort()
    print(*x)

#merge_sort()


""" Вывести все возможные комбинации """
def find_combinations():
    s = input()
    buttons = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    x = []
    for i in s:
        if i in buttons:
            x.append((buttons[i]))     
    
    result = list(product(*x))

    t = []
    for a in range(len(result)):
        for b in range(len(result[a]) - 1):
            t.append(result[a][b] + result[a][b + 1])
            continue
            
    print(*t)    
    
#find_combinations()            


""" Определить максимальное произведение заработанных очков среди троек дней, 
в которых сумма очков равна 0, а произведение положительное """
def find_max_point():    
    n = int(input())
    lst = list(map(int, input().split()))
    max_multi = -1
    neg_lst, pos_lst = [], []
    
    for i in lst:
        if i < 0:
            neg_lst.append(i)
        else:
            pos_lst.append(i)
    
    pos_lst.sort()
    
    for j in range(len(neg_lst) - 1):
        tmp1 = neg_lst[j] + neg_lst[j + 1]
        tmp2 = neg_lst[j] * neg_lst[j + 1]
        if abs(tmp1) in pos_lst:
            if max_multi <= tmp2 * abs(tmp1):
                max_multi = tmp2 * abs(tmp1)       
    
    print(max_multi)

#find_max_point()



""" Правильная скобочная последовательность """
def is_correct_bracket_seq():
    s = input()
    tmp = 0
    for b in s:
        if b == '(' or b == '[' or b == '{':
            tmp += 1
        elif b == ')' or b == ']' or b == '}':
            tmp -= 1
    if tmp == 0:
        print('True')
    else:
        print('False')

#is_correct_bracket_seq()


""" Определить сколько анаграмм шаблона в строке """
def find_anagram():
    s, sample = input(), input()
    if len(sample) > len(s):
        print('error')
    else:    
        counter = 0
        for i in sample:
            if s.count(i) >= 1:
                counter += 1
        if counter == len(sample):
            max_elem = 1
            for j in sample:
                if s.count(j) >= max_elem:
                    max_elem = s.count(j)
            print(max_elem)
        else:
            print('There is no anagrams')                

#find_anagram()
              

""" Задача 1
Условие задачи: дан массив nums, состоящий из целых чисел, и целое число val. 
Нужно удалить все вхождения val в nums и вернуть длину массива после удаления. 
При подсчёте длины можно не учитывать крайние левые или крайние правые элементы, равные val. """

""" Решение № 1 """
def removeTarget(nums, val):
    result = []
    for num in nums:
        if num != val:
            result.append(num)
    return len(result) 


""" Решение № 2 """
def removeTarget(nums, val):
    for i in range(len(nums)):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                continue
            else:
                i += 1
    return len(nums) 


""" Решение № 3   """  
def removeTarget(nums, val):
    start = 0
    end = len(nums) - 1
    mid = 0
    while mid <= end:
        if nums[mid] != val:
            nums[start], nums[mid] = nums[mid], nums[start]
            start += 1
            mid += 1
        else:
            mid += 1
    return start 


""" Задача 2
Дан связный список. 
Нужно написать функцию swapNodes, 
которая будет менять местами каждые два соседних узла и возвращать голову списка.    """ 

""" Пример 1:
Дан связный список 1 —> 2 —> 3 —> 4
Ответ в этом случае такой: 2 —> 1 — > 4 —> 3

Пример 2:
Дан связный список a —> b —> c
Ответ: b — > a — > c """

class MyNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def swapNodes(head):
    cur = head
    tmp = MyNode('-1')
    tmp.next = head
    prev = tmp
    while cur is not None and cur.next is not None:
        cur_next = cur.next
        next_tmp = cur_next.next
        prev.next = cur_next
        cur_next.next = cur
        cur.next = next_tmp
        prev = cur
        cur = next_tmp
    return tmp.next  


#node = MyNode(1, MyNode(2, MyNode(3, MyNode(4))))
#node = swapNodes(node)

#while node:
    #print(node.value)
    #node = node.next



""" Задача 2.
Дана закодированная строка, нужно её декодировать. 
Кодирование производится так: n[symbol] значит, что символ повторяется n раз.    """ 

""" Пример 1:
Входная строка: "2[a]3[bc]1[d]" Ответ: 'aabcbcbcd'
Пример 2:
Входная строка: "3[a2[b]]" Ответ: 'abbabbabb' """


def transformString(input_string):
    stack = []
    result = ''
    tmp = ''
    # Пройдем по всем символам строки
    for symbol in input_string:
        if stack:
            # Если стек не пуст
            if symbol != ']':
                # Если число больше 9, то нужно соединить цифры в число
                if stack[-1].isdigit() and symbol.isdigit():
                    # Если на верхушке стека цифра, прибавляем текущее значение
                    stack[-1] += symbol
                else:
                    # Добавляем символ в стек
                    stack.append(symbol)
            else:
                # Если текущий символ ']' извлекаем из стека элементы, пока не дойдем до '[' 
                while stack[-1] != '[':
                    tmp = stack.pop() + tmp
                stack.pop() # Извлекаем '['
                multiplier = stack.pop() # Извлекаем число необходимых повторений 
                tmp *= int(multiplier)
                # Если стек пуст, текущая итерация завершена, можно изменить переменную result
                if not stack:
                    result += tmp
                else:
                    # Иначе снова положим tmp в стек 
                    stack.append(tmp)
                tmp = '' # Присвоим переменной tmp пустую строку
        elif symbol.isalpha():
            # Если стек пуст, и текущий символ - буква, добавим ее к результату
            result += symbol
        else:
            # Иначе положим символ в стек
            stack.append(symbol)      
    return result 

#print(transformString("2[a]3[bc]"))
                                
