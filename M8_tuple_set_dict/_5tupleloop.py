tuple1 = ((13,11),'python', 'java', 'c', 'c#')

for data in tuple1:
    print(data)


tuple1 = ((21,45),(88,99),(12,67))

for data in tuple1:
    print(data)

for data in tuple1:
    for data1 in data:
        print(data1,end = ' ')
    print( )

list1 = [(21,45),(88,99),(12,67)]
for data in list1:
    print(data)