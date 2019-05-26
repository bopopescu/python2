str1 = 'hello123'
print(str1.isalnum())
print(str1.isalpha())
print(str1.isdigit())
print(str1.isidentifier())
print()

str1 = 'hello 123'
print(str1.isalnum())
print(str1.isalpha())
print(str1.isdigit())
print(str1.isidentifier())
print()

str1 = 'hello'
print(str1.isalnum())
print(str1.isalpha())
print(str1.isdigit())
print(str1.isidentifier())
print()

str1 = '_123'
print(str1.isidentifier())
print()

str1 = '123'
print(str1.isidentifier())
print()

str1 = 'hello'
print(str1.isupper())
print(str1.islower())
print('$')
str1 = 'HELLO'
print(str1.isupper())
print(str1.islower())
print('%')
str1 = 'HELLO123'
print(str1.isupper())
print(str1.islower())
print()

str1 = 'HELLO123'
print(str1.isupper())
print(str1.islower())
print()

str1 = ' '
print(str1.isspace())
print()

str1 = '\n'
print(str1.isspace())
print()

str1 = '\t'
print(str1.isspace())
print()

str1 = '\b'##back
print(str1.isspace())
print()

str1 = 'hello world'
print(str1.startswith('hello'))
print(str1.startswith('Hello'))

str1 = "hello.py"
print(str1.endswith('.py'))