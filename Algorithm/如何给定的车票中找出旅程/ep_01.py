
'''
根据车票的出发地和目的地构建字典

构建车票的逆向字典

遍历字典 如果key在逆向的字典中存在 pass  如果不存在 就是路途的起点
'''
def printResult(inputs):
    # 构建逆向字典
    reverseInput = dict()
    for k, v in inputs.items():
        reverseInput[v] = k

    # 找到起点
    start = ''
    for k, v in inputs.items():
        if not k in reverseInput:
            start = k
    if start == '':
        print('输入有误')
        return
    to = inputs[start]
    print(start + "到" + to,)
    start = to
    to = inputs[to]
    while to != None:
        print(start + "到" + to, )
        start = to
        to = inputs.get(to, None)   # 坑点




if __name__ == '__main__':
    inputs = dict()
    inputs['西安'] = '成都'
    inputs['北京'] = '上海'
    inputs['大连'] = '西安'
    inputs['上海'] = '大连'
    printResult(inputs)