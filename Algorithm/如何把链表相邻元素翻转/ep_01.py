# coding=UTF-8

'''
两个单链表求和
1，2，3，4，5，6，7
2，1，4，3，6，5，7

思路

pre cur next  换位置
'''

class LNode():
    def __init__(self, value=None):
        self.value = value
        self.next = None

def Exchange(head):
    '''
    pre head
    cur 1
    next 3
    第一步 记录3
    第二步 head.next = 2
    第三步 2.next = 1
    第四步 1.next = 3
    :param head:
    :return:
    '''
    pre = head
    cur = head.next
    next = None

    while cur != None and cur.next != None:
        next = cur.next.next
        pre.next = cur.next
        cur.next.next = cur
        cur.next = next
        # 坑点：pre = cur not cur.next
        pre = cur
        cur = next

if __name__ == '__main__':
    i = 1
    print('原链表：')
    head = LNode()
    cur = head
    while i < 8:
        cur.next = LNode(i)
        print(cur.next.value)
        cur = cur.next
        i += 1

    print('交换之后：')
    Exchange(head)
    cur = head.next
    while cur != None:
        print(cur.value)
        cur = cur.next
