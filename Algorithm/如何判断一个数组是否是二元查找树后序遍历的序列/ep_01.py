


def funcOne(arr, start, end):
    if arr == None:
        return False
    root = arr[end]
    i = start
    while i < end:
        if arr[i] > root:
            break
        i += 1
    j = i
    while j < end:
        if arr[j] < root:
            return False
        j += 1
    left = True
    right = True
    if i > start:
        left = funcOne(arr, start, i-1)
    if j < end:
        right = funcOne(arr, i, end)
    return left and right


if __name__ == '__main__':
    arr = [1,3,2,5,7,6,4]
    result = funcOne(arr, 0, len(arr)-1)
    if result:
        print("是")
    else:
        print("不是")
