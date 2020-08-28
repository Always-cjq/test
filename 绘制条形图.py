# 假设你获取2017年内地电影票房前20（列表a）和电影票房数据（列表b）
# a=["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5","最后的骑士","摔跤吧爸爸","加勒比海盗5","金刚","极限特工","战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5","最后的骑士","摔跤吧爸爸","加勒比海盗5","金刚","极限特工"]
# b=[56,29,53,16,15,12,96,11,8,11,61,11,28,11,12,10,49,10,3,8]

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

a=["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5\n:最后的骑士","最后的骑士","摔跤吧爸爸","加勒比海盗5\n：终极之战","金刚","极限特工","战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5","最后的骑士","摔跤吧爸爸","加勒比海盗5","金刚","极限特工"]
b=[56,29,53,16,15,12,96,11,8,11,61,11,28,11,12,10,49,10,3,8]

plt.figure(figsize=(20,8),dpi=80)

plt.bar(range(len(a)),b,width=0.3)

plt.xticks(range(len(a)),a,FontProperties=my_font,rotation=90)

plt.savefig("./movie.png")

plt.show()