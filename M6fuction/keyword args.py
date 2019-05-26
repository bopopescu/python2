def stu(**data):
    for key,value in data.items():
        print("{} = {}".format(key,value))

def main():
    stu(name="mary",age=56,mobile= "12309812",id ='A123451234')
    print()

main()