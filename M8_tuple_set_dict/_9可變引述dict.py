def stu(**data):
    for key,value in data.items():
        print("{} = {}".format(key,value))

def main():
    stu(name="mary",age=56,mobile= "12309812",id ='A123451234')
    print()
    dict1 = {'name' : 'mary' , 'age' : '56' , 'mobile' : '12309812' , 'id' : 'a123456789'}
    stu(**dict1)

main()