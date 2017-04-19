#spider

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