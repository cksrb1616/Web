# chrome://version   or   setting
# download chrome driver
# pip install selenium

import time
from selenium import webdriver

browser = webdriver.Chrome("/Users/minjunchoi/Documents/GitHub/Web/selenium/chromedriver") # "./chromedriver.exe" ./는 현재폴더에 있다는 것을 의미. 같은 경로에 있으면 공란으로 둬도 됨

# 1. 네이버 이동
browser.get("http://naver.com")
# browser.back()
# browser.forward()
# browser.refresh()

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 2-1. to send key (like Enter)
# from selenium.webdriver.common.keys import Keys
# elem.send_keys("stock")
# elem.send_keys(Keys.ENTER)

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

# 5. id 를 새로 입력
#browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
#browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저 종료