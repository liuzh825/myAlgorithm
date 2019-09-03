'''
栈 1，3，2  翻转后 1，2，3
1、 使用数组实现一个栈
2、 把栈底元素移动到栈顶 比较栈顶元素和子栈栈顶的元素排序
3、 递归调用步骤2处理除了栈顶的子栈
'''

class Stack():
    def __init__(self):
        self.item = []

    def empty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)

    def peek(self):
        if self.empty():
            return
        return self.item[-1]

    def push(self, v):
        self.item.append(v)

    def pop(self):
        if self.empty():
            return
        else:
            self.item.pop(-1)

def moveBottomToTop(s):
    '''
    移动栈底元素到栈顶 并和子栈栈顶元素作比较
    :param s:
    :return:
    '''
    if s.empty():
        return
    top1 = s.peek()
    s.pop()
    if not s.empty():
        moveBottomToTop(s)
        top2 = s.peek()
        if top1 > top2:
            s.pop()
            s.push(top1)
            s.push(top2)
        else:
            s.pop()
            s.push(top2)
            s.push(top1)

    else:
        s.push(top1)

def sortStack(s):
    if s.empty():
        return

    moveBottomToTop(s)
    top = s.peek()
    s.pop()
    sortStack(s)
    s.push(top)



if __name__ == '__main__':
    s = Stack()
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(5)
    s.push(1)


    sortStack(s)
    while not s.empty():
        print(s.peek())
        s.pop()

