
""" Реализация стека на Python, поддерживает операцию определения максимума среди всех элементов в стеке """
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items == []:
            return 'error'
        else:
            self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items) 


class StackMax(Stack):
    def get_max(self):
        if self.items == []:
            return 'None'
        else:
            return max(self.items)



class StackMaxEffective(Stack):
    def __init__(self):
        self.items = []
        self.max_item = []
    
    def push(self, item):
        self.items.append(item)
        if self.max_item == []:
            self.max_item.append(item)
        else:
            if self.max_item[-1] <= item:
                self.max_item.append(item)
            else:
                self.max_item.append(self.max_item[-1])     

    def pop(self):
        if self.items == []:
            return 'error'
        else:
            self.items.pop()
            self.max_item.pop()

    def get_max(self):
        if self.items == []:
            return 'None'
        else:
            return self.max_item[-1]         


def work_with_stack():
    stack = StackMaxEffective()
    n = int(input())
    result = []
    for _ in range(n):
        s = input().split()
        if s[0] == 'get_max':
            result.append(stack.get_max())
        elif s[0] == 'pop':
            x = stack.pop()
            if x:
                result.append(x)
        else:
            stack.push(int(s[1]))
    for r in result:
        print(r)        

#work_with_stack()



""" Уникальный стек """
class StackSet():
    def __init__(self):
        self.items = []
        self.unique_items = set()

    def push(self, item):
        self.unique_items.add(item)
        self.items.append(item)

    def pop(self):
        if self.unique_items == set():
            return 'error'
        else:
            x = self.items[-1]
            self.items.pop()
            self.unique_items.discard(x)

    def peek(self):
        if self.items == set():
            return 'error'
        else:
            return self.items[-1]

    def size(self):
        return len(self.unique_items)        


def work_with_stackset():
    stackset = StackSet()
    n = int(input())
    result = []
    for _ in range(n):
        s = input().split()
        if s[0] == 'pop':
            stackset.pop()
        elif s[0] == 'size':
            result.append(stackset.size())
        elif s[0] == 'peek':
            result.append(stackset.peek())
        else:
            stackset.push(int(s[1]))

    for r in result:
        print(r)        

#work_with_stackset()  




""" Реализация обратной польской нотации (записи), используется для парсинга арифметических операций """
def calculator(input_string):
    stack = []
    functions = ['+', '-', '*', '/']
    for char in input_string:
        if stack:
            if char.isdigit():
                stack.append(char)
            elif char in functions:
                function = char
                second = int(stack.pop())
                first = int(stack.pop())
                if function == '+':
                    tmp = first + second
                elif function == '-':
                    tmp = first - second
                elif function == '*':
                    tmp = first * second
                else:
                    tmp = first // second
                
                stack.append(tmp)
        elif char.isdigit():
            stack.append(char)
    return stack

#print(*calculator("7 2 + 4 * 2 +"))         