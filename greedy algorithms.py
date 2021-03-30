""" Составить оптимальное расписание уроков в классе ///
Размещение максимального количества непересекающихся отрезков на прямой """

def schedule():
    n = int(input())
    lessons, result = [], []
    for _ in range(n):
        s = input().split()
        lessons.append(s)     

    lessons.sort(key = lambda x: (float(x[1]), float(x[0])))

    for l in range(len(lessons)):
        if l == 0:
            result.append(lessons[l])
        else:
            if float(result[-1][1]) <= float(lessons[l][0]):
                result.append(lessons[l])
                    
    print(len(result))
    for r in result:
        print(*r)

#schedule()


""" Вывести число, равное максимально возможной прибыли """

def get_max_profit():
    n = int(input())
    prices = list(map(int, input().split()))
    profit = 0

    if len(prices) < 2:
        raise IndexError(
            'Получение прибыли требует как минимум двух цен в массиве'
        )

    for p in range(len(prices) - 1):
        if prices[p] < prices[p + 1]:
            profit += prices[p + 1] - prices[p]

    return profit

#print(get_max_profit())


""" Проверить является ли строка подпоследовательностью другой строки """

def is_substring():
    s, t = input(), input()
    substring = ''
    if s == '':
        return True
    else:    
        for char in t:
            if char in s:
                substring += char
 
    if substring == s:
        return True
    else:
        return False 

#print(is_substring())


""" Задача о ценном рюкзаке, 
взять наиболее ценный предмет, который поместится в рюкзак """

def valued_knapsack():
    c, n = int(input()), int(input())
    costs_weights = []
    knapsack = ''
    item_order = {}
    for _ in range(n):
        costs_weights.append(list(map(int, input().split())))

    for i in range(len(costs_weights)):
        item_order[i] = costs_weights[i]
      
    costs_weights.sort(key=lambda x: x[0], reverse=True)

    for item in costs_weights:
        if item[1] <= c:
            c -= item[1]
            for k, v in item_order.items():
                if item == v:
                    knapsack += str(k)

    for symb in knapsack:
        print(symb, end=' ')         

#valued_knapsack()


""" Определить количество довольных детей.
У ребенка есть минимальный размер печенья, которое он возьмет.
Печенья могут быть разного размера. """

def give_cookies():
    n = int(input())
    children = list(map(int, input().split()))
    m = int(input())
    cookies = list(map(int, input().split()))
    happy = 0

    children.sort(reverse=True)
    cookies.sort(reverse=True)

    for i in children:
        for j in cookies:
            if i <= j:
                happy += 1
                break

    return happy    

#print(give_cookies())


""" Вывести количество столбцов, которые необходимо удалить, 
чтобы строки были упорядочены по неубыванию сверху вниз """

def string_matrix():
    n, m = int(input()), int(input())
    strings = []
    index = 0
    for _ in range(n):
        strings.append(list(input()))

    for i in range(n - 1):
        for j in range(m):
            if strings[i][j] <= strings[i + 1][j]:
                continue
            else:
                index += 1

    return index

#print(string_matrix())


""" Вывести на печать по спирали элементы матрицы """

def number_matrix():
    n, m = int(input()), int(input())
    numbers = []
    for _ in range(n):
        numbers.append(list(map(int, input().split())))
    
    for i in range(0, 1):                # up
        for j in range(m):
            print(numbers[i][j])

    for i in range(1, n):                # right
        for j in range(m - 1, m):
            print(numbers[i][j])

    for i in range(n - 1, n):            # down
        for j in range(m - 2, -1, -1):
            print(numbers[i][j])

    for i in range(n - 2, 0, - 1):       # left
        for j in range(0, 1):
            print(numbers[i][j])

    for i in range(1, n - 1):            # inner  
        for j in range(1, m - 1):
            print(numbers[i][j])                     

#number_matrix()        


""" Вывести длину наибольшего возрастающего подмассива """

def growing_list():
    n = int(input())
    numbers = list(map(int, input().split()))
    length, max_length = 1, 1
    
    for num in range(n - 1):
        if numbers[num] < numbers[num + 1]:
            length += 1
        else:
            max_length = max(max_length, length)
            length = 1

    print(max_length) 

#growing_list()


""" Вывести длину последнего слова в строке """

def get_last_length():
    # s = input().split()
    # print(len(s[-1]))

    s = input()
    lenght = 0
    for letter in s:
        if letter.isalpha() and letter != s[-1]:
            lenght += 1
        elif letter == ' ':
            lenght = 0
        elif letter.isalpha() and letter == s[-1]:
            lenght += 1
            return lenght

#print(get_last_length())


""" Определить какое наибольшее количество домов можно купить на k денег """

def buy_houses():
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))
    prices.sort()

    count_houses = 0
    for p in prices:
        if p <= k:
            count_houses += 1
            k -= p
    
    print(count_houses)

#buy_houses()



""" Опрелелить, можно ли с нижней ступеньки добраться до верхней,
дан массив чисел, обозначающих на какое количество ступенек вверх 
можно допрыгнуть с этой ступеньки """

def stairs():
    n = int(input())
    steps = list(map(int, input().split()))
    if steps[0] == 0 and n != 1:
        return False
    else:
        for s in range(n - 1):
            if steps[s] == 0 and steps[s - 1] == 1:
                return False
    return True    

#print(stairs())                            
                    


""" Задача о покрытии множества 
Требуется определить, на каких радиостанциях передача должна транслироваться.
Есть список станций, каждая из которых транслируется в определённых населённых пунктах
"""

def radiostations():
    states_needed = set (["mt", "wa", "or", "tg", "nv", "ut", "lp", "az"]) 

    stations = {}
    stations["kone"] = set (["tg", "nv", "ut"])
    stations["ktwo"] = set (["wa", "tg", "mt"])
    stations["kthree"] = set (["or", "nv", "lp"])
    stations["kfour"] = set (["nv", "ut"])
    stations["kfive"] = set (["lp", "az"]) 

    final_stations = set() 

    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len (states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

#radiostations()     


""" Вывести максимальное количество фотографий, которые можно хранить в датацентрах.
Фотографии хранятся в двух экземплярах.
1 экземпляр в одном датацентре, другой в другом датацентре. """

def get_copy(n, centres):
    counter = 0
    while len(centres) != 1:
        centres = sorted(centres, reverse=True)
        if centres[-1] == 0:
            centres = centres[:-1] 
            continue   
        centres[-1] -= 1
        centres[0] -= 1
        counter += 1

    return counter

#n = int(input())
#centres = list(map(int, input().split()))
#print(get_copy(n, centres))