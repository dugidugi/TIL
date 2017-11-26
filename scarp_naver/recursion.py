#-*- coding: utf-8 -*-
import datetime

#기본 재귀함수 

# def countdown(n):
# 	if n==0:
# 		print('Stop')
# 	else:
# 		print(n)
# 		countdown(n-1)

# countdown(5)


#날짜로 재귀함수 만들어 보
start_date = datetime.date(2015, 3, 1)
end_date = datetime.date(2015,3,20)

dates = []

def countdate(start_date):
	if start_date==end_date:
		dates.append(end_date.isoformat())
	else:
		print(start_date)
		dates.append(start_date.isoformat()) 
		countdate(start_date + datetime.timedelta(days=1))

countdate(start_date)

print(dates)



