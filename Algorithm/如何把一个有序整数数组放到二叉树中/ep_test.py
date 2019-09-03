'''
1,2,3,4,5,6,7,8,9,10
'''


# 定义二叉树
class BiTNode():
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


# 递归的放数字到二叉树中，每次折中
def deal(arr, start, end):
    bit = None
    if end >= start:
        mid = int((end + start + 1) / 2)
        bit = BiTNode()
        bit.data = arr[mid]
        bit.lchild = [arr, start, mid - 1]
        bit.rchild = [arr, mid + 1, end]
    else:
        bit = None
    return bit


# 中序遍历打印二叉树
def printBiT(bit):
    if bit == None:
        return
    if bit.lchild != None:
        printBiT(bit.lchild)
    print(bit.data)
    if bit.rchild != None:
        printBiT(bit.rchild)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bit = deal(arr, 0, len(arr) - 1)
    printBiT(bit)
