#编写函数, 接收一个列表和一个索引，返回这个列表中对应索引的数据，
#如果索引超出范围，返回-1.
#2021/6/9/19/59
#

def fun(num,i):
    if i>=0 and i < len(num):
        return num[i]
    else:
        return -1

a = [1,2,3,4,5,6]

print(fun(a,1))
print(fun(a,10))

#运行结果为
# 2
#-1
#