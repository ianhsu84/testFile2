from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def driver_wait(webdriver,wait_sec,target_id):
    WebDriverWait(webdriver,wait_sec).until(expected_conditions.presence_of_element_located((By.ID,target_id)))

def open_webdriver(url):
    return webdriver.Chrome().get(url)

## find element here
def find_element_by_id(webdriver,target_id):
    return webdriver.find_element(By.ID,target_id)

def find_element_by_class_name(webdriver,target_class_name):
    return webdriver.find_element(By.CLASS_NAME,target_class_name)

def find_element_by_linktext(webdriver,target_linktext):
    return webdriver.find_element(By.LINK_TEXT,target_linktext)

def find_element_by_css_selector(webdriver,target_css_selector):
    return webdriver.find_element(By.CSS_SELECTOR,target_css_selector)



