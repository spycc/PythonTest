origin = 0

def weizhi(wz):
    def go(bushu):
        nonlocal wz #因为该函数内没有定义wz这个变量，因此要定义该wz不是局部变量，因此系统就认为wz是闭包的环境变量
        nowwz = wz + bushu
        wz = nowwz
        return nowwz
    return go

f = weizhi(0)
print(f(2))
print(f(3))
print(f(5))

