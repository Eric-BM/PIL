import requests
import random
import time 
import datetime
from datetime import timedelta
import sys
import os
import socket
import struct
import re
import docx
from urllib.request import urlretrieve
import cv2
import xlrd 
import openpyxl
from selenium import webdriver
import numpy as np

def ScreenShot():
    driver.execute_script("document.body.style.zoom='0.5'")
    PIC = driver.find_element_by_xpath("""//*[@id="app"]/div/div[2]/div[1]/div[1]/div[1]/div[1]""")
    driver.execute_script("arguments[0].scrollIntoView();", PIC)
    driver.save_screenshot(txtPath+'\\screenshot\\'+ AuthorName + '.png')
    driver.quit()
def AuthorName():
    B = driver.execute_script("""
    b = document.getElementsByClassName("name-detail")
    return [b[0].innerText]
    """)
    global AuthorName
    AuthorName = B[0]

KOLLinkLists = []
txtPath = sys.path[0]
data = xlrd.open_workbook(r"C:\Users\1243712.JABIL\Desktop\Work\codes\PIL\1.xlsx", encoding_override='utf-8')
rsheet = data.sheet_by_name("Sheet1")
for row in rsheet.get_rows():
    product_column = row[12]  
    product_value = product_column.value  
    if product_value !="":
        KOLLinkLists.append(product_value)

for KOLLinkList in KOLLinkLists:
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu')
    options.add_argument('lang=zh_CN.UTF-8')
    options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"')

    driver= webdriver.Chrome(chrome_options=options)

    Url_Short = KOLLinkList
    Url_Long = (requests.head(Url_Short, stream=True)).headers['Location']
    driver.get(Url_Long)
    time.sleep(random.randint(10,11)) 
    B = driver.execute_script("""
    b = document.getElementsByClassName("name-detail")
    return [b[0].innerText]
    """)
    AuthorName = B[0]
    
    ScreenShot()
    


