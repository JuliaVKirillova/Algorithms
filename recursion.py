""" Найти определённый файл в компьютере """

import os

file_to_find = 'some_file'
path = os.getcwd()

def look_for_file(path):
    for _object in os.listdir(path):
        if os.path.isdir(_object):
            look_for_file(_object)
        else:
            if _object == file_to_find:
                return _object

# Комментарии к используемым методам:

os.path.isdir(path) # True, если объект является папкой
os.path.isfile(path) # True, если объект является файлом
os.getcwd() # узнать текущую директорию
os.listdir(path) # получить содержимое папки 


""" Создать матрёшку размера size с n-1 матрёшкой внутри. """

def matryoshka_builder(size, n):
    if n >= 1:
        print("Создаём низ матрёшки размера {}.".format(size))
        matryoshka_builder(size - 1, n - 1)
        print("Создаем верх матрешки размера {}.".format(size))  
        print('Матрешка размера {} готова!'.format(size))
    else:
        return 

#matryoshka_builder(4, 3) 
       

""" Рекурсия для чисел Фибоначчи """

def fib1(n):
    if n == 0 or n == 1:
        x = 1
    else:    
        x = fib1(n - 1) + fib1(n - 2)
    
    return x

#n = 5
#print(fib1(n))



fib_num = {
    0: 1,
    1: 1
}

def fib2(n):
    if n in fib_num:
        return fib_num[n]
    else:
        fib_num[n] = fib1(n - 1) + fib1(n - 2)
        return fib_num[n] 

#n = 5
#print(fib2(n))


def fib3(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a

#n = 5
#print(fib3(n))


def fib4(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b % 10, (a + b) % 10
    return a

#n = 2
#print(fib4(n))    


""" Рекурсивное вычисление факториала """

def factorial1(n):
    if n == 0 or n == 1:
        return 1
    else:
        f = n * factorial1(n - 1)
    return f

#n = 3
#print(factorial1(n))


""" Циклическое вычисление факториала """

def factorial2(n):
    if n == 0 or n == 1:
        return 1
    else:
        f = 1
        for i in range(2, n + 1):
            f *= i
    return f


def factorial3(n):
    if n == 0 or n == 1:
        return 1
    else:
        f = 1
        while n > 1:
            f *= n
            n -= 1
    return f

n = 5
#print(factorial2(n))
#print(factorial3(n))


""" Вывести буквы английского алфавита до заданной буквы """

letters = 'abcdefghijklmnopqrstuvwxyz'
result = ''
def alphabet(letter):
    idx = letters.index(letter)
    global result
    result = letter + ' ' + result
    while letter != letters[0]:
        return alphabet(letters[idx - 1])

#alphabet('d')
#print(result)


""" Вывести всевозможные правильные скобочные последовательности заданной длины """

def brackets_generator(n, open_b, close_b, s=''):
    if open_b + close_b == 2 * n:
        print(s)
        return

    if open_b < n:
        brackets_generator(n, open_b + 1, close_b, s + '(') 

    if open_b > close_b:
        brackets_generator(n, open_b, close_b + 1, s + ')')                

#n = int(input())
#brackets_generator(n, 0, 0)


""" Определить можно ли разделить n-монет различного достоинства на k победителей поровну """

def award():
    k, n = int(input()), int(input())
    coins = list(map(int, input().split()))
    
    if sum(coins) % k:
        return False

    coins.sort(reverse=True)
    winners = []

    for c in range(n):
        winners.append(coins.pop(0))

    while coins:
        winners[winners.index(min(winners))] += coins.pop(0)

    for i in range(k):
        if winners[k] == winners[k + 1]:
            continue
        else:
            return False
    return True                 

#print(award())


""" Определить какой символ будет находиться на n-строке на k-позиции
0 меняется на 01, 1 меняется на 10
1. 0
2. 01
3. 0110  """

def interchange(s):
    s = list(s)
    for i in range(0, len(s) - 1, 2):
        s[i], s[i + 1] = s[i + 1], s[i]
    s = ''.join(s)
    return s    

def string_generator(n, k, s='01', counter=1):
    if n == 1:
        return 0

    if n == 2:
        s = '01'    

    if counter == n - 1:
        return s[k - 1]
    else:    
        s = s + interchange(s)
        return string_generator(n, k, s, counter + 1)

#n, k = int(input()), int(input())
#print(string_generator(n, k))


""" Вычислить квадратный корень из 2 только с помощью +, -, *, /  """

def square():
    a = 1
    for _ in range(3):
        a = a / 2 + 1 / a
    a = str(a)
    a = a[:7]    
    return a
    #return round(a, 5)

#print(square())    


""" Вывести количество способов, которым можно набрать нужную сумму
Монеты разных достоинств можно брать бесконечно раз """

def get_money(m, n, coins):
    if m == 0:
        return 1
    if n == 1 and m % coins[0] != 0:
        return 0

    s = [[0 for __ in range(m + 1)] for _ in range(n + 1)]

    for i in coins:
        for j in range(m + 1):
            if j == 0 or j == 1:
                s[i][j] = 1 
                continue

            if j < i:
                s[i][j] = s[i - 1][j]
            else:
                s[i][j] = s[i - 1][j] + s[i][j - i]    

    return s[i][j]              


def exchange(m, coins):
    if m == 0:
        return 1
    i = 0
    combinations = 0
    while i < len(coins):
        if coins[i] <= m:
            combinations += exchange(m - coins[i], coins[i:])
        i += 1    
    return combinations        


#m, n = int(input()), int(input())
#coins = list(map(int, input().split()))
#coins = sorted(coins)

#coins = sorted(map(int, input().split()), reverse=True)
#print(exchange(m, coins))
#print(get_money(m, n, coins))    


""" Вывести максимально возможный размер квадратных участков, 
на который можно разделить территорию """

def get_size(a, b):
    if a % b == 0:
        return b
    elif b % a == 0:
        return a   
    else:
        if a > b:
            a = a - b * (a // b)
            return get_size(a, b)
        elif a < b:
            b = b - a * (b // a)
            return get_size(a, b)

#b, a = int(input()), int(input())
#print(get_size(a, b))            


""" Найти НОД(a, b) и коэффициенты x, y, такие что 
а * х + b * y = НОД(a, b) """

def get_gcd(a, b):
    if a == 0:
        return 0, 1, b

    x1, y1, gcd = get_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return x, y, gcd


#a, b = int(input()), int(input())
#print(*get_gcd(a, b))


""" Алгоритм бинарного поиска в массиве, 
отсортированном по возрастанию без повторяющихся элементов """

""" def binarySearch1(arr, x, l = 0, r = len(arr)-1): 
    if r >= l: 
        mid = l + (r - l) // 2

        if arr[mid] == x: 
            return mid 

        elif arr[mid] > x: 
            return binarySearch1(arr, x, l, mid - 1) 

        else: 
            return binarySearch1(arr, x, mid + 1, r) 
    else: 
        return -1  """


""" Алгоритм бинарного поиска в массиве, 
отсортированном по убыванию без повторяющихся элементов """

""" def binarySearch2(arr, x, l = 0, r = len(arr) - 1): 
    if r >= l: 
        mid = l + (r - l) // 2

        if arr[mid] == x: 
            return mid 

        elif arr[mid] < x: 
            return binarySearch2(arr, x, l, mid - 1) 

        else: 
            return binarySearch2(arr, x, mid + 1, r) 
    else: 
        return -1  """


""" Алгоритм быстрого возведения в степень """

def recursive_power(x, n):
    if n == 0:
        return 1

    if n % 2:
        return x * recursive_power(x, n - 1)
    else:
        m = recursive_power(x, n // 2)
        return m * m 

#print(recursive_power(2, 5))


""" Алгоритм генерации всех двоичных последовательностей длины n """

def gen_binary(n, prefix):
    if n == 0:
        print(prefix)
    else:
        gen_binary(n - 1, prefix + '0')
        gen_binary(n - 1, prefix + '1') 

#print(gen_binary(3, ''))


""" Поиск индекса искомого элемента 
в неотсортированном / частично отсортированном массиве  
= линейный (последовательный) поиск"""

def search(k, array):
    for a in range(len(array)):
        if k == array[a]:
            return a
    return -1    


def search1(k, array, l=0, r = 0):
    if r >= l: 
        mid = l + (r - l) // 2

        if array[mid] == k: 
            return mid 

        elif array[mid] > k: 
            return search1(k, array, l, mid - 1) 

        else: 
            return search1(k, array, mid + 1, r) 
    else: 
        return -1


#n, k = int(input()), int(input())
#array = list(map(int, input().split()))
#print(search(k, array))
#print(search1(k, array, r = n - 1))