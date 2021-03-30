""" Реализация дека """
class Deque:
    def __init__(self, limit=None):
        self.items = []
        self.limit = limit

    def push_back(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            return 'error'    

    def push_front(self, item):
        if len(self.items) < self.limit:
            self.items.insert(0, item)
        else:
            return 'error'     

    def pop_back(self):
        if len(self.items) == 0:
            return 'error'
        else:    
            return self.items.pop()

    def pop_front(self):
        if len(self.items) == 0:
            return 'error'
        else:
            return self.items.pop(0)

def work_with_deque():
    n, m = int(input()), int(input())
    deque = Deque(m)
    result = []
    for _ in range(n):
        s = input().split()
        if s[0] == 'pop_back':
            result.append(deque.pop_back())
        elif s[0] == 'pop_front':
            result.append(deque.pop_front())
        elif s[0] == 'push_back':
            x = deque.push_back(s[1])
            if x is not None:
                result.append(x)
        else:
            y = deque.push_front(s[1])
            if y is not None:
                result.append(y)  

    for r in result:
        print(r) 

#work_with_deque()