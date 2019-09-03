from collections import deque # 双向队列

'''
思路：双向队列  hashset  缓存大小
要求 访问的页面放队列头  不访问的放后面 缓存不够就从队列尾删除
'''


class LRU():
    def __init__(self, cacheSize):
        self.cacheSize = cacheSize
        self.q = deque()
        self.hashSet = set()

    # 判断缓存是否满了
    def isQueueFull(self):
        return len(self.q) == self.cacheSize

    # 访问页面入队列头
    def enQueue(self, pageNum):
        if self.isQueueFull():
            self.hashSet.remove(self.q[-1])
            self.q.pop()
        self.q.appendleft(pageNum)
        self.hashSet.add(pageNum)

    def accessPage(self, pageNum):
        '''
        不在队列中直接缓存到头部
        在队列中但是不在队列头 缓存到队列头
        :param pageNum:
        :return:
        '''
        if pageNum not in self.hashSet:
            self.hashSet.add(pageNum)
            self.enQueue(pageNum)

        elif pageNum != self.q[0]:
            self.q.remove(pageNum)
            self.q.appendleft(pageNum)

    def printQueue(self):
        while len(self.q) > 0:
            print(self.q.popleft())

if __name__ == '__main__':
    lru = LRU(3)
    lru.accessPage(1)
    lru.accessPage(2)
    lru.accessPage(5)
    lru.accessPage(1)
    lru.accessPage(6)
    lru.accessPage(7)
    lru.printQueue()