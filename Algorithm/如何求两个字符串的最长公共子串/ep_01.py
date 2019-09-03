


# 方法1：动态规划法

# 缺点是申请了m*n的额外的存储空间

def getMaxSubStr(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    sb = ""  # 最长公共子串
    maxs = 0 # 用来记录最长公共子串的长度
    maxI = 0 # 用来记录最长公共子串的最后一个字符的位置

    # 申请新的空间来记录公共子串长度信息 （len1*len2的矩阵）
    M = [([None]*(len1+1)) for i in range(len2 + 1)]

    # 填写第0行和第0列
    i = 0
    while i < len1 + 1:
        M[i][0] = 0
        i += 1
    j = 0
    while j < len2 + 1:
        M[0][j] = 0
        j += 1

    # 通过递归的方式填写新建的二维数组
    i = 1
    while i < len1+1:
        j = 1
        while j < len2+1:
            if list(str1)[i-1] == list(str2)[j-1]:
                M[i][j] = M[i-1][j-1] + 1
                if M[i][j] > maxs:
                    maxs = M[i][j]
                    maxI = i
            else:
                M[i][j] = 0
            j += 1
        i += 1
    # 找出公共子串
    i = maxI - maxs
    while i < maxI:
        sb = sb + list(str1)[i]
        i += 1
    return sb


if __name__ == '__main__':
    str1 = "abccade"
    str2 = "dgcadde"
    sb = getMaxSubStr(str1, str2)
    print(sb)