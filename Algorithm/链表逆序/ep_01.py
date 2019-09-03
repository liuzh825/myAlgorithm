# coding=UTF-8

'''后插法'''

class LNode:
    def __init__(self, x=None):
        self.data = x
        self.next = None


def Reverse(head):
    if head == None or head.next == None:
        return
    pre = None  # 前驱节点
    cur = None  # 当前节点
    next = None  # 后继节点
    # 把链表首节点变为尾节点
    cur = head.next
    next = cur.next
    cur.next = None
    pre = cur
    cur = next
    # 使当前遍历节点cur指向前驱节点
    while cur.next != None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    # 遍历到链表最后一个节点时候，将其指向前驱节点
    cur.next = pre
    # 头节点指向原来链表的最后一个节点
    head.next = cur


if __name__ == "__main__":

    i = 1
    # 链表的头结点
    head = LNode()
    cur = head
    # 构造单链表
    while i < 8:
        tmp = LNode(i)
        cur.next = tmp
        cur = tmp
        i += 1

    print("原链表：")
    cur = head.next
    while cur != None:
        print(cur.data)
        cur = cur.next
    print("\n逆序后：")
    Reverse(head)
    cur = head.next
    while cur != None:
        print(cur.data)
        cur = cur.next
