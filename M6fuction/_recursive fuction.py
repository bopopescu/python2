def func(n):
    print("level",n)
    if n<4:
        func(n+1)
    print("LEVEL",n)
def mian():
    func(1)
mian()
