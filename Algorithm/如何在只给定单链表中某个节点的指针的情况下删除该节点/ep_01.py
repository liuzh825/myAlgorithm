# coding=utf-8

'''
如何在只给定单链表中某个节点的指针的情况下删除该节点

思路：删除链表中一个节点p，将p的下一个节点的值赋给p然后，p的下一个节点等于p的下一个节点的下一个节点

输入 1，2，3，4，5，6，7
输出 1，2，3，4，6，7
'''


class LNode():
    def __init__(self, value=None):
        self.value = value
        self.next = None


def deleteP(head, p):
    if head == None or head.next == None:
        return
    if p.next == None:
        return
    next = p.next
    p.value = next.value
    p.next = next.next
    return head


if __name__ == '__main__':
    i = 1
    head = LNode()
    cur = head
    p = None
    while i < 8:
        cur.next = LNode(i)
        print(cur.next.value)
        cur = cur.next
        if i == 5:
            p = cur
            print('p节点的值：', p.value)
        i += 1

    print('删除p节点之后：')
    Nhead = deleteP(head, p)
    cur = head.next
    while cur != None:
        print(cur.value)
        cur = cur.next