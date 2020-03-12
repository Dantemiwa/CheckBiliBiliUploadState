import re ##此处使用的编辑器是python3.x 
from matplotlib import pyplot as plt 
from matplotlib import animation
import time
import datetime
#import seaborn as sns  # 美化图形的一个绘图包

#sns.set_style("whitegrid")  # 设置图形主图
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2, 1.01*height, '%s' % int(height))


pattern="[\u4e00-\u9fa5]+"#中文正则表达式
patternTime = '\d+\S\d+\S\d+\s\d+\S\d+\S\d{2}'#匹配时间
f = open("upload.txt")#打开记录文件
l = []
criteria = ["阻塞"]#存储通道状态
point = [0]#记录对应状态出现的次数
timeList = []#时间列
statusList = []#中文状态列
pointList = []#数值状态列，2:阻塞 3：爆满
pointEmpty = 0#记录空值出现次数（比如网络突然断开而没有重连）
j = 1
k = 0
row = 1
for i in f:
      try:
        patternCri = re.findall(pattern,i)[0]#通过正则表达式匹配中文字符
        while(k<j):
          if re.match(patternCri,criteria[k]) != None:
            point[k] = point[k] + 1
            try:
              timeResult = re.findall(patternTime,i)#通过正则表达式匹配时间
              statusResult = re.findall(pattern,i)#通过正则表达式匹配状态
              timeList.append(timeResult)#存储时间
              statusList.append(patternCri)#存储状态
            except Exception as e:
              print(e)
            #time[row - 1] = i - 
            break
          else:#当前criteria与中文字符不匹配，更换criteria
            k = k + 1
            if k == j:
              criteria.append(patternCri)
              print(criteria)
              point.append(1)
              j = j + 1   
        k = 0          
      except Exception as e:#出现空值
        pointEmpty = pointEmpty + 1
        print(e)
      row = row + 1       
f.close()
print(point)
print(criteria)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
autolabel(plt.bar(range(len(point)), point, color='rgb', tick_label=criteria))#画出柱状图
plt.show()




for i in range(len(statusList)):
    if statusList[i] == '阻塞':
      pointList.append(2)
    elif statusList[i] == '爆满':
      pointList.append(3)          
print(timeList,pointList) 
tim = []
for d in timeList:
      tempStr = "".join(d)
      xs = datetime.datetime.strptime(tempStr, '%Y-%m-%d %H:%M:%S')
      tim.append(xs)

plt.ion() #开启interactive mode 成功的关键函数
plt.figure(figsize=(15,5))
t = []
m = []
t_now = 0

for i in range(len(tim)):#动画输出状态-时间曲线
 t_now = tim[i]
 t.append(t_now)#模拟数据增量流入
 m.append(pointList[i])#模拟数据增量流入
 plt.plot(t,m,'-r')
 plt.xlabel(tim[i])
 plt.ylabel("2:阻塞  3:爆满")
 plt.draw()#注意此函数需要调用
 plt.pause(0.001)

plt.figure(1)
plt.plot(tim,pointList,'-r')
plt.pause(100)#持续显示


'''
for k in range(len(tim)):
#  plt.figure(figsize=(15,5))
  plt.plot(tim[k],pointList[k])
  plt.pause(1)
  plt.cla()
 ''' 
'''
fig, ax = plt.subplots()
fig.set_tight_layout(True)

line, = ax.plot(tim  , pointList, 'r-', linewidth=2)


def animate(i):
    # 更新直线和x轴（用一个新的x轴的标签）。
    # 用元组（Tuple）的形式返回在这一帧要被重新绘图的物体
    
    line.set_ydata(pointList[i])  # 这里是重点，更新y轴的数据
    line.set_xdata(tim[i])
    ax.set_xlabel(tim[i])    # 这里是重点，更新x轴的标签
    return line, ax

ani = animation.FuncAnimation(fig,animate,frames=350,interval = 1,blit = False)
plt.show()
'''