import random
counts = 5
answer=random.randint(0,100)
while counts>0:
    temp=input("请输入一个数字")
    guess=int(temp)
    if guess==answer:
        print("bingo")
        break
    else:
        if guess <answer:
            print("小了")
        else:
            print("大了")
        counts=counts-1
print("游戏结束")