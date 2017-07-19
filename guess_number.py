import random
while True:
    target = random.randint(1, 99)
    print ("I am thinking a number between 1 and 100")
    print (target)

    while True:
        while True:
            user_input = input("take a guess!\n")
            if user_input.isdigit() and user_input !='q':
                user_number = int(user_input)
                break
            else:
                print("输入不合法，请重新输入：")
        """
        user_input = input("take a guess!\n")
        if not user_input.isdigit():
            print ("输入不合法，请重新输入：")
            continue
        """
        #try:
        #    user_number = int(user_input)
        #except:
        #   ( print "输入不合法，请重新输入")
        #    continue
        if user_number > target:
            print ("Your guess is too high")
        elif user_input =='q':
            break
        elif user_number < target:
            print ("Your guess is too low")
        else:
            print ("Good job, the correct number is %s" %target)
            break