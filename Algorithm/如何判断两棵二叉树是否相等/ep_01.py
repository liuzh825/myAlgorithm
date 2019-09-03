

'''

'''


class biTreeBiNode():
    # 定义二叉树
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


def structure():
    root = biTreeBiNode()
    node1 = biTreeBiNode()
    node2 = biTreeBiNode()
    node3 = biTreeBiNode()
    node4 = biTreeBiNode()
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


# 核心思想
def equal(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None and root2 != None:
        return False
    if root2 == None and root1 != None:
        return False
    if root1.data == root2.data:
        return equal(root1.lchild, root2.lchild) and equal(root1.rchild, root2.rchild)
    else:
        return False


if __name__ == '__main__':
    root1 = structure()
    root2 = structure()
    if equal(root1, root2):
        print('两棵二叉树相等')
    else:
        print('两棵二叉树不相等')

