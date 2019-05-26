tuple1 = ('python', 'java', 'c', 'c#')
print ( tuple1 )
print ( tuple1 [ 0 ] )
print ( "c" in tuple1 )
print ( tuple1 * 2 )
# tuple.append("javascipt") #no append()

# list tuple 轉換 可變不可辨有序列
print ( tuple1 )
list1 = [ ]
list1.append ( 34 )
list1.append ( 67 )
list1.append ( 88 )
tuple1 = tuple ( list1 )  ## list 轉tuple

str1 = 'python'
tuple1 = tuple ( str1 )
print ( tuple1 )  ##('p', 'y', 't', 'h', 'o', 'n')
print ( tuple1 )
print ( type ( tuple1 ) )

tuple1 = (45,67,89,23,789,12,34)
tuple1+= (66,22)######加值 兩個 以上
print ( tuple1 )
tuple1 +=(99,)########    加值一個
print ( tuple1 )
del tuple1########del
print(tuple1)
list1 = list(tuple1)#轉換 在調整函數
print(list1)
