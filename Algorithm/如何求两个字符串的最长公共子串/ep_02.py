


# 方法1：滑动比较法


def getMaxSubStr(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    maxLen = 0 # 公共子串的长度
    tmpMaxLen = 0
    maxLenEnd1 = 0 # 公共子串结束的位置
    sb = ""
    i = 0
    while i < len1 + len2:
        s1begin = s2begin = 0
        tmpMaxLen = 0
        if i < len1:
            s1begin = len1-i
        else:
            s2begin = i - len1
        j = 0
        while (s1begin+j < len1) and (s2begin+j < len2):
            if list(str1)[s1begin+j] == list(str2)[s2begin+j]:
                tmpMaxLen += 1
            else:
                if tmpMaxLen > maxLen:
                    maxLen = tmpMaxLen
                    maxLenEnd1 = s1begin + j
                else:
                    tmpMaxLen = 0
            j += 1
        if tmpMaxLen > maxLen:
            maxLen = tmpMaxLen
            maxLenEnd1 = s1begin + j
        i += 1
    i = maxLenEnd1 - maxLen
    while i < maxLenEnd1:
        sb = sb + list(str1)[i]
        i += 1
    return sb

if __name__ == '__main__':
    str1 = "abccade"
    str2 = "dgcadde"
    sb = getMaxSubStr(str1, str2)
    print(sb)