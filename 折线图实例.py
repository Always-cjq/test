import random

from matplotlib import font_manager  # 另一个推荐的设置字体的方式，也不用记，找注释Ctrl+b
from matplotlib import pyplot as plt  # matplotlib默认中文不显示

'''
windows和linux设置字体的方式
font={'family':'Microwsoft YaHei',
       'weight':'bold',
       'size':'11'}
matplotlib.rc('font',**font)
matplotlib.rc('font',family='MicroSoft YaHei',weight='bold')
'''
#另外一种实例化字体的方式
my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\simsun.ttc",size=11.5)#实例化一个字体，还没完

x=range(0,120)
y=[random.randint(20,35) for i in range(120)]

plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

#调整x轴的对象
_x=list(x)#只有转化成列表的时候才可以[]取步长
_xtick_labels=["10点{}分".format(i) for i in range(60)]
_xtick_labels+=["11点{}分".format(i) for i in range(60)]
#取步长，数字和字符串一一对应，数据的长度一样
plt.xticks(_x[::3],_xtick_labels[::3],rotation=45,FontProperties=my_font)#rotation旋转的角度<实例化my_font后用的时候还要添加一个参数，叫做

#添加描述信息(同样是中文无法显示要加入实例化对象）
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度 单位(℃)",fontproperties=my_font)
plt.title("10点到12点每分钟温度变化的结果",fontproperties=my_font)

plt.show()