


class BiTreeNode():
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

def creatBuptree(root):
    if root == None:
        return None
    duptree = BiTreeNode()
    duptree.data = root.data
    duptree.lchild = creatBuptree(root.lchild)
    duptree.rchild = creatBuptree(root.rchild)

    return duptree


def printTreeMidOrder(root):
    if root == None:
        return
    if root.lchild != None:
        printTreeMidOrder(root.lchild)
    print(root.data)
    if root.rchild != None:
        printTreeMidOrder(root.rchild)


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
    printTreeMidOrder(root1)
    print("=" * 50)

    root2 = creatBuptree(root1)
    printTreeMidOrder(root2)
