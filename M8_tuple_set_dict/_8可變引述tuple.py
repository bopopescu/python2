def greet(*names):
    for name in names:
        print("hello ,", name)

def main():
    greet ("tom", "mary", "stephen", "tina")
    print()
    names= ("tom", "mary", "stephen", "tina")
    greet(names)
    greet(*names)
    print()
    names= ("tom", "mary", "stephen", "tina")
    greet(*names)
    print(14)
    names = 'mary'
    greet(names)
    greet(*names)
    print(18)

main()