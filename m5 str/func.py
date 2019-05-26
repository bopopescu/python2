str1 = 'hello world'
print(len(str1))

for i in str1:
    print(i,end='')
print()


##抓取所有元素 hello world 無限延伸
for i in range (0,len(str1)):#
    print(str1[i],end='')

print()
print(max(str1))
print(min(str1))## AScii 空白直

str2= "simple"
print(str2+str1)
print(str1*3,end=" ")