with open("lang.txt","r") as f:
    line =f.readline()
    while line !='':#檢查空字串1 檢查到黨尾
        print(line,end='')
        line= f.readline()
print('-----------')
with open("lang.txt","r") as f:
    line =f.readline()
    while line !='':#檢查空字串1 檢查到黨尾
        print(repr(line))
        line= f.readline()
print ( '-----------' )

with open("lang.txt","r") as f:
    data: str =f.read()
    print(data)
    print(repr(data))
print ( '-----------' )

with open("lang.txt","r") as f:
    data: str =f.read(10)
    print(data)
    print('-----------')

    data: str =f.read(10)
    print(data)
    print('-----------')

    data: str = f.read(10)
    print(data)
    print('-----------')
 #有多少就讀多少
with open("lang.txt","r") as f:
    data= f.readlines()
    print(data)

with open("lang.txt","r") as f:
    data= f.readlines(2) #子串無條件進位02
    print(data)