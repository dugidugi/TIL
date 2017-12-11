from selenium import webdriver
from bs4 import BeautifulSoup
#셀레늄 드라이버 위치찾기
driver = webdriver.Chrome('/Users/yooduckhwang/TIL/crawl/chromedriver')

url = 'https://nid.naver.com/nidlogin.login?url=http%3A%2F%2Fmail.naver.com%2F'

#url 열기
driver.get(url)



# driver.find_element_by_id('id').send_keys('robert92')
# driver.find_element_by_id('pw').send_keys('dbejrgn10')

# driver.find_element_by_class_name('btn_global').click()

# driver.implicitly_wait(4)

# #현재 창에 있는 page_source 전부 저장하기
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')

# titles = soup.find_all(class_ = 'subject ')

# for title in titles:
# 	print(title.text)
