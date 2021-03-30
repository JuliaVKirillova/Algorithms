""" Обход дерева в глубину """

class Node :
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        return str(self.value)


""" Обработка узла после рекурсии """

def dfs_post_order(node, path=[]) :
    if node.left:
        path = dfs_post_order(node.left, path)
    if node.right:
        path = dfs_post_order(node.right , path)
    path += [node]
    return path        


""" Обработка вершины до рекурсии """

def dfs_pre_order(node, path=[]) :
    path += [node]
    if node.left:
        path = dfs_pre_order(node.left, path)
    if node.right:
        path = dfs_pre_order(node.right, path)
    return path


""" Рекурсия для левой части, обработка узла, рекурсия для правой части """

def dfs_in_order(node, path=[]) :
    if node.left:
        path = dfs_pre_order(node.left, path)
    path += [node]    
    if node.right:
        path = dfs_pre_order(node.right, path)
    return path



""" Обход дерева в ширину  """

from collections import deque

def bfs(root, path=[]) :
    q = deque()
    q.append(root)
    while q:
        cur_node = q.popleft()
        path.append(cur_node)
        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return path    