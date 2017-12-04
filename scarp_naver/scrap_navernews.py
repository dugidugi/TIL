#-*- coding: utf-8 -*-
#한글 때무네 오려나면 이렇게 

from bs4 import BeautifulSoup
import requests
import datetime


##### 리컬션으로 날짜 목록 만들기
start_date = datetime.date(2017, 3, 1)
end_date = datetime.date(2017,3,20)

dates = []

def countdate(start_date):
	if start_date==end_date:
		dates.append(end_date.isoformat())
	else:
		# print(start_date)
		dates.append(start_date.isoformat()) 
		countdate(start_date + datetime.timedelta(days=1))

countdate(start_date)
print(dates)


#####
for date in dates:
	url = 'http://news.naver.com/main/history/mainnews/index.nhn?date=' + str(date) + '&time=21:00'

	html = requests.get(url).text

	soup = BeautifulSoup(html, 'html.parser')

	pars = soup.find_all('div', class_ ='newsnow_tx_inner')

	for par in pars:
		print(par.text)




