# import sys
# import time
# from collections import deque
#
# fancy_loading = deque('>--------------------')
#
# while True:
#     print ('\r%s' % ''.join(fancy_loading),
#     fancy_loading.rotate(1))
#     sys.stdout.flush()
#     time.sleep(0.08)
#
# # Result:
#
# # 一个无尽循环的跑马灯

import requests


from lxml import html

url='https://movie.douban.com/' #需要爬数据的网址
page=requests.Session().get(url)
tree=html.fromstring(page.text)
result=tree.xpath('//td[@class="title"]//a/text()') #获取需要的数据
