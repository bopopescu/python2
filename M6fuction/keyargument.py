def msg(name, age):
    print("{}is a {} years old.".format(name,age))

def main():
    msg('mary',34) #posistional argument
    msg ( age =35, name = 'john')#keyargument
    msg ('amy', age =33)
    #msg (name='amy', 33)# POS>key位置 引數
main()