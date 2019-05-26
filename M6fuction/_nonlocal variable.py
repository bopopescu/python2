#P51
def func():#############
    x= 10
    def get_x():
        return x

    def set_x(n):#setY
         nonlocal x # 改local 變數方法
         x = n;
    return get_x,set_x

getx,setY = func()
print(getx())
setY(20)
print(getx())