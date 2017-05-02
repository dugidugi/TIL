판다스

series
dataframe

import numpy as mp
import pandas as pd

obj = pd.Series([2,4,5,6])

obj
인덱스, 값 같이 표시

obj.values
값만 표시

obj.index
인덱스만

obj.dtypes
데이터형 확인

#인덱스 같이 입력할 수 있음
obj2 = pd.Series([2,4,5,6], index = ['a', 'b', 'c', 'd'])

#딕셔너리를 시리즈로 변환할 수 있음
sdata = {'Chales' : 3500, 'kiho' : 3000}
obj3 = pd.Series(sdata)

#name과 인덱스 네임
obj3.name = 'Salary'
obj3.index.name = 'Names'
obj3 

#인덱스는 이렇게 바꿔준다 
obj3.index = ['A', 'B'] 


#dataframe 만들기
pd.DataFrame(변수)

data = {
	"name" : ["ka", "ta", "ba", "ru", "mu"],
	"year" : [2012, 2009, 2008, 2015, 2017],
	"points" : [1.3, 2.7, 5.3, 8.2, 9.0]
}

pf = pd.DataFrame(data)

df.index 

df.columns

df.values

df.index.name = "ddd"
df.columns.name = "info"

#새로운 칼럼만들기 
df2 =pd.DataFrame(data, colums=["year", "name", "points", "penalty"],
index = ["one", "two", "three", "four", "five"])

df2.index
df2.columns
df2.values

.discribe()
df2.describe()
평균 최대 최소 값등을 보여줌. 





