


'''
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''



# 定义链表
class linkNode():
    def __init__(self, value=None):
        self.value = value
        self.next = None

# 快慢指针 判断是否有重复的节点
def Remove(pHead):
    if not pHead or pHead.next == None:
        return pHead
    head = pHead
    pre = head
    last = pHead.next
    while last != None:
        if last.next != None and last.value == last.next.value:
            while last.next != None and last.value == last.next.value:
                last = last.next
            pre.next = last.next
            last = last.next
        else:
            pre = pre.next
            last = last.next

    return head



if __name__ == '__main__':
    head = linkNode()
    head.next = linkNode(1)
    head.next.next = linkNode(2)
    head.next.next.next = linkNode(3)
    head.next.next.next.next = linkNode(3)
    head.next.next.next.next.next = linkNode(4)
    head.next.next.next.next.next.next = linkNode(4)
    head.next.next.next.next.next.next.next = linkNode(5)

    newHead = Remove(head)
    cur = newHead
    while cur.next != None:
        print(cur.next.value)
        cur = cur.next


