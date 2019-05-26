##P56

list1 = []
list1.append(77)
list1.append(34)
list1.append(58)
list1.append(92)
list1.append(34)
list1.append(78)
print(list1)########[77, 34, 58, 92]

list1.insert(1,999)
print(list1)

print(list1.pop(0))#取完刪除77  [999, 34, 58, 92, 34, 78]
print(list1)
print('---------------------------------')

list1.reverse()
print(list1)

print('---------------------------------')
print(list1.pop())#取完刪除 預設從最後山除 92 [999, 34, 58, 92, 34]
print(list1)
print(list1.index(34)) #只取一個 並傳值
print('---------------------------------')
print(list1.count(34))

list1.remove(34)#刪除第一個34 ans :[999, 58, 92, 34]
print(list1)
print(list1.index(92))## 查詢位置  ans 2

list1.sort()#排序[34, 58, 92, 999] 小到大

print(list1)

list1.reverse()#[999, 92, 58, 34]反轉 並非大到小
print(list1)
