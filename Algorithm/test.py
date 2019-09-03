import sys


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1

    result += left[i:]
    result += right[j:]
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    num = int(len(arr)/2)
    left = merge_sort(arr[:num])
    right = merge_sort(arr[num:])
    return merge(left, right)


if __name__ == '__main__':
    arr = [3,4,2,8,9,5,1]
    print("排序前的序列为：", arr)
    arr = merge_sort(arr)
    print("排序后的序列为：", arr)






