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
class Generate 밑에 다른 매서드 만들기 : 오버라이ㄷ

~~~
def __str__(self):
	return "%s %s" % (self.name, self.text)
~~~

오버라이딩 : 서브클래스가 자신의 부모클래시들 중에 의해 이미 제공된 메소드를 특정한 형태로 구현하는 것



# 장고 test코드 작성
generate 매소드 테스트 하기.

test는 테스트용 db를 만들었다가 완료후 디비를 삭제한다

## tests.py 이용하기(tests.py)
~~~
from django.test import TestCase
from .models import GuessNumbers

class GuessNumbersTestCase(TestCase):
	def test_generate(self):
		g = GuessNumbers(name='apple', text='pineapple')
		g.generate() #실제 generate 매소드 써보기
		print(g.update_date) 
		print(g.lottos)
		self.assertTrue(len(g.lottos) > 20) #assert : 테스트할 때 쓰임
~~~

## tests.py 실행하기(terminal)
~~~
python manage.py test #테스트 코드 실행하기
~~~


# views와 template 연동

## urls.py 수정하기(views.py)
~~~
path('lotto/', views.index, name = 'index'),
~~~

## template 만들기 (lotto/templates/lotto/default.html)
lotto/templates/lotto/default.html 만든다
app안에 templates폴더 만들고 그안에 또 app이름 이랑 똑같이 폴더 만들어준다

~~~
<!DOCTYPE html>
<html lang="ko">
<head>
  <title>My Little Lotto</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
  <link href="//fonts.googleapis.com/css?family=Space+Mono" rel="stylesheet">
</head>

<body>
  <div class="page-header">
  <h1>My Lotto Page</h1>
  </div>
  <div class="container lotto">
    <h2>당첨 기원 (2)</h2>
    <p> last update:2000/1/1</p>
    <p> 1, 10, 15, 20, 30 </p>
  </div>
</body>
</html>
~~~

## static 파일 연동(/lotto/static/css/lotto.css)
lotto/static/css/lotto.css

~~~
.page-header {
    background-color: #652596;
    margin-top: 0;
    padding: 20px 20px 20px 40px;
    font-family: 'Space Mono', monospace;
}

.page-header h1 {
  color: #FFFFFF;
}

.container {
  font-family: 'Space Mono', monospace;
}

.container h2 {
  color: #b9f442;
}
~~~

## static-html 연결하기 (lotto/templates/lotto/default.html)
head에 추가하기

~~~ 
{% load staticfiles %}
<link rel=”stylesheet” href=”{% static ‘css/lotto.css’ %}”>
~~~

## static 파일 수집 명령 (terminal)
~~~
python manage.py collectstatic
~~~



# shell을 이용한 장고 관리 (terminal)
~~~
python manage.py shell
~~~

~~~ 
from lotto.models import GuessNumbers
from django.utils import timezone

GuessNumbers.objects.all() #전체 리스트 보기
Guessnumbers.objects.get(name = 'dugi') #name이 dugi 인 것만 보기

g = Guessnumbers.objects.get(name = 'dugi')
g.name

g.update_date #현재 날짜로 변경
g.lottos #default 값이 들어있음

g.generate() #로또 생성 매소드 실행
g.lottos #확인해보자

g.save() #저장저장


##필터 기능
Guessnumbers.objects.filter(name__contains= 'a') #name에 'a'가 포함된 object 리스트들보여줌
a = Guessnumbers.objects.filter(name__contains= 'a')

a[0]
a[1] #이런 식으로확인 가능
~~~


# MYV 연동하기

## 그냥 urls.py 추가해주기
index 오류 나면 그냥 그러니까
~~~ 
path('', views.index, name = 'index')
~~~

## views 수정
~~~
from .models import GuessNumbers

def index(request):
	lottos = GuessNumbers.objects.all()
	return render(request, "lotto/default.html", {"lottos":lottos}) 
	#request온 것을 default.html로 보낸다.
	#{} 안에서 object 보내줄 수 있음 

~~~

## default.html 수정
for loop돌면서 lottos objects 나열하기
~~~
<div class="container lotto">
  {% for lotto in lottos%}
  <h2>{{lotto.text}}</h2>
  <p> last update: {{lotto.update_date}} by {{lotto.name}}</p>
  <p> {{lotto.lottos|linebreaksbr}}</p>
  {% endfor %}
~~~

# form 만들기
데이터 입력 받는 폼 

##form.py 작성(app_name/form.py)
앱 폴더 안에 form.py 파일 일단 만들어주고 
django자체에 forms기능이 있음
~~~
from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm):

	class Meta:
		model = GuessNumbers
		fields = ('name', 'text',) #name, text를 입력받는다. 나머지는 dafualt

~~~

## url 추가하기 (urls.py)
~~~
path('lotto/new', views.post, name = 'new_lotto'),
~~~

## views 수정 (views.py)
~~~
from .form import PostForm

def post(request):
	form = PostForm()
	return render(request, 'lotto/form.html', {"form": form})
~~~

## template 수정 (form.html)
form.html 만들어주고
~~~
<!DOCTYPE html> {% load staticfiles %}
<html lang="ko">
 <head>
  <title>My Little Lotto</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
  <link href="//fonts.googleapis.com/css?family=Space+Mono" rel="stylesheet">
  <link rel="stylesheet" href="{% static 'css/lotto.css' %}"> 
 </head>
 <body>
  <div class="page-header">
   <h1>My Little New Lotto</h1>
  </div>
  <div class="container lotto">
   <form method="POST" class="post-form"> {%csrf_token%} {{form.as_p}} <button type="submit" class="save btn btn-default">Save</button> </form>
  </div>
 </body>
</html>
~~~

# POST 처리


# 앱 다듬기 



