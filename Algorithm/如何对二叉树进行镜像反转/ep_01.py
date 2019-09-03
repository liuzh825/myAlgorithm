from collections import deque



# 定义二叉树
class BiTreeNode():
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

# 平铺二叉树 1-7
def arrToBiTree(arr, start, end):
    root = None
    if start <= end:
        root = BiTreeNode()
        mid = int((start+end+1)/2)
        root.data = arr[mid]
        root.lchild = arrToBiTree(arr, start, mid-1)
        root.rchild = arrToBiTree(arr, mid+1, end)
    else:
        root = None
    return root

# 层序遍历二叉树
def printBiTree(root):
    if root == None:
        return
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        p = queue.popleft()
        print(p.data, end=',')
        if p.lchild != None:
            queue.append(p.lchild)
        if p.rchild != None:
            queue.append(p.rchild)

# 反转二叉树
def reserveBiTree(root):
    if root == None:
        return
    reserveBiTree(root.lchild)
    reserveBiTree(root.rchild)
    tmp = root.lchild
    root.lchild = root.rchild
    root.rchild = tmp


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    root = arrToBiTree(arr,0,len(arr)-1)
    printBiTree(root)
    print('\n')
    reserveBiTree(root)
    printBiTree(root)