
	.shape : 데이터 형태 보기

	np.array(--) : array만들기

	np.zeros : 0으로된 array 만들기
	np.ones : 1로된 array 만들기
	np.arrange(15) : 1~15 array만들기


	.dtype : data type 살펴보기

## 데이터형

> int : 정수
> float : 실수
> complex : 복소수
> bool : 불리언 
> object 
> string_
> unicode_ : 유니코드 문자열 

## Array 인덱싱 이해하기

	data[2,4]
	#3번째 행 / 5번째 열
	
	data[:] 
	#모든 행렬

	data[2:5, 3]
	#3~5행 / 4열


	names = np.array(["a", "b", "c", "d"])
	data[names == "name"]
	#불리언으로도 인덱싱 가능

	data[names == "a" | names =="b"]
	#or 조건을 넣어서 인덱싱





