# 假设你获取2017年内地电影票房前20（列表a）和电影票房数据（列表b）
# a=["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5","最后的骑士","摔跤吧爸爸","加勒比海盗5","金刚","极限特工","战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5","最后的骑士","摔跤吧爸爸","加勒比海盗5","金刚","极限特工"]
# b=[56,29,53,16,15,12,96,11,8,11,61,11,28,11,12,10,49,10,3,8]
# 绘制横着的条形图

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

a=["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5:最后的骑士","最后的骑士","摔跤吧爸爸","加勒比海盗5：终极之战","金刚","极限特工","战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5","最后的骑士","摔跤吧爸爸","加勒比海盗5","金刚","极限特工"]
b=[56,29,53,16,15,12,96,11,8,11,61,11,28,11,12,10,49,10,3,8]

plt.figure(figsize=(20,8),dpi=80)

plt.barh(range(len(a)),b,height=0.3,color="orange")#bar()是竖着条形图，条宽用width，barh是横着的,用height(查看源码)

plt.yticks(range(len(a)),a,FontProperties=my_font)

plt.grid(alpha=0.2)

plt.savefig("./movie.png")

plt.show()