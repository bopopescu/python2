
#p61 動態二維陣列
import  random
print('--------------------')
list1 =[]
row,col = eval(input("input row and col :  "))
for i in range (row):
    list1.append([])
    for j in range(col):
        list1[i].append((random.randint(1,100)))
print(list1)
print('--------------------')


