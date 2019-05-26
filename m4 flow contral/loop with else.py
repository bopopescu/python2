for i in range(1,10):
    for j in range (1,10):
        print("{}*{}={} ".format(i,j,i*j),end = '\t')
    print()
print('==================================================')

for i in range(1,10):
    for j in range (1,10):
        print("{0}*{1}={2} ".format(j,i,i*j),end = '\t')
    print()
print('==================================================')



print('\b |	1	2	3	4	5	6	7	8	9')
print('----------------------------------------------------------------------')
for i in range(9,0,-1):
    for j in range (1,i+1):
        print("{}".format(i*j),end = '\t')
    print()


for i in range(5):
    for j in range(0,i):
        print(" ",end=" ")

    for j in range(i,5):
        print("*", end=" ")

    print("")

for i in range (6):
    for j in range (0, 5-i):
        print ("$", end=" ")

    for j in range (5-i, 5):
        print ("*", end=" ")

    print ("")
print( )

for i in range(6):
    for j in range(0, 6 -i):
        print(end=" ")
    for k in range(6 - i, 6):
        print("*", end=" ")

    print("")

