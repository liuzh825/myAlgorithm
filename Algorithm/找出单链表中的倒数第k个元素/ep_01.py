# coding=UTF-8

'''
找出单链表中倒数第k个元素

1，2，3，4，5，6，7

倒数第三个元素 5
'''

class LNode():
    def __init__(self, value=None):
        self.value = value
        self.next = None


def forEach(head, k):
    i = 1
    slowcur = head.next
    fastcur = head.next
    while i <= k:
        fastcur = fastcur.next
        i += 1


    while fastcur != None:
        slowcur = slowcur.next
        fastcur = fastcur.next

    return slowcur



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

    print('倒数第三个元素是：')
    slowcur = forEach(head, 3)
    print(slowcur.value)