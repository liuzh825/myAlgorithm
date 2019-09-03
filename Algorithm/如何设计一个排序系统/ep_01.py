from collections import deque # 双向队列


class User():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.seq = 0

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def setSeq(self, seq):
        self.seq = seq

    def getId(self):
        return self.id

    def equal(self, arg0):
        o = arg0
        return self.id == o.getId()

    def toString(self):
        return 'id:' + str(self.id) + 'name:' + str(self.name) + 'seq:' + str(self.seq)


class MyQueue():
    def __init__(self):
        self.q = deque()

    # 进入到对尾
    def enQueue(self, u):
        u.setSeq(len(self.q) + 1)
        self.q.append(u)

    # 队头出队列
    def deQueue(self):
        self.q.popleft()  # 删除队列头元素
        self.updateSeq()

    # 队列中的人随机离开
    def deQueuemove(self, u):
        self.q.remove(u)  # 根据元素删除
        self.updateSeq()

    # 出队列之后更新队列中的每一个人的序列
    def updateSeq(self):
        i = 1
        for u in self.q:
            u.setSeq(i)
            i += 1

    # 打印队列的信息
    def printList(self):
        for u in self.q:
            print(u.toString())

if __name__ == '__main__':
    u1 = User(1, 'user1')
    u2 = User(2, 'user1')
    u3 = User(3, 'user1')
    u4 = User(4, 'user1')
    queue = MyQueue()
    queue.enQueue(u1)
    queue.enQueue(u2)
    queue.enQueue(u3)
    queue.enQueue(u4)
    queue.deQueue()
    queue.deQueuemove(u3)
    queue.printList()
