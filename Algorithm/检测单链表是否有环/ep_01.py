# coding=utf-8

'''
检测单链表是够又环

1，2，3，4，5，6，7，3

检测结果有环
环的入口点是3

思路
1 判断是否有环
快慢指针遍历法
慢指针没前进一步  快指针前进两步  每移动一步进行比较  如果相等就有环

2 找出环的入口点
假设有环  慢指针走了s步 则快指针走了2s步  同时如果环的长度为r,快指针在环上转了n圈 有2s=s + nr 所以s = nr

链表头和相遇点分别设一个指针，每次各走一步，两个指针必定相遇，且第一次相遇的点就是环入口点  证明
'''

class LNode():
    def __init__(self, value=None):
        self.value = value
        self.next = None

def Exchange(head):
    '''
    判断是否有环
    思路
    慢指针和快指针相遇 记住相遇的点
    '''
    slowcur = head
    fastcur = head
    while slowcur.next != None:
        slowcur = slowcur.next
        fastcur = fastcur.next.next
        if slowcur == fastcur:
            return slowcur
    return False

def Find(head, slowcur):
    '''
    找出环入口
    证明参考： https://www.jianshu.com/p/87d1f66f3cdf
    :param head:
    :param slowcur:
    :return:
    '''
    cur1 = head
    cur2 = slowcur

    while cur1 != None:
        if cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next

        else:
            return cur1


if __name__ == '__main__':
    i = 1
    head = LNode()
    cur = head
    while i < 7:
        cur.next = LNode(i)
        cur = cur.next
        i += 1

    print('生成带环链表')
    cur1 = head.next
    while cur1 != None:
        if cur1.value == 3:
            inputcur = cur1
            break
        cur1 = cur1.next
    cur.next = cur1

    # cur = head.next
    # while cur != None:
    #     print(cur.value)
    #     cur = cur.next


    print('判断是否有环：')
    slowcur = Exchange(head)
    if slowcur == False:
        print('链表没有环')
    else:
        print('链表有环')
        cur1 = Find(head, slowcur)
        print('环的入口是：', cur1.value)



