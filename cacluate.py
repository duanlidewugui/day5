#编写一个函数cacluate, 可以接收任意多个数,返回的是一个元组.
#元组的第一个值为所有参数的平均值, 第二个值是大于平均值的所有数
#2021/6/9/19/59
#

number =[1,2,3,4,5]

def calute(number):
    k = 0
    if len(number) > 1:
        for i in number:
            k = k + i
    elif len(number) == 1:
        print("只有一个数字")
        return number
    else:
        print("没有数字")
        return number

    avg = k / len(number)

    i = 0
    #num接收所有大于平均数的参数
    num = []
    while i < len(number):
        if number[i] > avg:
            num.append(number[i])
        i += 1
    return(avg,num)
a = calute(number)
print(a)

#运行结果为
#(3.0, [4, 5])




