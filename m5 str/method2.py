str1 = "python world, python is simple language, python is good"
print(str1.find("hello"))
print(str1.find("Hello"))

print(str1.find("python"))
print(str1.rfind("python"))
print(str1.count("python"))

print(str1.capitalize())
print(str1.lower())
print(str1.upper())
print(str1.title())
print(str1.swapcase())

print(str1.replace('python','java'))

str1= "  Hello  World  "

print(str1.lstrip())#DEL L 空白
print(str1.rstrip())#DEL R 空白
print(str1.strip())#DEL both 空白

str1= "hello"
width= 20
print("/"+str1.center(15)+"/")##/     hello     /
print("/"+str1.center(width)+"/")#/       hello        /

print("/"+str1.ljust(15)+"/")#/hello          /
print("/"+str1.rjust(15)+"/")#/          hello/
