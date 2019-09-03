# coding=UTF-8

'''
单链表重新排序
example：1，2，3，4，5，6，7
result:  1,7,2,6,3,5,4
'''


class LNode():
    def __init__(self, value=None):
        self.value = value
        self.next = None


def findMiddleNode(head):
    cur = head.next

    fast = head.next
    slow = head.next

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    return slow


def backReverce(mid):
    '''坑点 需要next记录下一个位置'''
    pre = mid
    cur = mid.next
    next = cur.next
    pre.next = None

    while cur != None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    return pre


def merge(head, backhead):
    '''
    1,2,3
    7,6,5,4

    result 1,7,2,6,3,5,4
    :param head:
    :param backhead:
    :return:
    '''
    forecur = head.next
    backcur = backhead

    while forecur != None and backcur != None:
        forenext = forecur.next
        forecur.next = backcur
        backnext = backcur.next
        backcur.next = forenext

        forecur = forenext
        backcur = backnext

    return head


if __name__ == '__main__':
    # 构造1，2，3，4，5，6，7单链表
    i = 1
    head = LNode()
    cur = head
    while i < 8:
        cur.next = LNode(i)
        print(cur.next.value)
        cur = cur.next
        i += 1

    print('单链表的中间节点：')
    # 找到单链表的中间节点 4
    mid = findMiddleNode(head)
    print(mid.value)

    print('后半截无头单链表逆序：')
    # 后半截无头单链表逆序
    backRevercehead = backReverce(mid)
    cur = backRevercehead
    while cur != None:
        print(cur.value)
        cur = cur.next

    print('合并后的最终结果：')
    resultHead = merge(head, backRevercehead)
    cur = resultHead
    while cur.next != None:
        print(cur.next.value)
        cur = cur.next
