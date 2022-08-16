from func import *

def run_case(webdriver):
    mouse_move_to_side_bar() #移動滑鼠
    main_page_login(webdriver) #跳轉到登入頁
    social_login_google(webdriver) # google第三方登入
    search_bar_click(webdriver) # 點search
    search_bar_click_tag(webdriver) # 點tag
    search_vpin_by_tag_unfollow_to_following(webdriver) # 點追蹤
    print('following ok')
    search_vpin_by_tag_following_to_unfollow(webdriver) # 點取消追蹤
    print('unfollow ok')
    mouse_move_to_side_bar()