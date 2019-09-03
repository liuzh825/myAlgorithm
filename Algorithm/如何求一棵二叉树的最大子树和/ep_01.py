

'''

'''


class sumMaxBiTree():
    # 定义二叉树
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

class Test():
    # 定义初始最大值
    def __init__(self):
        self.maxSum = -9999999999
    # 构造一个二叉树  分别是  6.lchild=3 6.rchild=-7 3.lchild=-1 3.rchild=9
    def structure(self):
        root = sumMaxBiTree()
        node1 = sumMaxBiTree()
        node2 = sumMaxBiTree()
        node3 = sumMaxBiTree()
        node4 = sumMaxBiTree()
        root.data = 6
        node1.data = 3
        node2.data = -1
        node3.data = 9
        node4.data = -7
        root.lchild = node1
        root.rchild = node4
        node1.lchild = node2
        node1.rchild = node3
        node2.lchild = None
        node2.rchild = None
        node3.lchild = None
        node3.rchild = None
        node4.lchild = None
        node4.rchild = None
        return root

    # 递归处理每个节点 如果sum大于maxSum 更新maxSum
    def maxSumFunc(self, root, maxRoot):
        if root == None:
            return 0
        lsum = self.maxSumFunc(root.lchild, maxRoot)
        rsum = self.maxSumFunc(root.rchild, maxRoot)
        sum = lsum + rsum + root.data
        if sum > self.maxSum:
            self.maxSum = sum
            maxRoot.data = root.data
        return sum


if __name__ == '__main__':
    test = Test()
    root = test.structure()
    maxRoot = sumMaxBiTree()
    test.maxSumFunc(root, maxRoot)
    print(maxRoot.data)
    print(test.maxSum)



