""" Вывести элементы связного списка """
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item
 
n4 = Node('fourth')
n3 = Node('third', n4)
n2 = Node('second', n3)
n1 = Node('first', n2) 

def print_lst(node):
    while node.next_item:
        print(node.value)
        node = node.next_item

#print_lst(n1)


""" Удалить элемент из связного списка """
def delete_elem(node, idx):
    head = node
    if idx == 0:
        head = node.next_item
    else:
        node = node.next_item.next_item
    print(head.value)        
    
#delete_elem(n1, 0)


""" Найти элемент в связном списке """
def find_elem(node, elem):
    idx = 0
    while node:
        if node.value == elem:
            print(idx)
            break
        else:
            idx += 1
            node = node.next_item


#find_elem(n1, 'second')


class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


k1 = DoubleConnectedNode('one') 
k2 = DoubleConnectedNode('two', prev=k1)
k3 = DoubleConnectedNode('three', prev=k2)
k4 = DoubleConnectedNode('four', prev=k3)
k1.next = k2
k2.next = k3
k3.next = k4


""" Вывести элементы двусвязного списка в обратном порядке """
def reverse_node(node):
    while node.next:
        node = node.next
    
    while node:
        print(node.value)
        node = node.prev     

#reverse_node(k1)       



""" Определить, есть ли цикл в связном списке, на вход подается голова списка """
""" floyd's tortoise and the hare algorithm """

class NodeCicled:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


def has_cycle(head):
    if head is None:
        return False
    
    else:    
        p1, p2 = head, head  
        while p2 is not None:
            if p2.next is None:
                return False
            else:
                p2 = p2.next.next
                p1 = p1.next
                if p2 == p1:
                    return True
        
        return False

""" n7 = NodeCicled('Воскресенье', None)
n6 = NodeCicled('Суббота', n7)
n5 = NodeCicled('Пятница', n6)
n4 = NodeCicled('Четверг', n5)
n3 = NodeCicled('Среда', n4)
n2 = NodeCicled('Вторник', n3)
n1 = NodeCicled('Понедельник', n2)
#n7.next = n1 
print(has_cycle(n1)) """