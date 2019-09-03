# coding=UTF-8

'''
两个单链表求和
3，4，5，6，7，8
9，8，7，6，5

2,3,3,3,3,9
'''


class LNode():
    def __init__(self, value=None):
        self.value = value
        self.next = None

def addResult(h1, h2):
    # 接受参数 h1, h2
    cur1 = h1.next
    cur2 = h2.next
    c = 0 # 进位
    sumh = LNode
    cur = sumh
    tmp = None
    while cur1 != None and cur2 != None:
        sum = cur1.value + cur2.value
        value = sum % 10
        tmp = LNode(value + c)
        c = sum // 10
        cur.next = tmp
        cur = cur.next
        cur1 = cur1.next
        cur2 = cur2.next

    # h2比较长
    if cur1 == None:
        while cur2 != None:
            sum = cur2.value
            value = sum % 10
            tmp = LNode(value + c)
            c = sum // 10
            cur.next = tmp
            cur = cur.next
            cur2 = cur.next

    # h1比较长
    if cur2 == None:
        while cur1 != None:
            sum = cur1.value
            value = sum % 10
            tmp = LNode(value + c)
            c = sum // 10
            cur.next = tmp
            cur = cur.next
            cur1 = cur.next

    return sumh


if __name__ == '__main__':
    # 构造第一个单链表
    i = 1
    h1 = LNode()
    cur = h1
    tmp = None

    while i < 7:
        tmp = LNode(i+2)
        cur.next = tmp
        cur = cur.next
        i += 1

    print('第一个单链表：')
    cur = h1.next
    while cur != None:
        print(cur.value)
        cur = cur.next


    # 构造第二个单链表
    i = 9
    h2 = LNode()
    cur = h2
    tmp = None
    while i > 4:
        tmp = LNode(i)
        cur.next = tmp
        cur = cur.next
        i = i - 1


    print('第二个单链表：')
    cur = h2.next
    while cur != None:
        print(cur.value)
        cur = cur.next


    # 求和
    sumh = addResult(h1, h2)
    cur = sumh.next
    print('求和之后的链表')
    while cur != None:
        print(cur.value)
        cur = cur.next