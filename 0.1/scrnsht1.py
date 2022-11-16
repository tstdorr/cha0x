#coding=utf-8                                                                                                                                                                              
import time
import sys
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager # Code 2


#binary = FirefoxBinary('/usr/lib/firefox/firefox')
#driver = webdriver.Firefox(firefox_binary=binary)
options = Options()
options.binary_location = r'/usr/lib/firefox/firefox'
options.headless = True
#driver = webdriver.Firefox(executable_path='./usr/bin/geckodriver', options=options)
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options = options) # Code 3
#driver = webdriver.Firefox(executable_path='./usr/bin/geckodriver', firefox_options=options)
fopen=open('/home/Arch0/Documents/prjcts/f1rst/URLs.txt','r')
for x in fopen.readlines():
    URL = x.strip('\n')
    driver.get(URL)

    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
    driver.save_screenshot('%s.png' %URL)
    #driver.find_element_by_tag_name('body').screenshot('%s.png' %URL)
driver.quit()
