# -*- coding: utf-8 -*-


'''
判断两个单链表（无环）是否交叉

思路
判断两个链表是否相交，并找出相交点，分别遍历两个单链表，如果尾节点相同即相交，并记录两个链表的长度为n1,n2(假设呢n2>n1)
长的链表先走(n2-n1步)，然后每走一步进行比较。第一次相同的点就是相交点
'''

class LNode():
    def __init__(self, value=None):
        self.value = value
        self.next = None


def intersection(h1, h2):
    if h1 == None or h2 == None:
        return
    if h1.next == None or h2.next == None:
        return
    i1 = 1
    cur1 = h1.next
    pre1 = None
    while cur1 != None:
        pre1 = cur1
        cur1 = cur1.next
        i1 += 1
    print('链表1的总长度是：', i1)
    print('链表1的最后一个节点的值是：', pre1.value)

    i2 = 1
    cur2 = h2.next
    pre2 = None
    while cur2 != None:
        pre2 = cur2
        cur2 = cur2.next
        i2 += 1
    print('链表2的总长度是：', i2)
    print('链表2的最后一个节点的值是：', pre2.value)

    if pre1.value == pre2.value:
        print('两个链表交叉')
        if i1 > i2:
            distince = i1 - i2
            cur1 = h1.next
            cur2 = h2.next
            i = 1
            while i <= distince:
                cur1 = cur1.next
                i += 1
            while cur1 != None and cur2 != None:
                if cur1.value == cur2.value:
                    print('链表的交叉点是', cur1.value)
                    return
                cur1 = cur1.next
                cur2 = cur2.next
        else:
            distance = i2 - i1
            cur1 = h1.next
            cur2 = h2.next
            i = 1
            while i <= distance:
                cur2 = cur2.next
                i += 1
            while cur1 != None and cur2 != None:
                if cur1.value == cur2.value:
                    print('链表的交叉点是', cur1.value)
                    return
                cur1 = cur1.next
                cur2 = cur2.next
        print('两个链表的总长度差是：', distance)


    else:
        print('两个链表没有交叉点')




if __name__ == '__main__':
    print('构造第一个链表：')
    i = 1
    h1 = LNode()
    cur1 = h1
    while i < 9:
        if i == 4:
            i += 1
            continue
        cur1.next = LNode(i)
        print(cur1.next.value)
        cur1 = cur1.next
        i += 1
    print('构造第二个链表：')
    x = 3
    h2 = LNode()
    cur2 = h2
    while x < 9:
        cur2.next = LNode(x)
        print(cur2.next.value)
        cur2 = cur2.next
        x += 1

    intersection(h2, h1)

