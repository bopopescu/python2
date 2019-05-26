def outer(): #1 +msg #2
    def inner1():
        def inner2():#3
            print("hello world")#1
        inner2()#3


    def inner3():
        def inner4():
            print("have a nice day")
        inner4()
    inner1()
    inner3()#+msg #2

outer()#1　　＃寫死參數回傳
