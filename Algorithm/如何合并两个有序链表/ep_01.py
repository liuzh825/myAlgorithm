# coding=utf-8

'''
两个有序链表
1，3，5
2，4，6
合并
1，2，3，4，5，6

思路
比较两个链表的第一个节点 确定合并后的链表的第一个节点
遍历两个链表，每次放最小的进去
'''

class LNode():
    def __init__(self, value=None):
        self.value = value
        self.next = None

def Merge(h1, h2):
    if h1.next == None or h2.next == None:
        return
    cur1 = h1
    cur2 = h2
    if cur1.next.value <= cur2.next.value:
        head = h1
        cur = cur1
        pre = cur.next
        cur = pre.next
        cur2 = cur2.next
        while cur2 != None and cur != None:
            if cur2.value <= cur.value:
                pre.next = cur2
                pre = cur2
                cur2 = cur2.next
            else:
                pre.next = cur
                pre = cur
                cur = cur.next
        if cur2 == None:
            pre.next = cur
        else:
            pre.next = cur2

    else:
        head = h2
        cur = cur2
        pre = cur.next
        cur = pre.next
        cur1 = cur1.next
        while cur1 != None and cur != None:
            if cur1.value <= cur.value:
                pre.next = cur1
                pre = cur1
                cur1 = cur1.next
            else:
                pre.next = cur
                pre = cur
                cur = cur.next
        if cur1 == None:
            pre.next = cur
        else:
            pre.next = cur1
    # 坑点
    return head



if __name__ == '__main__':
    x = 1
    y = 2
    h1 = LNode()
    cur1 = h1
    cur1.next = LNode(x)
    cur1 = cur1.next
    while x < 5:
        cur1.next = LNode(x + 2)
        cur1 = cur1.next
        x += 2

    h2 = LNode()
    cur2 = h2
    cur2.next = LNode(y)
    cur2 = cur2.next
    while y < 6:
        cur2.next = LNode(y + 2)
        cur2 = cur2.next
        y += 2

    print('第一个链表：')
    cur1 = h1.next
    while cur1 != None:
        print(cur1.value)
        cur1 = cur1.next

    print('第二个链表：')
    cur2 = h2.next
    while cur2 != None:
        print(cur2.value)
        cur2 = cur2.next


    print('合并之后的链表：')
    mergeL = Merge(h2, h1)
    cur = mergeL.next
    while cur != None:
        print(cur.value)
        cur = cur.next




