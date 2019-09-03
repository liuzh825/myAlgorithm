'''
1,2,3,4,5,6,7
'''
from collections import deque


class BiTreeNode():
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


def arrToBiTree(arr, start, end):
    if len(arr) <= 0:
        return
    root = None
    if end >= start:
        root = BiTreeNode()
        mid = (start+end+1)//2
        root.data = arr[mid]
        root.lchild = arrToBiTree(arr, start, mid-1)
        root.rchild = arrToBiTree(arr, mid+1, end)
    else:
        return None
    return root

def upToDown(root):
    if root == None:
        return
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        print(node.data)
        if node.lchild != None:
            queue.append(node.lchild)
        if node.rchild != None:
            queue.append(node.rchild)




if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    root = arrToBiTree(arr, 0, len(arr)-1)
    upToDown(root)

