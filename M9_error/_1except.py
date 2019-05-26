'''
try:
    num = int(input("please input a  number"))

    print("{} is an {}".format(num,'odd' if num %2 else 'even'))

except ValueError as e:
    print(e)
'''

try:
    num = int(input("please input a  number"))

    print("{} is an {}".format(num,'odd' if num %2 else 'even'))

except ValueError  :
        print('please input a number, not char!!')


