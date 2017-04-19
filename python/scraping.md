#설치하기
	pip install Scrapy
	pip install Selenium

	웹드라이버 다운로드
	https://sites.google.com/a/chromium.org/chromedriver/downloads

	다운받고 경로 알아놓기

# Scrapy 실행

터미널에서
	scrapy shell "url입력"
	#ipython으로 실행됨

	response.text : html코드 모두 가져옴

# selenium 실행

	from selenium import webdriver

	browser = webdriver.Chrome("/Users/yooduckhwang/chromedriver")

	browser.get("url입력")

	browser.quit()

# Scrapy구조

Spider 
: 어떤 웹사이트를 어떻게 크롤링 할 것인지
: 어떤 부분을 스크래핑 할 것인지

Selector
: 특성 html 요소를 선택할 수 있도록
: css 선택하거나 XPath를 사용할 수 있음

Item
: 원하는 부분을 스크랩하여 저장할 때 사용하는 사용자 정의 자료구조 클래스

Item Pipline
: 결물을 가공하거나 파일형태로 저장할 수 있도록 하는 클래스

Setting
: Spider, Item Pipline 등이 어떻게 동작하도록 할지에 대한 설정을 기재하는 파일
*robots.txt를 따를 것인가 말것인가도 결정

#Scrapy 해보기

	scrapy shell "url입력"

## xpath로 select


	response.xpath('')

	response.xpath('/text()')
	#text 부분만 가져오기

	response.xpath('/text()').extract()

	response.xpath('/text()').extract()[0]


### 변수 저장하기 
	titles = dddd

	title = titles[0]

	title.xpath('./~~~~~')






	