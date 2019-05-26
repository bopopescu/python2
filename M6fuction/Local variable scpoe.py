x= 10
y= 11
def main():
    x= 20
    print(x)
    print(y)
main()
print(x)
print(y)
print()

def outer ():
    x =20
    def inner():
        x= 30
        print(x) #30
        print(y)
    inner()
    print (x) #20
    print (y)
outer()
print(x)#10
print(y)

print()



x=10 #global

def outer():
    x= 20  # x便灰色　記憶體回收
    def inner():
        x =30
        print(x)#30
    inner()
    print(x)#20
outer()
print(x)#10