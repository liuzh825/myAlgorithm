'''
栈 1，2，3，4，5  翻转后 5，4，3，2，1
1、 使用数组实现一个栈
2、 把栈底元素移动到栈顶
3、 递归调用步骤2处理除了栈顶的子栈
'''


class Stack():
    def __init__(self):
        self.item = []

    # 判断是否为空
    def isEmpty(self):
        return len(self.item) == 0

    # 栈大小
    def size(self):
        return len(self.item)

    # 返回栈顶元素
    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.item[-1]

    # 压栈
    def push(self, v):
        self.item.append(v)

    # 出栈
    def pop(self):
        if self.isEmpty():
            return
        else:
            self.item.pop(-1)


def moveBottomToTop(myStack):
    if myStack.isEmpty():
        return
    top1 = myStack.peek()
    myStack.pop()
    if not myStack.isEmpty():
        moveBottomToTop(myStack)
        top2 = myStack.peek()
        myStack.pop()
        myStack.push(top1)
        myStack.push(top2)
    else:
        myStack.push(top1)


def reverse_stack(myStack):
    if myStack.isEmpty():
        return
    moveBottomToTop(myStack)
    top = myStack.peek()
    myStack.pop()
    reverse_stack(myStack)
    myStack.push(top)

if __name__ == '__main__':
    myStack = Stack()
    myStack.push(5)
    myStack.push(4)
    myStack.push(3)
    myStack.push(2)
    myStack.push(1)

    reverse_stack(myStack)
    while not myStack.isEmpty():
        print(myStack.peek())
        myStack.pop()
