x = 10
print(x)
y = 10
print(y)
print(id(x))
print(id(y))
z=x
print(id(z))
x=20
print(id(x))#換記憶體空間
print(id(z))

a,b =10,20
print(id(a))
print(id(b))

a=c=b =1
print(id(a))
print(id(b))
print(id(c))
xxx = 100
print(id(xxx))
xxx =xxx+1

print(id(xxx))
print(x)