# def mdbig():
#     a = 25
#     def mdsmall(x):
#         return a*x*x
#     return mdsmall

# a = 10
# count = mdbig()
# print(count(2))


def nianjiang(year, proportion):
    def bonus(salary):
        return salary * year * proportion
    return bonus

print('请输入工作年份')
x = int(input())
print('请输入月薪')
y = int(input())
hanshu = nianjiang(x,0.5)
print(hanshu(y))
