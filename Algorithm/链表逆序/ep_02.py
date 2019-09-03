# coding=UTF-8
import re

'''前插法'''

'''
1,2,3,4,5,6,7
7,6,5,4,3,2,1
'''

class Node():
    def __init__(self, value = None):
        self.value = value
        self.next = None



def reverse(head):
    # if head.next == None:
    #     return

    # 只需要当前节点和后继节点
    cur = None
    next = None

    # 从2开始处理
    cur = head.next.next

    # 将1设置为最后一个节点
    head.next.next = None

    while cur != None:
        # 记录3
        next = cur.next

        # 2的下一个节点是head后面那个节点 也就是1
        cur.next = head.next

        # 将2放置在head后面
        head.next = cur

        # 将指针cur指向3
        cur = next

if __name__ == '__main__':
    i = 1
    head = Node()
    cur = head
    print('反转之前')
    while i < 8:
        cur.next = Node(i)
        print(cur.next.value)
        cur = cur.next
        i += 1


    print('反转之后')

    reverse(head)

    while cur != None:
        print(cur.value)
        cur = cur.next
