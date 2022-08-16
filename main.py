from func import *
from case_1 import *
url = 'https://www.vpin.club/main?sort=date'
wd = webdriver.Chrome()
wd.get(url)

driver_wait(wd,30,'main-style')

print('OK')
wd.quit()