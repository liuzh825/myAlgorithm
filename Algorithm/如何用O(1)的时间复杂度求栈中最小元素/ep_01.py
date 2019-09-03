'''

1、 使用数组实现一个栈
2、 申请一个额外的栈来保存每个状态的最小值
3、 push 知道栈顶元素等于 pop 第一个元素 然后出栈 之后就像上述操作
4、 push 全部入栈 pop为完全遍历 并且栈顶元素不等于当前pop元素 return False
5、 栈为空 pop完全遍历 True
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


class myStack():
    def __init__(self):
        self.elementStack = Stack()
        self.minsStack = Stack()

    def push(self, v):
        self.elementStack.push(v)
        if self.minsStack.empty():
            self.minsStack.push(v)
        else:
            if v < self.minsStack.peek():
                self.minsStack.push(v)

    def pop(self):
        topData = self.elementStack.peek()
        self.elementStack.pop()
        if topData == self.minsStack.peek():
            self.minsStack.pop()

    def mins(self):
        if self.minsStack.empty():
            return 2 ** 32
        else:
            return self.minsStack.peek()


if __name__ == '__main__':
    s = myStack()
    s.push(5)
    print('栈中最小元素是：', str(s.mins()))
    s.push(6)
    print('栈中最小元素是：', str(s.mins()))
    s.push(2)
    print('栈中最小元素是：', str(s.mins()))
    s.pop()
    print('栈中最小元素是：', str(s.mins()))

