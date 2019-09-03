# coding=UTF-8
# 递归法

import random


class LNode(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None

"""
题目描述：
1,3,1,5,5,7
1,3,5,7
方法：递归法2
"""
def RemoveDup(head):
    if head.next is None:
        return head

    pre=head
    cur=head.next
    head.next=RemoveDup(head.next)
    # 注意是head.next 因为这里是去掉与head相同的值，但是head还是留下来的
    while cur is not None:
        if cur.value == head.value:
            pre.next=cur.next
            cur=cur.next

        else:
            #遍历下一个节点
            cur=cur.next
            pre=pre.next
    return head

if __name__ == '__main__':
    i = 1
    head = LNode()
    cur = head
    tmp = None

    while i < 7:

        if i % 2 == 0:
            tmp = LNode(i + 1)
            cur.next = tmp
            cur = cur.next
            i += 1

        elif i % 3 == 0:
            tmp = LNode(i - 2)
            cur.next = tmp
            cur = cur.next
            i += 1
        else:
            tmp = LNode(i)
            cur.next = tmp
            cur = cur.next
            i += 1

    print('去重之前: ')

    cur = head.next
    while cur != None:
        print(cur.value)
        cur = cur.next


    print('去重之后: ')
    RemoveDup(head)
    cur = head.next
    while cur != None:
        print(cur.value)
        cur = cur.next