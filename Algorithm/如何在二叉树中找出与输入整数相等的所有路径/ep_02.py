import random


def generate_random_numbers(total_num=10, max_num=20):
    num_list = []
    for i in range(total_num):
        num_list.append(random.randint(0, max_num))
    return num_list


def dict_sort(num_list):
    final_list = []
    num = 1
    decrease_list = sorted(num_list, reverse=True)
    increase_list = sorted(num_list)
    for i in range(len(increase_list)):
        num *= increase_list[i]  # A(n,n)代表所有元素的全排列数量
    while num:  # 这里循环产生A(n,n)次
        for i in range(len(num_list) - 2, -1, -1):
            if num_list[i] < num_list[i + 1]:
                flagi = i
                break
        for j in range(len(num_list) - 1, flagi, -1):
            if num_list[j] > num_list[flagi]:
                flagj = j
                break
        # num_list[i], num_list[j]=num_list[j], num_list[i]
        num_list[flagi], num_list[flagj] = num_list[flagj], num_list[flagi]
        num_list2 = sorted(num_list[i + 1:])
        result_list = num_list[:i + 1] + num_list2
        final_list.append(''.join([str(x) for x in result_list]))
        num -= 1

    return final_list


if __name__ == '__main__':
    num_list1 = [1, 2, 3]
    num_list2 = [1, 2, 3, 4]
    final_list1 = dict_sort(num_list1)

    print(len(final_list1))

    final_list2 = dict_sort(num_list2)

    print(len(final_list2))
