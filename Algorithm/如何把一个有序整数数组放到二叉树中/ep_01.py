
'''
思路：递归思想

取数组中间的数字作为根节点，将数组分成左右两部分，左右两部分递归处理
'''


class BiTNode():
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


def arraytotree(arr, start, end):
    root = None
    if end >= start:
        root = BiTNode()
        mid = int((start+end+1)/2)
        root.data = arr[mid]
        # 递归的处理左子树
        root.lchild = arraytotree(arr, start, mid-1)
        # 递归的处理右子树
        root.rchild = arraytotree(arr, mid+1, end)

    else:
        root = None
    return root


# 中序遍历的方式打印出二叉树节点的内容
def printTreeMidOrder(root):
    if root == None:
        return
    # 遍历root节点的左子树
    if root.lchild != None:
        printTreeMidOrder(root.lchild)
    # 遍历root节点
    print(root.data)
    # 遍历root节点的右子树
    if root.rchild != None:
        printTreeMidOrder(root.rchild)

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    print('数组：', end='')
    i = 0
    while i < len(arr):
        print(arr[i], end='')
        i += 1

    root = arraytotree(arr, 0, len(arr)-1)
    print('转化成树的中序遍历结果是：')
    printTreeMidOrder(root)
