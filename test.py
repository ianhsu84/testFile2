from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pyautogui
import time

def driver_init(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.set_window_size(1200,800)
    driver.set_window_position(0,0)
    return driver

def find_element_by_id(webdriver,target_id):
    return webdriver.find_element(By.ID,target_id)

def driver_wait_by_id(webdriver,wait_sec,target_id):
    WebDriverWait(webdriver,wait_sec).until(expected_conditions.presence_of_element_located((By.ID,target_id)))

def driver_wait_by_class_name(webdriver,wait_sec,target_class_name):
    WebDriverWait(webdriver,wait_sec).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,target_class_name)))

def search_click(webdriver):
    driver_wait_by_id(webdriver,20,'header-search')
    time.sleep(1)
    find_element_by_id(webdriver,'header-search').click()

#if __name__== '__main__':
url = 'https://www.vpin.club/main?sort=date'
wd = driver_init(url)
driver_wait_by_class_name(wd,30,'main-style')
print('driver init OK')

search_click(webdriver)
print('search ok')