x= 10
y= 11

def main():
    x= 20
    print(x)
    global y
    y = 22
    print(y)

main()
print(x)
print(y)
print()