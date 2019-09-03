

def gradient_descent(y):
    x = 1
    alpha = 0.001  # 注意学习率不能太大，否则会震荡甚至发散，啥，不信 ？！陷入死循环之后你会改回来的
    deta = 1
    count = 1
    while abs(deta)>0.00001:  # abs()返回数字的绝对值
        deta = 4*x*(x**2-y)
        x -= alpha * deta
        count += 1
    return x,count

def newton(y):
    x=1
    deta = 1		# 牛顿法，求解方程的根不需要学习率，它会自动确定每一步的更新步长，细节可出门谷歌
    count = 1
    while abs(deta)>0.00001:
        fx = (y-x**2)**2
        deta = 4*x*(x**2-y)
        if not deta:  # 分母不能为0
            break
        x -= fx/(deta)
        count += 1
    return x,count


if __name__ == '__main__':
    res1, count1 = gradient_descent(16)
    print(res1, count1)
    res2, count2 = newton(16)
    print(res2, count2)
