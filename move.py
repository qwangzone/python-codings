#https://www.zhihu.com/question/37152936  关于汉诺塔的很好的解释
def move(n, a='起点A', b='缓冲区B', c='目的地C'):
    if n==1:
        print(a + "-->" + c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1,b,a,c)
move(int(input('这个鬼东西有多少层？')))
