'''
使用链表实现栈

具体方法
是否为空  栈的大小  栈顶元素  弹栈  压栈

后进先出
'''

class LNode():
    def __init__(self, value=None):
        self.value = value
        self.next = None



class MyStack():
    def __init__(self, head=None):
        self.head = head

    # 是否为空
    def isEmpty(self):
        return self.head == None or self.head.next == None

    # 栈的大小
    def Size(self):
        if self.isEmpty():
            print('栈为空')
            return
        cur = self.head.next
        i = 0
        while cur != None:
            cur = cur.next
            i += 1
        return i

    # 栈顶元素
    def Top(self):
        return self.head.next.value

    # 弹栈
    def pop(self):
        cur = self.head.next
        self.head.next = cur.next

    # 压栈
    def push(self, v):
        v = LNode(v)
        next = self.head.next
        self.head.next = v
        v.next = next


if __name__ == '__main__':
    head = LNode()
    head.next = LNode(1)
    head.next.next = LNode(2)
    ms = MyStack(head)
    if ms.isEmpty():
        print('栈为空')
    else:
        print('栈不为空')
    size = ms.Size()
    print('栈的大小为：', size)
    topEle = ms.Top()
    print('栈顶元素', topEle)
    ms.pop()
    topEle = ms.Top()
    print('栈顶元素', topEle)
    size = ms.Size()
    print('栈的大小为：', size)
    ms.push(3)
    topEle = ms.Top()
    print('栈顶元素', topEle)
    size = ms.Size()
    print('栈的大小为：', size)