# 检测B站审核状态，并进行数据分析
本python项目用于检测B站的审核状态

### B站的审核状态没有找到相应的api，其审核状态是用vue写的，无法直接通过request读取。
### 方便起见，用了selenium模块直接读取元素
### 此处我用的是chromedriver.exe，如果没有谷歌浏览器的，请到百度查找相应浏览器的webdriver,或者直接下载一个最新版的chrome浏览器

#### shift+右键打开powershell，并键入
```python
pythonw upload.pyw 1>stdout.txt 2>stderr.txt
```

#### 此时程序进入后台运行，并弹出Chrome浏览器界面，登录以后，就可以正常地开始读取B站审核状态了
#### 程序根目录下会产生一个upload.txt,里面就存储了当前时间和当前审核状态
#### 在使用过程中请勿关闭chromedriver.exe以及浏览器

#### shift+y右键打开powershell,并输入
```python
python data_analysis.py
```

#### 将画出当前bilibili各种状态出现的次数
#### 程序默认每10分钟运行一次，如果想要修改，请修改upload.pyw中的第55行：
```python
timer = threading.Timer(600, up.GetUploadStatusFromBiliBili)#600s定时运行
```
#### 以及第57行
```python
 time.sleep(590)#休眠590s
```
### 具体内容可见B站:
<video id="video" controls="" preload="none" poster="http://om2bks7xs.bkt.clouddn.com/2017-08-26-Markdown-Advance-Video.jpg">
      <source id="mp4" src="https://www.bilibili.com/video/av95553466/" type="video/mp4">
      </video>
