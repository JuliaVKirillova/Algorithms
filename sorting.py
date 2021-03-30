""" Сортировка выбором на месте
сложность O(n^2) """

def selection_sort(l):
    for i in range(len(l)-1):
        need_replace = False
        max_elem = l[i]
        for j in range(i, len(l)):
            if l[j] > max_elem:
                need_replace = True
                max_elem = l[j]
                max_pos = j
        if need_replace:
            tmp = l[i]
            l[i] = max_elem
            l[max_pos] = tmp
    return l 


""" Сортировка пузырьком 
сложность O(n^2) в худшем случае, в лучшем O(n) """

def buble_sort(l):
    for _ in range(len(l)- 1):
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
    return l            

#n = int(input())
#l = list(map(int, input().split()))
#print(*buble_sort(l))    


""" Сортировка вставками 
сложность O(n^2), в лучшем случае O(n) """

def insert_sort(l):
    for i in range(len(l)):
        if i == 0:
            continue
        if l[i] < l[i - 1]:
            l[i], l[i - 1] = l[i - 1], l[i]
        
        for j in range(i - 1, 0, -1):
            while l[j - 1] > l[j] and j > 0:
                l[j], l[j - 1] = l[j - 1],  l[j]
                j -= 1
    return l                                


#n = int(input())
#l = list(map(int, input().split()))
#print(*insert_sort(l))     


""" Алгоритм поиска k-й порядковой статистики 
сложность  O(n) в среднем, в худшем O(n^2)"""

from random import choice

def statistics_search(s, k):
    v = choice(s)
    sl = [elem for elem in s if elem < v]
    sv = [elem for elem in s if elem == v]
    sr = [elem for elem in s if elem > v]
    
    if k <= len(sl):
        return statistics_search(sl, k)
    elif len(sl) < k <= len(sl) + len(sv):
        return v
    elif k > len(sl) + len(sv):
        return statistics_search(sr, k - len(sl) - len(sv))      

#k = int(input())
#s = list(map(int, input().split())) 
#print(statistics_search(s,k))


""" Быстрая сортировка или сортировка Хоара
сложность O(nlogn) в среднем, или O(n^2) в худшем"""

def quicksort(array):
    if len (array) < 2:
        return array

    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater) 

#array = list(map(int, input().split())) 
#print(*quicksort(array))


""" Быстрая сортировка без использования дополнительной памяти """

def quick_sort(array, l, r):
    if l >= r:
        return 
    else:
        pivot = choice(array[l:r + 1])
        i = l
        j = r
        while i <= j:
            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            if i <= j:
                array[i], array[j] = array[j], array[i]  
                i += 1
                j -= 1
                quick_sort(array, l, j)
                quick_sort(array, i, r)  
    return array                    

#n = int(input())
#array = list(map(int, input().split())) 
#print(*quick_sort(array, 0, len(array) - 1))


""" Вывести номера, которые встречаются в обоих списках 
Реализация с помощью бинарного поиска и быстрой сортировки"""

def binarySearch1(arr, x, l = 0, r = 0): 
    if r >= l: 
        mid = l + (r - l) // 2

        if arr[mid] == x: 
            return mid 

        elif arr[mid] > x: 
            return binarySearch1(arr, x, l, mid - 1) 

        else: 
            return binarySearch1(arr, x, mid + 1, r) 
    else: 
        return -1


def unique_numbers(l, s):
    s = quicksort(s)
    for i in l:
        if binarySearch1(s, i, 0, len(s) - 1) != -1:
            print(i, end=' ')


#n, m = int(input()), int(input())
#l, s = list(map(int, input().split())), list(map(int, input().split()))
#unique_numbers(l, s)


""" Вывести номера, которые встречаются в обоих списках,
столько раз сколько они встречаются в списках одновременно
Ввод:
1 1 1
1 1

Вывод:
1 1 """

def repeated_numbers(l, s):
    s = sorted(s)
    for i in l:
        if i in s:
            print(i, end=' ')
            s.remove(i)

#n, m = int(input()), int(input())
#l, s = list(map(int, input().split())), list(map(int, input().split()))
#repeated_numbers(l, s)


""" Сортировка по четности """

def even_sort(array, n):
    even = [i for i in array if i % 2 == 0]
    uneven = [j for j in array if j % 2 != 0]

    for elem in range(n // 2):
        print(even[elem], end=' ')
        print(uneven[elem], end=' ')
    
#n = int(input())
#array = list(map(int, input().split()))
#even_sort(array, n)


""" Вывести наибольший периметр треугольника, 
который возможно составить из сторон с заданными длинами """

def perimeter(array):
    array = sorted(array, reverse=True)
    m = 0

    for a in range(len(array) - 2):
        if array[a] < array[a + 1] + array[a + 2] \
        and m < array[a] + array[a + 1] + array[a + 2]:

            m = array[a] + array[a + 1] + array[a + 2]
    
    return m        

#n = int(input())
#array = list(map(int, input().split()))
#print(perimeter(array))


""" Алгоритм сортировки слиянием
сложность O(nlogn) """

def merge_sort(array):
    if len(array) < 2:
        return array
    
    left = array[:len(array) // 2]
    right = array[len(array) // 2:]
    left = merge_sort(left)
    right = merge_sort(right)
    
    i, j, r = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[r] = left[i]
            i += 1
        else:
            array[r] = right[j]
            j += 1
        r += 1

    while i < len(left):
        array[r] = left[i]
        i += 1
        r += 1

    while j < len(right):
        array[r] = right[j]          
        j += 1
        r += 1

    return array 

#array = list(map(int, input().split()))
#print(*merge_sort(array))       


""" Алгоритм сортировки подсчетом
сложность O(n+k) """

def counting_sort(a):
    counter = [0 for _ in range(max(a) + 1)]
    
    for i in range(len(a)):
        counter[a[i]] += 1

    sorted_a = []

    for j in range(len(counter)):
        while counter[j] != 0:
            sorted_a.append(j)
            counter[j] -= 1

    return sorted_a            

#a = [5, 7, 1, 0, 1, 5, 11, 1] 
#print(*counting_sort(a))


""" Алгоритм поразрядной сортировки """

def countingSort(arr, digit):  
    
    n = len(arr)  
    count = [0] * (10)  
    output = []
    
    for i in range(0, n):  
        index = (arr[i] % 10 ** digit) // 10 ** (digit - 1)
        count[index] += 1
    
    for idx in range(10):
        while count[idx] != 0:
            for i in arr:
                if idx == i % 10 ** digit // 10 ** (digit - 1):
                    output.append(i)
                    count[idx] -= 1   
            break             
    
    return output

def radix_sort(arr):
    k = len(str(max(arr)))
    digit = 1
    while k >= digit:
        arr = countingSort(arr, digit)
        digit += 1 
    return arr    

#arr = list(map(int,input().split()))
#print(*radix_sort(arr))


""" Вывести координаты непересекающихся отрезков
Ввод:
7 8
2 2 
2 3 
6 10

Вывод:
2 3
6 10
"""

def get_areas(array):
    for a in range(len(array) - 1, -1, -1):
        if array[a][0] <= array[a - 1][1] <= array[a][1]:
            if array[a][0] <= array[a - 1][0] <= array[a][1]:
                array.remove(array[a - 1])
            else:
                array[a][0] = array[a - 1][0]
                array.remove(array[a - 1])   
    return array            


#n = int(input())
#sections = []
#for _ in range(n):
    #sections.append(list(map(int,input().split())))
#sections = sorted(sections, key=lambda x: x[1])
#sections = get_areas(sections)
#for s in sections:
    #print(*s)


""" Отсортировать по возрастанию """

def sorted_clothes(colors):
    a, b, c = 0, 0, 0
    for i in colors:
        if i == 0:
            a += 1
        elif i == 1:
            b += 1
        else:
            c += 1
    s = '0' * a + '1' * b + '2' * c
    for j in s:
        print(j, end=' ')               


#n = int(input())
#if n == 0 or n is None:
    #print('')
#else:
    #colors = list(map(int, input().split()))
    #sorted_clothes(colors)    


""" Относительная сортировка (задан образец) """

def relative_sort(lst, exp):
    counter = [0 for _ in range(max(exp) + 1)]
    sorted_lst, left = [], []
    
    for i in range(len(lst)):
        if lst[i] in exp:
            counter[lst[i]] += 1
        else:
            left.append(lst[i])    

    for e in exp:
        while counter[e] != 0:
            sorted_lst.append(e)
            counter[e] -= 1

    left = sorted(left)

    sorted_lst.extend(left)
    return sorted_lst        

#n = int(input())
#lst = list(map(int, input().split()))
#m = int(input())
#exp = list(map(int, input().split()))
#print(*relative_sort(lst, exp))


""" Алгоритм частичной сортировки """

def partial_sort(lst):
    k = 1
    for l in range(len(lst) - 1):
        if abs(lst[l] - lst[l + 1]) == 1:
            k += 1
    if k != 2:        
        return k
    return k - 1

#n = int(input())
#lst = list(map(int, input().split()))
#print(partial_sort(lst))


""" Вывести самое длинное подслово """

def subword(word, s):
    max_w = 0
    
    i, j = 0, 0
    while i < len(word):
        while j < len(s):
            if word[i] == s[j]:
                max_w += 1
                i += 1
                j += 1
            else:
                i += 1     
            if i < len(word):
                continue
            else:
                break
        break         
    return max_w

#max_length = 0
#s = []
#word = input()
#n = int(input())
#for _ in range(n):
    #s.append(input())

#for i in range(n):
    #length = subword(word, s[i])
    #if max_length < length:
        #max_length = length
        #max_word = s[i]

#print(max_word)


""" Сортировка матрицы по диагонали 
n = row
m = column """

def diagonal_sort(martix, n, m):
    for column in range(m - 1):
        diagonal_list = []
        col = column

        for row in range(n):
            diagonal_list.append(matrix[row][col])
            col += 1

            if col >= m:
                break
        
        diagonal_list = sorted(diagonal_list)
        col = column    

        for row in range(n):
            martix[row][col] = diagonal_list[row]
            col += 1

            if col >= m:
                break

    for row in range(1, n):
        diagonal_list = []
        r = row

        for column in range(m):
            diagonal_list.append(matrix[r][column])
            r += 1

            if r >= n:
                break

        diagonal_list = sorted(diagonal_list)
        r = row

        for column in range(m):
            matrix[r][column] = diagonal_list[column]
            r += 1

            if r >= n:
                break

    return matrix                   

#n, m = int(input()), int(input())
#matrix = []
#for _ in range(n):
    #matrix.append(list(map(int,input().split()))) 
#print(diagonal_sort(matrix, n, m))


""" Индекс «замечаемости» автора равен k, 
если из всех n его работ на k ссылаются минимум k раз другие авторы, 
а остальные n-k− работ имеют не более k ссылок 
Определить индекс по списку работ"""

def noticeIndex(arr):
    arr.sort(reverse = True)
    notice_index = 0
    for i in range(len(arr)):
        if arr[i] > notice_index:
            notice_index += 1
        else:
            break
    return notice_index 


#arr = [3, 0, 4, 1, 5]
#print(noticeIndex(arr))


""" Сортировка слиянием связного списка 
Сложность O(nlogn)"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        return str(self.val) 


def sortList(head):
    if not head:
        return None

    length = 1
    node = head
    tail = None
    while node.next:
        node = node.next
        length += 1
    tail = node
    return merge_sort(head, tail, length) 


def merge_sort(head, tail, length):
    # Базовый случай
    if head == tail:  # Длина списка равна 1
        head.next = None
        return head

    if head.next == tail:  # Длина списка равна 2
        if head.val < tail.val:
            tail.next = None
            return head
        head.next, tail.next = None, head
        return tail

    # Рекурсивный случай
    i = 1 # Определяем центральный элемент
    node = head
    while i < length / 2:
        node = node.next
        i += 1
        
    length1 = length2 = length / 2
    if length % 2: # Если длина нечётная 
        length2 += 1 # Нужно увеличить переменную, равную длине правой части

    tail1, head2 = node, node.next # Задаём конец левого списка и начало правого
        # Рекурсивно вызываем функцию для левой и правой частей
    left_part = merge_sort(head, tail1, length1)
    right_part = merge_sort(head2, tail, length2)

    return merge(left_part, right_part)  


def merge(head1, head2):
        # Выбираем меньший элемент в качестве cur. Его next сохраняем в tmp
    # Больший элемент записывем в other
    if head1.val < head2.val:
        cur, tmp, other = head1, head1.next, head2
    else:
        cur, tmp, other = head2, head2.next, head1
    mergedList = cur # Сохраняем в переменной, чтобы потом вернуть из функции
    # Если у меньшего элемента не было next, записываем в это поле больший и возвращаем 
    if not tmp:
        cur.next = other
        return mergedList
        
    while tmp: # Выбираем меньший элемент из tmp и other
        if tmp.val < other.val: # Если tmp меньше, просто передигаемся по списку на 1
            cur, tmp = tmp, tmp.next
        else: # Если нужно взять элемент из другого списка
            t = tmp # Сохраняем во временную переменную для обмена
            cur.next = other # Добавляем выбранный элемент
            cur = other # Переставляем указатель
            other = t # Производим обмен
            tmp = cur.next # Обновляем значение tmp
    cur.next = other # Добавляем оставшуюся часть

    return mergedList # Возвращаем результат слияния


""" Вывести самое большое число, которое можно составить из заданных чисел """

def big_number(l):
    for _ in range(len(l)- 1):
        for i in range(len(l) - 1):
            if l[i] + l[i + 1] < l[i + 1] + l[i]:
                l[i], l[i + 1] = l[i + 1], l[i]
    print(''.join(l))  


from typing import Text

class String(str):
    def __lt__(self, x: Text):
        return f'{self}{x}' > f'{x}{self}'

#n = int(input())
#numbers = input().split()
#big_number(numbers)

#numbers = [String(s) for s in input().split()]
#numbers.sort()
#print(''.join(numbers))