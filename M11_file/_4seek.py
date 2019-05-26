import os

with open("lang.txt","r") as f:
    # data= f.read()
    # print(data)
    f.seek(10) #起點10開始
    f.seek(10,0)#起點10開始
    f.seek(10,os.SEEK_SET)#起點10開始

    print(f.read())
PI=3.1416
    print()