# a = (1,2)

# def add (x):
#     return x + x

# b = map(add,a)
# print(list(b))



b = [1,0,0,1,1,1,0,1]
count = filter(lambda x: True if x == 0 else False,b )
print(list(count))