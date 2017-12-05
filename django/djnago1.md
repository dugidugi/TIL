# 장고첫앱 - 장고와 MTV

## MTV
- 순서 : HTTP -> urls -> View -> Template 이랑 Model로 각각 -> View -> HTTP 
- 주의) MVC의 View는 장고의 View와 다른 역할.
- ![이런 구조](https://www.inflearn.com/wp-content/uploads/django_mtv-1024x768.png)

# 프로젝트 및 앱 생성

## 1 가상환경 설정, 시작 (terminal)
~~~
virtualenv myvenv
source mevenv/bin/activate
pip install django
~~~

## 2 프로젝트 생성 (terminal)
~~~
django-admin startproject myproj1
~~~

## 3 setting바꾸기 (settings.py)
~~~
LANGUAGE_CODE = 'ko-kr'
timezone = ‘Asia/Seoul’
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
~~~

## 4 앱 시작하기 (terminal)
~~~
python manage.py startapp lotto
~~~
## 5 등록해주기 (settings.py)
~~~
INSTALLED_APPS = []에 추가하기
	'lotto'
~~~
## 6 서버 시작
~~~
python manage.py runserver
~~~


# urls.py / views 수정

## urls.py수정 (urls.py) 
- *장고 ver2임
- 그냥 기본 url일 때, 
- views의 index 매소드를 실행해라
~~~
from lotto import views
~~~
~~~	
urlpatterns = [] 안에 추가
	path('', views.index),
~~~
	
## views 수정 (views.py)
- 위에 urls에서 import라고 써 놓았는데 view가 없으니까. view 만들어줘야지
- index 매소드는 h1태그안에 Http response를 한다
~~~
from django.http import HttpResponse
def index(request):
	return HttpResponse('<h1>Hello World</h1>')
~~~



# Model 클래스 만들기

- 장고는 모델-데이터베이스를 연결해서 데이터베이스에 영구적으로 데이터 저장함
- Object - Relational Mapping [ORM] 이라고함.

## model class / 매소드 만들기 (models.py)
~~~
class GuessNumbers(models.Model): 
	name = models.CharField(max_length= 24)
	lottos = models.CharField(max_length=255, default = '[1,2,3,4,5,6')
	text = models.CharField(max_length = 255)
	num_lotto = models.IntegerField(default = 5) 
	update_date = models.DateTimeField()
~~~
- model class 만들기
- db에서 column 같은 것 만드는 것

~~~
	def generate(self):
		self.lottos = ""
		origin = list(range(1,46))
		for _ in range(0, self.num_lotto):
			random.shuffle(origin)
			guess = origin[:6]
			guess.sort()
			self.lottos += str(guess) +'\n'
		self.update_date = timezone.now()
		self.save() 
~~~
- 매소드 : 실행할 수 있는 것 만든다
- self.save() : DB에 반영한다 

## db에 반영하기 (terminal)
~~~
python manage.py makemigration
#마이그레이션을 준비해라
python manage.py migrate
#제 db에 반영을 해라
~~~


# admin site에 model 등록하기 

## superuser 만들기 (terminal)
python manage.py createsuperuser

## admin (admin.py)
~~~
from .models import GuessNumbers
admin.site.register(GuessNumbers)
~~~
. : 같은 디렉토리 
models에서 import하기 .py 생략가능

register에 매소드 GuessNumbers 넣기

이렇게 하고 admin가서 Guessnumbers 하나 만들어줍니다

## model에서 설명 (models.py)
admin페이지에 name, text 보이도록만들기 
class Generate 밑에 다른 매서드 만들기 : 오버라이
~~~
def __str__(self):
	return "%s %s" % (self.name, self.text)
~~~

오버라이딩 : 서브클래스가 자신의 부모클래시들 중에 의해 이미 제공된 메소드를 특정한 형태로 구현하는 것





