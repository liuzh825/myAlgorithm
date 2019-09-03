'''
使用链表实现队列：

判断队列是否为空
返回队列的大小
返回队列的首元素
返回队列的尾元素
删除队列头元素
新元素加入队列尾

队列规则 先进先出
'''
class LNode():
    def __init__(self, value=None):
        self.value = value
        self.next = None


class MyQueue():
    def __init__(self, head=None):
        self.head = head

    # 判断队列是否为空
    def isEmpty(self):
        return self.head == None or self.head.next == None

    # 返回队列的大小
    def size(self):
        if self.isEmpty():
            return 0
        else:
            i = 0
            cur = self.head.next
            while cur != None:
                cur = cur.next
                i += 1
            return i

    # 返回队列的首元素
    def getFroent(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        return cur.value

    # 返回队列的尾元素
    def getBack(self):
        cur = self.head.next
        return cur.value

    # 删除队列头元素
    def delFroent(self):
        pre = self.head
        cur = self.head.next
        while cur.next != None:
            pre = cur
            cur = cur.next
        pre.next = None


    # 新元素加入队列尾
    def addrear(self, e):
        e = LNode(e)
        if self.isEmpty():
            self.head = LNode()
            self.head.next = e
        else:
            cur = self.head.next
            self.head.next = e
            e.next = cur


if __name__ == '__main__':
    head = LNode()
    head.next = LNode(1)
    head.next.next = LNode(2)
    mq = MyQueue(head)
    if mq.isEmpty():
        print('队列为空')
    else:
        print('队列不为空')
    size = mq.size()
    print('队列的大小为：', size)
    firstEle = mq.getFroent()
    print('队列的首元素为：', firstEle)

    endEle = mq.getBack()
    print('队列的尾元素为：', endEle)

    print('--' * 20)
    print('删除队列头元素')

    mq.delFroent()
    size = mq.size()
    print('队列的大小为：', size)
    firstEle = mq.getFroent()
    print('队列的首元素为：', firstEle)

    print('--' * 20)
    print('新元素加入队列尾')

    mq.addrear(4)
    size = mq.size()
    print('队列的大小为：', size)
    endEle = mq.getBack()
    print('队列的尾元素为：', endEle)




