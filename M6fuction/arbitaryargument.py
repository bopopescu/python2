def greet(*names):
    for name in names:
        print("hello ,", name)

def main():
    greet ("tom", "mary", "stephen", "tina")

main()