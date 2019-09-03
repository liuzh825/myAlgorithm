


'''
思路  队列 先进先出

用两个栈来实现
A栈实现入栈
B栈实现出栈  出栈如果B为空了  A栈的元素先到B栈  然后B在出栈
'''


class Stack():
    def __init__(self):
        self.item = []

    def empty(self):
        return len(self.item) == 0

    def size(self):
        if self.empty():
            return 0
        return len(self.item)

    def peek(self):
        if self.empty():
            return None
        return self.item[-1]

    def push(self, data):
        self.item.append(data)

    def pop(self):
        if self.empty():
            return
        self.item.pop()

class Mystack():
    def __init__(self):
        self.A = Stack()
        self.B = Stack()

    def push(self, data):
        self.A.push(data)

    def pop(self):
        if self.B.size() == 0:
            while not self.A.empty():
                temp = self.A.peek()
                self.A.pop()
                self.B.push(temp)
        first = self.B.peek()
        self.B.pop()
        return first


if __name__ == '__main__':
    s = Mystack()
    s.push(1)
    s.push(2)
    print('队列的首元素是：', s.pop())
    print('队列的首元素是：', s.pop())

