"""用户输入姓名后生成1个100之内的随机数
如果用户猜的数字比目标数字大，提示过大
如果用户猜的数字比目标数字小，提示过小
如果用户猜测正确,打印目标数字，退出游戏
如果用户猜对了，自动进行下一轮游戏.
用户输入非数字的话要求重新输入
实现用户按q可以退出游戏功能
用户猜测成功后询问用户是继续还是按q退出
增加按Q也可以退出功能
用户一共有5次猜测机会，5次没猜中游戏结束
"""
import random
import sys
while True:
    target = random.randint(1, 99)
    print ("I am thinking a number between 1 and 100")
    print (target)
    times = 0
    while True:
        while True:
            user_input = input("take a guess and input 'q' to exit\n")
            if user_input.strip().lower() == 'q':
                sys.exit("goodbye,see you next time")
            if user_input.isdigit():
                user_number = int(user_input)
                break
            else:
                print("输入不合法，请重新输入：")
        if times > 5:
            sys.exit("times out")
        if user_number > target:
            print ("Your guess is too high")
            times = times + 1
        elif user_number < target:
            print ("Your guess is too low")
            times = times + 1
        else:
            print ("Good job, the correct number is %s" %target)
            print ("Continue or enter 'q' to quit.")
            user_input1 = input("")
            if user_input1 !='q':
                break
            else:
                sys.exit("goodbye")