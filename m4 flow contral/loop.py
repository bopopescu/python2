sum=0
for i in range(1,11):
    sum+=i
print(sum)

n = 1
total =0
while n<=10:
    total+=n
    n+=1
print(total)

#1+2+...+10

n =10
total =0
while n>=1:
    total+=n
    n-=1
print(total)

#10+9+8+...+1

n = 10
total =0
while n<=1:
    total+=n
    n-=1
print(total)
#邏輯錯誤 while n<=1:

n = 2
total = 0
while n <= 100:
    total+= n
    n+= 2
print(total)

n = 1
total =0
while n<=100:
    total+=n
    n+=2
print(total)

total= 0
for n in range(10,0,-1):
    total+=n
print(total)