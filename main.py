import requests
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
option = webdriver.ChromeOptions()
# option.add_argument('--headless')
driver = webdriver.Chrome(executable_path=r'C:\Users\Admin\Downloads\chromedriver.exe',options=option)
driver.get('https://spys.one/en/anonymous-proxy-list/')
sleep(3)
driver.find_element_by_xpath("//*[@id='xpp']/option["+str(6)+"]").click()
sleep(3)
open('proxy.txt','w').write('')
for i in range(3,503):
    xpath  = driver.find_element_by_xpath(f'//tbody/tr[{i}]/td[1]/font[1]')
    with open('proxy.txt','a') as file:
        file.write(xpath.text + '\n')
print('done')
driver.quit()
