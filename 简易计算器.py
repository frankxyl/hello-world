def div(x,y):
    if y==0:
        return "除数不能为零" 
    else:
        return x/y

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multi(x,y):
    return x*y

# 主程序
# 输入两个数字
num1 = float(input("请输入第一个数："))
num2 = float(input("请输入第二个数："))
# 输入运算符
op = input("请输入运算符(+ - * /)：")

# 判断运算并输出结果
if op == "+":
    res = add(num1, num2)
elif op == "-":
    res = sub(num1, num2)
elif op == "*":
    res = multi(num1, num2)
elif op == "/":
    res = div(num1, num2)
else:
    res = "输入的运算符有误"

print("计算结果：", res)