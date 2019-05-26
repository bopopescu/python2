def outer(msg):
    print("hi",msg)

    def inner():
        print(msg)##回傳參數
    inner()
outer("hello world")
outer("python good")