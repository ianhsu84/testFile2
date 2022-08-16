from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pyautogui
import time
## webdriver here
def driver_init(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.set_window_size(1200,800)
    driver.set_window_position(0,0)
    return driver

def driver_wait_by_id(webdriver,wait_sec,target_id):
    WebDriverWait(webdriver,wait_sec).until(expected_conditions.presence_of_element_located((By.ID,target_id)))

def driver_wait_by_class_name(webdriver,wait_sec,target_class_name):
    WebDriverWait(webdriver,wait_sec).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,target_class_name)))

def driver_wait_by_css_selector(webdriver,wait_sec,target_css_selector):
    WebDriverWait(webdriver,wait_sec).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,target_css_selector)))

def driver_wait_by_name(webdriver,wait_sec,target_name):
    WebDriverWait(webdriver,wait_sec).until(expected_conditions.presence_of_element_located((By.NAME,target_name)))

## find element here
def find_element_by_id(webdriver,target_id):
    return webdriver.find_element(By.ID,target_id)

def find_element_by_class_name(webdriver,target_class_name):
    return webdriver.find_element(By.CLASS_NAME,target_class_name)

def find_element_by_name(webdriver,target_name):
    return webdriver.find_element(By.NAME,target_name)

def find_element_by_linktext(webdriver,target_linktext):
    return webdriver.find_element(By.LINK_TEXT,target_linktext)

def find_element_by_css_selector(webdriver,target_css_selector):  
    return webdriver.find_element(By.CSS_SELECTOR,target_css_selector)

## login here
def main_page_login(webdriver):  #在首頁點登入
    driver_wait_by_css_selector(webdriver,30,'#app > section > aside > div > div > div > div > div.side-footer > div.user-func > a')
    time.sleep(1)
    find_element_by_css_selector(webdriver,'#app > section > aside > div > div > div > div > div.side-footer > div.user-func > a').click()

def social_login_google(webdriver):  #登入頁點第三方登入
    #點google登入
    find_element_by_css_selector(webdriver,'#app > div > div.v-left > form > div:nth-child(2) > a.btn.v-btn-google').click()
    #點帳號輸入框並寫入帳號後繼續
    driver_wait_by_id(webdriver,20,'identifierId')
    time.sleep(1)
    find_element_by_id(webdriver,'identifierId').click()
    find_element_by_id(webdriver,'identifierId').send_keys(r'yiyanghsu@osparks.com')
    find_element_by_css_selector(webdriver,'#identifierNext > div > button > span').click()
    #點密碼輸入框並寫入密碼
    driver_wait_by_name(webdriver,20,'password')
    time.sleep(1)
    find_element_by_name(webdriver,'password').click()
    find_element_by_name(webdriver,'password').send_keys(r'vm3u4u;6841008')
    find_element_by_css_selector(webdriver,'#passwordNext > div > button > span').click()
## control here
def mouse_move_to_side_bar(): #移動滑鼠讓首頁左側的side bar跑出來
    pyautogui.moveTo(50,300)

## UI here
def search_bar_click(webdriver):
    driver_wait_by_id(webdriver,20,'header-search')
    time.sleep(1)
    find_element_by_id(webdriver,'header-search').click()

def search_bar_click_tag(webdriver):
    driver_wait_by_class_name(webdriver,20,'tag-el')
    time.sleep(1)
    find_element_by_class_name(webdriver,'tag-el').click()

def search_vpin_by_tag_unfollow_to_following(webdriver):
    driver_wait_by_class_name(webdriver,20,'unfollow')
    time.sleep(1)
    find_element_by_class_name(webdriver,'unfollow').click()

def search_vpin_by_tag_following_to_unfollow(webdriver):
    driver_wait_by_class_name(webdriver,20,'following')
    time.sleep(1)
    find_element_by_class_name(webdriver,'following').click()
