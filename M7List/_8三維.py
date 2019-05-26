list6 = [[[1,2],[3,4]],
          [[5,6],[7,8]],
          [[9,10],[11,12]]] #3*2*2


print(list6[0][0][0],end= ' ')
print(list6[0][0][1],end= ' ')
print(list6[0][1][0],end= ' ')
print(list6[0][1][1],end= ' ')
print(list6[1][0][0],end= ' ')
print(list6[1][0][1],end= ' ')
print(list6[1][1][0],end= ' ')
print(list6[1][1][1],end= ' ')
print(list6[2][0][0],end= ' ')
print(list6[2][0][1],end= ' ')
print(list6[2][1][0],end= ' ')
print(list6[2][1][1],end= ' ')
print( )
for i in range (len(list6)):
    for j in range(len(list6[i])):
        for k in range(len(list6[i][j])):
            print(list6[i][j][k],end = ' ')
print()

for i in range (len(list6)):

            print(list6[i])
print()

import random

list1 =[]

layer,row,col = eval(input("input layer, row,col:"))
for i in range(layer):
    list1.append([])
    for j in range(row):
        list1[i].append([])
        for k in range(col):
            list1[i][j].append(random.randint(1,100))
print(list1)
print()

