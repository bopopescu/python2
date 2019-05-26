##### 值均為字串
dict1 = {'name': 'tom' , 'age': 25 , 'mobile ': '0934111222'}

print ( len ( dict1 ) )
print ( 'age' in dict1 )
print ( 'tom' in dict1 )

dict2 = {'age': 30 , 'mobile ': '0934111222'}
print ( dict1 == dict2 )

dict1 [ "email" ] = 'tom@gmail.com'
print ( len ( dict1 ) )

print ( dict1 )

del dict1 [ 'age' ]  ##刪除項目
print ( dict1 )

print ( dict1.pop ( 'email' ) )  # POP先取後刪除
print ( dict1 )

print ( dict1.popitem ( ) )  # POP先取(值tuple)後刪除
print ( dict1 )

dict1.clear ( )  # 清空{}
print ( dict1 )

dict1 = dict2.copy ( )
print ( dict1 )


dict1 ={'name': 'tom' , 'age': 25,'email':'tom@gmail.com' }
dict2 ={ 'age': 26,'moblie':'0988888887','name':'tom' }
dict1.update(dict2)
print(dict1)
print(dict2)