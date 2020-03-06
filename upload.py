from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from lxml import etree
import time
# 通过find定位标签
# BeautifulSoup文档：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
def bs_parse_movies(html):
    movie_list = []
    soup = BeautifulSoup(html,'html.parser')
    print(soup.prettify());
    # 查找所有class属性为hd的div标签
    p_list = soup.find_all('div', class_='video-jam-state')
    # 获取每个div中的a中的span（第一个），并获取其文本
    for each in p_list:
        movie = each.a.span.text.strip()
        movie_list.append(movie)
 
    return movie_list

def get_movies():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        'Host': 'member.bilibili.com'
    }
 
    link = 'https://member.bilibili.com/video/upload.html'
    r = requests.get(link, timeout=10)
    r.encoding =  "utf-8";
    print("响应状态码:", r.status_code)
    
    if 200 != r.status_code:
        return None

    return bs_parse_movies(r.text)


driver = webdriver.Chrome()
url = 'https://member.bilibili.com/video/upload.html'
driver.get(url)
time.sleep(5)
print(driver.title)
i = 0
while(i < 1000):  
    i = i + 1
    try:  
        #print(driver.title)
        listing = driver.find_elements_by_class_name("video-jam-state")
        for k in range(len(listing)):
            print(listing[k].text)
    except:
        print("find nothing")   
    time.sleep(5)
   # driver.find_element_by_name("你的手机号").send_keys("18923296180")
   # driver.find_element_by_name("密码").send_keys("mia984299")
   # driver.find_element_by_class_name("btn-login").click()
   

#movies = get_movies()
#print(movies)