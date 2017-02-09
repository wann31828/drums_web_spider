from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os


starturl = 'http://www.looperman.com/loops?page=1&keys=drums&dir=d'


fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-msdos-program")

driver = webdriver.Firefox(firefox_profile=fp)

for i in range(13):
    cururl = starturl + str(i+1) + '/'
    driver.get(cururl)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.findAll("a", { "class" : "btn-download" })
    for div in divs:
        if div['href']:
            driver.get(div.a['href'])
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            targetdiv = soup.find('a', attrs={'class' : 'btn-download'})
            audio_url = targetdiv['href']
            titlediv = soup.find('a', attrs={'class' : 'player-title'})
            filename = titlediv.text
            save_file(audio_url,filename)



def save_file( url, file_name):  ##保存图片
        print('开始请求图片地址，过程会有点长...')
        file = request(url)
        print('开始保存图片')
        f = open(file_name, 'ab')
        f.write(file.content)
        print(file_name, '图片保存成功！')
        f.close()       
#elem = driver.find_element_by_class_name('btn-download')
#elem.click()

def request(url):  # 封装的requests 请求
        r = requests.get(url)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        return r        