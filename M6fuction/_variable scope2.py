x =10

def outer ():


    x =20

    def inner():
        nonlocal  x  #上一層X
        print(x)
      #  print (x)順序 先宣告後print
         #local varibale
        print(x) #30
        x= 30
    inner()
    print (x) #20

outer()
print(x)#10

print()