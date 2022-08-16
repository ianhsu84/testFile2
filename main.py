from func import *
from case_1 import *
url = 'https://www.vpin.club/main?sort=date'
wd = driver_init(url)
driver_wait_by_class_name(wd,30,'main-style')

print('driver init OK')

run_case(wd)
#wd.quit()