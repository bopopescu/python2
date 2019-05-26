import random
list1=[45,65,78,34,25,66,12,67]

for i in range(len(list1)):
    print((list1[i]),end=',')
print()
for val in list1:
    print(val,end= ',')
print()



list1 =[]
for i in range(6):
    list1.append(random.randint(1,100))

print(list1)