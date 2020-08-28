# 假设通过爬虫你获取了北京2016年3，10月份每天的白天最高气温（分别是列表a,b)，绘制气温随时间的变化规律
# a=[11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22.22,23]
# b=[26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc",size=8)
my_font2=font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc",size=15)

y_3=[11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10=[26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]
x_3=range(1,32)
x_10=range(51,82)

plt.figure(figsize=(20,8),dpi=80)

#使用scatter绘制散点图，是和折线图唯一区别
plt.scatter(x_3,y_3,label="3月份")
plt.scatter(x_10,y_10,label="10月份")

#调整x轴的刻度
_x=list(x_3)+list(x_10)
_xtick_labels=["3月{}日".format(i) for i in x_3]
_xtick_labels+=["10月{}日".format(i-50) for i in x_10]
plt.xticks(_x[::3],_xtick_labels[::3],FontProperties=my_font,rotation=45)

#添加图例
plt.legend(loc="upper right",prop=my_font2)

#添加描述信息
plt.xlabel("时间",fontproperties=my_font2)
plt.ylabel("温度",fontproperties=my_font2)
plt.title("标题",fontproperties=my_font2)

#展示
plt.show()