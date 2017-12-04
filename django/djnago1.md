#장고첫앱 - 장고와 MTV

##MTV
순서 : HTTP -> urls -> View -> Template 이랑 Model로 각각 -> View -> HTTP 
주의) MVC의 View는 장고의 View와 다른 역할.

#프로젝트 및 앱 생성

##1 가상환경 설정, 시작 (terminal)
	virtualenv myvenv
	source mevenv/bin/activate
	pip install django

##2 프로젝트 생성 (terminal)
	django-admin startproject myproj1

##3 setting바꾸기 (settings.py)
	LANGUAGE_CODE = 'ko-kr'
	timezone = ‘Asia/Seoul’
	STATIC_ROOT = os.path.join(BASE_DIR, 'static')

##4 앱 시작하기 (terminal)
	python manage.py startapp lotto

##5 등록해주기 (settings.py)
INSTALLED_APPS = []에 추가하기
	'lotto'

##6 서버 시작
	python manage.py runserver


#urls.py / views 수정

##urls.py수정 (urls.py) 
	from lotto import views
	
urlpatterns = [] 안에 추가
	path('', views.index),
*장고 ver2임
그냥 기본 url일 때, 
views의 index 매소드를 실행해라

##views 수정
위에 urls에서 import라고 써 놓았는데 view가 없으니까. view 만들어줘야지
	
	from django.http import HttpResponse

	def index(request):
		return HttpResponse('<h1>Hello World</h1>')

index 매소드는 h1태그안에 Http response를 한다





