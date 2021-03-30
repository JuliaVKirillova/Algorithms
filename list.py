""" Вывести уникальные названия кружков """
def find_unique_courses():
    n = int(input())
    courses = [input() for i in range(n)]
    unique_courses = set(courses)
    for course in unique_courses:
        print(course)

#find_unique_courses()


""" Вывести транспонированную матрицу """
def turn_over_list():
    n, m = int(input()), int(input())
    matrix = []
    for _ in range(n):
        s = list(map(int, input().split()))
        matrix.append(s)
    
    new_matrix = [[0 for t in range(n)] for k in range(m)]

    for x in range(m):
        for y in range(n):
            new_matrix[x][y] = matrix[y][x]

    for a in new_matrix:
        print(*a) 

#turn_over_list()


""" Определить длину наибольшей подстроки, без повторяющихся символов """
def find_max_substring():
    s = input()
    sub_s = []
    for char in s:
        if char not in sub_s:
            sub_s.append(char)
    print(len(sub_s))  

#find_max_substring()


""" Вывести для заданной ячейки матрицы соседние элементы кроме дигональных """
def find_neigbours():
    n, m = int(input()), int(input())
    matrix = []
    neigbours = []
    for _ in range(n):
        s = list(map(int, input().split()))
        matrix.append(s)
    x, y = int(input()), int(input())

    def right(matrix, x , y, neigbours):
        neigbours.append(matrix[x][y + 1])
        return neigbours

    def left(matrix, x , y, neigbours):   
        neigbours.append(matrix[x][y - 1])
        return neigbours

    def up(matrix, x , y, neigbours):  
        neigbours.append(matrix[x - 1][y])
        return neigbours

    def down(matrix, x , y, neigbours): 
        neigbours.append(matrix[x + 1][y])
        return neigbours


    if x == 0 and y == 0:
        right(matrix, x, y, neigbours)
        down(matrix, x, y, neigbours)
    elif x == 0 and y == m - 1:
        left(matrix, x, y, neigbours)
        down(matrix, x, y, neigbours)
    elif x == 0 and y != 0 and y != m - 1:
        right(matrix, x, y, neigbours)
        left(matrix, x, y, neigbours)
        down(matrix, x, y, neigbours)

    elif x == n - 1 and y == 0:
        right(matrix, x, y, neigbours)
        up(matrix, x, y, neigbours)
    elif x != 0 and x != n - 1 and y == 0:
        right(matrix, x, y, neigbours)
        down(matrix, x, y, neigbours)
        up(matrix, x, y, neigbours)

    elif x == n - 1 and y == m - 1:
        up(matrix, x, y, neigbours)
        left(matrix, x, y, neigbours)
    elif x == 0 and x != n - 1 and y != m - 1:
        left(matrix, x, y, neigbours)
        right(matrix, x, y, neigbours)
        up(matrix, x, y, neigbours)

    elif x != 0 and x != n - 1 and y == m - 1:
        up(matrix, x, y, neigbours)
        left(matrix, x, y, neigbours)
        down(matrix, x, y, neigbours)                  
    
    else:
        up(matrix, x, y, neigbours)
        right(matrix, x, y, neigbours)
        down(matrix, x, y, neigbours) 
        left(matrix, x, y, neigbours)

    neigbours.sort()
    print(*neigbours)

#find_neigbours()        