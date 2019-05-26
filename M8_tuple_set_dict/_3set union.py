


###聯集(|) 交集(&) 差及(-)對稱差及(^)          P66
set1 ={11,22,33,44,55}
set2 ={44,55,66,77,88}

print(set1.intersection(set2))#{44, 55}交集(&)
print(set1.union(set2))#{33, 66, 11, 44, 77, 22, 55, 88}聯集(|)
print(set1.difference(set2))#{33, 11, 22}差及(-)
print(set1.symmetric_difference(set2))#{33, 66, 11, 77, 22, 88}對稱差及(^)

print("----------------------------------------------")
print(set1&(set2))#{44, 55}交集(&)
print(set1|(set2))#{33, 66, 11, 44, 77, 22, 55, 88}聯集(|)
print(set1-(set2))#{33, 11, 22}差及(-)
print(set1^(set2))#{33, 66, 11, 77, 22, 88}對稱差及(^)
print("----------------------------------------------")

#子集合 超集合
set3 = {1,2,3,4,5,8}
set4 = {1,3,5}
print(set4.issubset(set3))## 4元素集合三

print(set3.issuperset(set4))##三包含四所有

print(set4==set3)#檢視兩集  合相 等不相等
print(set4!=set3)#檢視兩集合 相等   不相等
