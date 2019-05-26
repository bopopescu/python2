a = 123
b = 12345.6789
c = 'python'
print(format(a,'5d'))
print(format(a,'05d'))
print(format(a,'+5d'))
#print(format(a,'-5d')) -5d 無用 format模式
print(format(a,'<5d'))
print('%5d' % a )#將A 用空白補足五位數(又靠
print('%05d' % a )# 用0 補足五位數
print('%-5d' % a )# 負數 ,向左靠 不代表負數
print('%+5d' % a )# +符號




a =357
print(format(a,'#x'))
print(format(a,'#o'))

a=427

print(format(a,'#x'))
print(format(a,'#X'))
print(format(a,'b'))
print(format(a,'#b'))# new




print(format(b,'f'))
print(format(b,'.2f'))
print(format(b,'10.2f'))
print(format(b,'#<10.2f'))#work!!!
print(format(b,'#10.2E'))
print(format(b,'x<10.2e'))
print(format(b,'10,.2f'))#12,234.68 千位符號


print(format(c,'10s'))
print(format(c,'@<10s'))
print(format(c,'#>10s'))
print(format(c,'*^16s'))  #置中 前導字元


