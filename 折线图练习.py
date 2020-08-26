#练习
# 假设大家在30岁的时候，根据自己的实际情况，统计出来从11岁到30岁每年交朋友的数量列表a，请绘制出该数据的折线图
# a=[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
# b=[1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
# 要求：
#     y轴表示个数
#     x轴表示岁数，比如11岁，12岁

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\simsun.ttc")

y_1=[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_2=[1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
x=range(11,31)

#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y_1,label="自己",color="orange",linestyle=":")#颜色可以用16进制写，百度上找颜色代码
plt.plot(x,y_2,label="同桌",color="cyan",linestyle="-.")

#设置x轴刻度
_xtick_lables=["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_lables,FontProperties=my_font)
plt.yticks(range(0,9))

#绘制网格
plt.grid(alpha=0.4,linestyle="--",color="#8E236B")

#添加图例
plt.legend(prop=my_font,loc="upper left")#只有在legend()里面用prop，其他地方都是fontproperties,看源码

plt.show()
