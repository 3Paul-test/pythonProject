
def test_1(x,y):
    if x>y:
        print('x大于y')
    elif x==y:
        print('x=y')
    else:
        print('x小于y')


def guess():
    while True:
        num1 = input('请输入数字：')
        try:
            num1 = int(num1)
        except ValueError:
            print('参数类型错误哦，请输入数字')
            continue

        if num1 > 50:
            return '太大了'
        elif num1 == 50:
            return '正常'
        elif num1 < 50:
            return '太小了'


print(guess())

