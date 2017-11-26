import datetime

start_date = datetime.date(2017,10,11)
end_date = datetime.date(2017,10,31)

dates = []

def datecount(start_date):
	if start_date == end_date:
		dates.append(end_date.isoformat())
		# print(end_date)
		print('stop')
	else:
		# print(start_date)
		dates.append(start_date.isoformat())
		datecount(start_date + datetime.timedelta(days=1))

datecount(start_date)

print(dates)