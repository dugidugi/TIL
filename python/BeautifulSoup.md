# BeautifulSoup 
### HTML을 수정하여 쉽게 탐색할 수 있는 xml형식의 파이썬 객체로 변환시켜줌

## 라이브러리 불러오ㄱ

	from urllib.request import urlopen
	#urllib 라이브러이 - request모듈에서 urlopen명령어를 가져온다
	from bs4 import BeautifulSoup


html로 읽어온 html저장
	html = urlopen("http://www.pythonscraping.com/pages/page1.html") 
BeautifulSoup로 파이썬 객체로 변환
	bsObj = BeautifulSoup(html.read(), "html.parser")


## 접근하기

	bsObj.head : head태그 읽기
	bsObj.h1 : h1태그 읽기

	find(tag, attribute, recursive , text, keywords)
	findAll(tag, attribute, recursive , text, limit, keywords)

	bsObj.findAll("span", {"class" : "red"})
	이런식으로 사용한다

	.get_text() : 태그를 제외한 text만 읽어온다


## for loop으로 가져오기
IMDB에서 영화 목록 가져오기
	html4 = urlopen("http://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm_8")
	movies = BeautifulSoup(html4, "html.parser")

	for movie in movies.findAll("td", {"class" : "titleColumn"}) :
    print(movie.a.get_text())