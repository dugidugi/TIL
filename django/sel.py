from selenium import webdriver

#크롬 드라이버 위치 지정 
driver = webdriver.Chrome('/Users/yooduckhwang/TIL/selenium_crawl/chromedriver')

url = 'https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/'
driver.get(url)

