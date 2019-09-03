


# 定于二叉树
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

# 找出最大节点
def maxNode(root):
    if root == None:
        return root
    while root.rchild != None:
        root = root.rchild
    return root
# 找出最小节点
def minNode(root):
    if root == None:
        return root
    while root.lchild != None:
        root = root.lchild
    return root

# 找出目标值
def getTarget(root):
    maxnode = maxNode(root)
    minnode = minNode(root)
    mid = int((maxnode.data+minnode.data)/2)
    result = None
    while root != None:
        if root.data <= mid:
            root = root.rchild
        else:
            result = root
            root = root.lchild

    return result

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    root = arrToBiTree(arr, 0, len(arr)-1)
    print(getTarget(root).data)