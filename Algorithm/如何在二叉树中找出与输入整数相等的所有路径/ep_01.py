# 定义二叉树
class BiTreeNode():
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

# 先序遍历查看是否等于整数(重点)
def findRoad(root,num,sums,v):
    sums += root.data
    v.append(root.data)
    mark = 0
    if root.lchild==None and root.rchild==None and num==sums:
        i = 0
        while i < len(v):
            # print(v[i])
            mark += 1
            i += 1

    if root.lchild != None:
        findRoad(root.lchild,num,sums,v)
    if root.rchild != None:
        findRoad(root.rchild,num,sums,v)

    sums -= v[-1]
    v.remove(v[-1])
    print(mark)



# 构造二叉树
def creatTree():
    root = BiTreeNode()
    node1 = BiTreeNode()
    node2 = BiTreeNode()
    node3 = BiTreeNode()
    node4 = BiTreeNode()
    root.data = 6
    node1.data = 3
    node2.data = -7
    node3.data = -1
    node4.data = 9
    root.lchild = node1
    root.rchild = node2
    node1.lchild = node3
    node1.rchild = node4
    node2.lchild=node2.rchild=node3.lchild=node3.rchild=node4.lchild=node4.rchild=None
    return root


if __name__ == '__main__':
    root1 = creatTree()
    s = []
    findRoad(root1, 8, 0, s)
