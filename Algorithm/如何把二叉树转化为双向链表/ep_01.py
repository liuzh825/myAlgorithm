


class BiTreeNode():
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None


class One():
    def __init__(self):
        self.head = None
        self.end = None

    # 将有序数组转化为二叉树
    def funcOne(self, arr, start, end):
        root = None
        if end >= start:
            root = BiTreeNode()
            mid = int((start+end+1)/2)
            root.data = arr[mid]
            root.lchild = self.funcOne(arr, start, mid-1)
            root.rchild = self.funcOne(arr, mid+1, end)
        else:
            return None
        return root
    # 将二叉树转化为双向链表
    def funcTwo(self, root):
        if root == None:
            return
        self.funcTwo(root.lchild)
        root.lchild = self.end
        if self.end == None:
            self.head = root
        else:
            self.end.rchild = root
        self.end = root
        self.funcTwo(root.rchild)


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    one = One()
    root = one.funcOne(arr, 0, len(arr)-1)
    one.funcTwo(root)
    print("转换后双向链表的正向遍历：")
    cur = one.head
    while cur != None:
        print(cur.data)
        cur = cur.rchild
    print("转换后双向链表的反向遍历：")
    cur = one.end
    while cur != None:
        print(cur.data)
        cur = cur.lchild
