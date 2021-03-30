""" Реализация очереди на основе массива """
class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if self.queue == []:
            return 'None'
        else:    
            return self.queue.pop(0)

    def peek(self):
        if self.queue == []:
            return 'None'
        else:
            return self.queue[0]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.queue == []

def work_with_queue():
    queue = MyQueue()
    n = int(input())
    result = []
    for _ in range(n):
        s = input().split()
        if s[0] == 'push':
            queue.push(int(s[1]))
        elif s[0] == 'pop':
            result.append(queue.pop())
        elif s[0] == 'peek':
            result.append(queue.peek())
        else:
            result.append(queue.size())
    
    for r in result:
        print(r)        

#work_with_queue()    
        

class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None for _ in range(max_size)]
        self.max_elem = max_size
        self.head = 0
        self.tail = 0
        self.size = 0


    def push(self, x):
        if self.size != self.max_elem:
            self.queue[self.tail] = x
            self.size += 1
            self.tail = (self.tail + 1) % self.max_elem
        else:
            return 'error'    

    def pop(self):
        if self.queue == []:
            return 'None'
        else:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_elem
            self.size -= 1
            return x

    def peek(self):
        return self.queue[self.head]


def work_with_sized_queue():
    n, m = int(input()), int(input())
    queue = MyQueueSized(m)
    result = []
    for _ in range(n):
        s = input().split()
        if s[0] == 'push':
            add = queue.push(int(s[1]))
            if add == 'error':
                result.append(add)
        elif s[0] == 'pop':
            result.append(queue.pop())
        elif s[0] == 'peek':
            result.append(queue.peek())
        else:
            result.append(queue.size)
    
    for r in result:
        print(r)                

#work_with_sized_queue()

""" Реализация очереди на базе связного списка """
class NodeForQueue:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
class QueueLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    
    def put(self, item):
        new_node = NodeForQueue(item)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1

    def get(self):
        if self.length == 0:
            return 'error'
        else:
            item = self.head
            self.head = self.head.next
            self.length -= 1
            return item.value

    def size(self):
        return self.length


def work_with_linked_list_queue():
    n = int(input())
    queue = QueueLinkedList()
    result = []
    for _ in range(n):
        s = input().split()
        if s[0] == 'put':
            queue.put(s[1])
        elif s[0] == 'get':
            result.append(queue.get())
        else:
            result.append(queue.size())
    
    for r in result:
        print(r)     

#work_with_linked_list_queue()