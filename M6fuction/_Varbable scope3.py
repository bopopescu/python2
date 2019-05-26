
#P50
x = 10


def outer():
    x = 20

    def inner():
        y = 20

        def inner1():
         nonlocal x
         print(x)#20 ---> X
         x  = 40

        inner1()
        print(x)#40
    inner ()
    print (x)  #40


outer ()
print (x)  #10

print ()