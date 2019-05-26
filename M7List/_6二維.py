list1=[]
list2=[[1,2,3],[4,5,6]]
list3 =[[1,2],[3,4],[5,6]]
list4 =[[1,2],[3,4,5],[6,7,8,9]]

print(list4[1][2])
print(list4[2][3])
print(len(list3))#列數
print(len(list4[0]))

print('--------------------')
list6 = [[10,20,30],[40,50,60]]
for i in range (len(list6)):
    for j in range(len(list6[0])):
        print(list6[i][j],end = ' ')
print()
print('--------------------')
print(list6[0][0],end= ' ')
print(list6[0][1],end= ' ')
print(list6[1][0],end= ' ')
print(list6[1][1],end= ' ')
print(list6[1][2],end= ' ')


print()

print('$$$$$$$$$$$$$$$')


list5 = [[10,20],[30,40,50],[60,70,80,90]]
for i in range (len(list5)):

    for j in range (len (list5[i])):####[i]

        print (list5[i][j], end=' ')


print()
print('$$$$$$$$$$$$$$$$$$')
print(list5[0][0],end= ' ')
print(list5[0][1],end= ' ')
print(list5[1][0],end= ' ')
print(list5[1][1],end= ' ')
print(list5[1][2],end= ' ')
print(list5[2][0],end= ' ')
print(list5[2][1],end= ' ')
print(list5[2][2],end= ' ')
print(list5[2][3],end= ' ')

print()
print(list5)
print(list5[0])
print(list5[1])
print(list5[2])
print((len(list5)))










