'''
栈 1，3，2  翻转后 1，2，3
1、 使用数组实现一个栈
2、 入栈序列和出栈序列的长度不一样直接reurn False
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


def isPopSerial(push, pop):
    if push == None or pop == None:
        return False
    s = Stack()
    if len(push) != len(pop):
        return False
    pushLen = len(push)
    popLen = len(pop)
    pushIndex = 0
    popIndex = 0
    while pushIndex < pushLen:
        s.push(push[pushIndex])
        pushIndex += 1
        while (not s.empty()) and (s.peek() == pop[popIndex]):
            popIndex += 1
            s.pop()

    return s.empty() and popIndex == popLen








if __name__ == '__main__':
    push = '12345'
    pop = '32541'
    if isPopSerial(push, pop):
        print('是可能的出栈序列')
    else:
        print('不是可能的出栈序列')

