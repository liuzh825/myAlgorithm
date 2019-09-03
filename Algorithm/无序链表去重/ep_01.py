# coding=UTF-8
'''顺序删除'''

'''
1,3,1,5,5,7
1,3,5,7
'''


class LNode():
    def __init__(self, value=None):
        self.value = value
        self.next = None

def remover(head):
    outerCur = head.next
    while outerCur != None:
        innerCur = outerCur.next
        innerPre = outerCur
        while innerCur != None:

            if innerCur.value == outerCur.value:
                innerCur = innerCur.next
                innerPre.next = innerCur

            else:
                innerPre = innerCur
                innerCur = innerCur.next

        outerCur = outerCur.next




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
    remover(head)
    cur = head.next
    while cur != None:
        print(cur.value)
        cur = cur.next