a = 123
b = 12345.6789
c = 'python'
print('%d' % a )
print('%5d' % a )#將A 用空白補足五位數(又靠
print('%2d' % a )
print('%-5d' % a )# 負數 ,向左靠 不代表負數
print('%05d' % a )# 用0 補足五位數
print('%+5d' % a )# +符號


a =427
print('%x'%a)
print('%#X'%a)#能把文字print出則不分大小寫
print('%#x'%a)
print('%#o'%a)

print('%f'%b)#預設六位小數點
print('%.2f'%b)#2位數
print('%10.2f'%b)#總共要十位數(包含小數點)
print('%-10.2f'%b)#總共要十位數(包含小數點)靠左
print('%e'%b)#能把文字print出則不分大小寫
print('%E'%b)
print('%.2E'%b)
print('%10.2E'%b)
print('%.2f%%'%b)#加%符號

print('%s'%c)
print('%10s'%c)
print('%-10s'%c)
print('%r'%c)#字串用加'   '
print('%r'%b)
print('%r'%a)

