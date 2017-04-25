
# tutorial spider

scrapy는 그냥 bs처럼 import해서 사용하는게 아니라
project를 만들고 돌림. 그래서 project를 만들면 하위 폴더와 파일들이 생김. 좀 생소하다

순서는 대략 이렇다
1. Scrapy 프로젝트 만들기
2. Spider 작성
3. command line으로 데이터 내보내기
4. Changing spider to recursively follow links

5. Using spider arguments

4,5번 뭐라고..?


## 프로젝트 만들기
Terminal 열고
	scrapy startproject projectName

그럼 이렇게 파일이 생성됨

	projectName/
    	scrapy.cfg            # deploy configuration file

	    tutorial/             # 프로젝트의 파이썬 모듈, 여기서 코드불러옴
	        __init__.py

	        items.py          # 원하는 부분을 파일로 저장할 때 

	        pipelines.py      # 결과물을 파일로 저장할 때 

	        settings.py       # 설

	        spiders/          # 다음에 spiders를 놓을 공간
          		__init__.py



# Basic 컨셉

command line tool 
Spiders : 웹사이트 크롤 하는 규칙
Selectors : XPath로 웹페이지에서 데이터 추출
Scrapy shell : 인터렉티브 환경에서 코드 테스트
Items : 스크랩하고 싶은 데이터 정의
Item Pipline : 후 과정 & 스크랩한 데이터 저장하기
Feed exports : 다른 포맷으로 다른 위치에 저장하기
Request and Responses : Understand the classes used to represent HTTP requests and responses. 무슨말??
Link Extractors : 링크를 추출하기 위한 편리한 클래스 
Settings : 설정
Exceptions : 예외사항

# 내장 기능들
Logging : 로깅
Stats Collection : 크롤러의 통계수치 수집
Sending e-mail : 어떤 이벤트가 발생하면 이메일 보내기
Telnet Console : 돌고있는 크롤러를 파이썬 콘솔로 검사하기
Web Service : 웹서비스로 크롤러 모니터하고 조종하기