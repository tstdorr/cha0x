#coding=utf-8                                                                                                                                                                              
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)
fopen=open('~/Documents/prjcts/f1rst/URLss.txt','r')
for x in fopen.readLines():
    URL = x.strip('\n')
    driver.get(URL)

    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
    driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')
    driver.quit()
