'''
使用数组实现栈

具体方法
是否为空  栈的大小  栈顶元素  弹栈  压栈
'''




class MyStack():
    def __init__(self):
        self.items = []

    # 是否为空
    def isEmpty(self):
        return len(self.items) == 0

    # 栈的大小
    def Size(self):
        return len(self.items)

    # 栈顶元素
    def Top(self):
        return self.items[len(self.items) - 1]

    # 弹栈
    def pop(self):
        self.items.pop()

    # 压栈
    def push(self, v):
        self.items.append(v)

if __name__ == '__main__':
    ms = MyStack()
    ms.push(1)
    ms.push(2)
    print('查看栈中元素：', ms.items)
    if ms.isEmpty():
        print('栈为空')
    else:
        print('栈不为空')
    print('栈顶元素', ms.Top())
    ms.pop()
    print('弹栈后查看栈中元素：', ms.items)
    ms.push(3)
    print('压栈后查看栈中元素：', ms.items)