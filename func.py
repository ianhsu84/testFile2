from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def driver_wait(webdriver,wait_sec,target_id):
    WebDriverWait(webdriver,wait_sec).until(expected_conditions.presence_of_element_located(By.ID,target_id))

def open_webdriver(url):
    return webdriver.Chrome().get(url)
