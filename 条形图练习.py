# 假设列表a中电影分别在2017-09-14(b_14),2017-09-15(b_15)，2017-09-16(b-16)三天的票房
# a=["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠:英雄归来","战狼2"]
# b_16=[15746,312,4497,319]
# b_15=[12357,156,2045,168]
# b_14=[2358,399,2358,362]

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

a=["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠:英雄归来","战狼2"]
b_16=[15746,312,4497,319]
b_15=[12357,156,2045,168]
b_14=[2358,399,2358,362]

#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

bar_width=0.2

x_14=list(range(len(a)))
x_15=[i+bar_width for i in x_14]
x_16=[i+bar_width*2 for i in x_14]

plt.bar(x_14,b_14,width=bar_width,label="9月14日")
plt.bar(x_15,b_15,width=bar_width,label="9月15日")
plt.bar(x_16,b_16,width=bar_width,label="9月16日")

#设置图例
plt.legend(loc="upper right",prop=my_font)

#设置x轴刻度
plt.xticks(x_15,a,FontProperties=my_font)

plt.show()