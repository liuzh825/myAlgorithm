# coding=UTF-8

'''
单链表向右旋转k个位置

给定单链表： 1，2，3，4，5，6，7  k=3 旋转后的单链表是 5，6，7，1，2，3，4

'''

class LNode():
    def __init__(self, value=None):
        self.value = value
        self.next = None


def Rotating(head, k):
    '''
    思路
    原始链表    1，2，3，4，5，6，7
    处理后的结果 5，6，7，1，2，3，4
    slowcur 指向 4
    fastcur 指向 7
    slowcur处断开成两个单链表  1，2，3，4   5，6，7
    原链表的尾节点指向第一个节点1
    链表的头结点指向倒数第三个元素5
    '''
    i = 1
    slowcur = head.next
    fastcur = head.next
    while i <=  k + 1:
        fastcur = fastcur.next
        i += 1

    fasthead = fastcur
    fastpre = None
    while fastcur != None:
        fastpre = fastcur
        slowcur = slowcur.next
        fastcur = fastcur.next

    # 截断
    slowcur.next = None
    fastpre.next = head.next
    head.next = fasthead

    return head



if __name__ == '__main__':
    i = 1
    print('原始链表：')
    head = LNode()
    cur = head
    while i < 8:
        cur.next = LNode(i)
        cur = cur.next
        i += 1
        print(cur.value)

    print('单链表右旋转三个位置后的结果：')
    headR = Rotating(head, 3)
    cur = headR
    while cur.next != None:
        print(cur.next.value)
        cur = cur.next