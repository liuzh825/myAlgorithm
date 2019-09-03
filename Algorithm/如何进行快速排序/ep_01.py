
'''
快速排序

时间复杂度为 O(n2)
空间复杂度O(logn)
'''


def quick_sort(arr, left, right):
    if left >= right:
        return arr
    key = arr[left]
    low = left
    high = right

    while left < right:
        while left < right and arr[right] >= key:
            right -= 1
        arr[left] = arr[right]

        while left < right and arr[left] <= key:
            left += 1
        arr[right] = arr[left]

    arr[right] = key
    quick_sort(arr, low, left-1)
    quick_sort(arr, left+1, high)
    return arr


if __name__ == '__main__':
    arr = [3,4,2,8,9,5,1]
    print("排序前的序列为：", arr)
    arr = quick_sort(arr, 0, len(arr)-1)
    print("排序后的序列为：", arr)
