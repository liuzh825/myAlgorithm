# coding=utf-8

'''
输入：1，2，3，4，5，6，7  假设k=3
result: 3,2,1,6,5,4,7

思路
1 pre指向head  begin指向1  end指向3 pNext记录4
2 end.next=None 翻转1，2，3
3 翻转后的3，2，1接在head后面 head.next=end
4 begin指向pNext  不够k个 不做处理
'''

class LNode():
    def __init__(self, value=None):
        self.value = value
        self.next = None


def FlipK(head, k):

    if head == None or head.next == None or k < 2:
        return
    i = 1
    pre = head
    begin = head.next
    end = None
    pNext = None
    while begin != None:
        end = begin
        while i < k:
            if end != None:
                end = end.next
            else:
                return
            i += 1
        pNext = end.next
        end.next = None
        tmpNode = Flip(begin)
        pre.next = tmpNode
        cur = pre
        while cur.next != None:
            cur = cur.next
        cur.next = pNext
        pre = cur
        begin = pNext
        i = 1



def Flip(head):
    '''
    翻转无头链表
    :param head:
    :return:
    '''
    if head == None or head.next == None:
        return head
    pre = head
    cur = head.next
    next = None
    pre.next = None

    while cur != None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre





if __name__ == '__main__':
    print('原链表：')
    i = 1
    head = LNode()
    cur = head
    while i < 8:
        cur.next = LNode(i)
        print(cur.next.value)
        cur = cur.next
        i += 1

    print('翻转之后的链表：')

    FlipK(head, 3)
    cur = head.next
    while cur != None:
        print(cur.value)
        cur = cur.next



    # 测试Flip
    # head = LNode(1)
    # cur = head
    # cur.next = LNode(2)
    # cur = cur.next
    # cur.next = LNode(3)
    # cur = cur.next
    # cur.next = LNode(4)
    # cur = cur.next
    # cur.next = None
    # cur = head
    # while cur != None:
    #     print(cur.value)
    #     cur = cur.next
    # print('Flip')
    # pre = Flip(head)
    # cur = pre
    # while cur != None:
    #     print(cur.value)
    #     cur = cur.next


