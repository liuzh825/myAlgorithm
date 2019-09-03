
'''
构建字典 key为数对的和 value为数对

遍历所有可能的数对 如果和在字典中  print
'''
class pair():
    def __init__(self, first=None, second=None):
        self.first = first
        self.second = second

def findPairs(arr):
    # 构建字典key为数对的和value为数对
    sumPair = dict()
    n = len(arr)
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            sum = arr[i] + arr[j]
            if sum not in sumPair:
                sumPair[sum] = pair(i, j)
            else:
                print((arr[sumPair[sum].first], arr[sumPair[sum].second]), (arr[i], arr[j]))
                return True
            j += 1

        i += 1
    return False


if __name__ == '__main__':
    arr = [3,4,7,10,20,9,8]
    findPairs(arr)