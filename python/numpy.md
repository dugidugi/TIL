
## 기본 명령어
	.shape : 데이터 형태 보기
	.dtype : data type 살펴보기
	(numpy는 아니지만)

	np.array(--) : array만들기

	np.zeros : 0으로된 array 만들기
	np.ones : 1로된 array 만들기
	np.arrange(1,10) : 1-10 array만들기

## 데이터형

	int : 정수
	float : 실수
	complex : 복소수
	bool : 불리언 
	object 
	string_
	unicode_ : 유니코드 문자열 

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

## array 관련 함수

	abs : 절대값
	sqrt : 제곱근 (**0.5 결과와 동일)
	square : 제곱 계산
	exp : 무리수 e 
	log, log10, log2 
	sign 
	ceil : 첫번째 자리에서 내림
	floor : 첫번째 자리에서 내림
	isnan : 각 성분이 NaN(Not a Number)인 경우 True, 아닌 경우 False 반환
	isinf : 각 성분이 무한대인 경우 True, 아니면 Fasle
	cos, cosh, sin, sinh, tan, tanh : 삼각함수 계산

## 2개의 array에 쓰는 함수

	add : 더하기
	subtract : 빼기
	multiply : 곱하기
	divide : 나누기
	maximum : 두 array에서 같은 위치의 성분 비교해서 최댓값 반환
	minimun : 두 array에서 같은 위치의 성분 비교해서 최솟값 반환

## 통계함수

	sum 
	mean
	std, var : 표현편차, 분산
	min, max : 전체의 최솟값 (*minimum, maximum과 다름)
	argmin, argmax : 최소, 최대값 인덱스 반환
	cumsum : 처음부터 각 성분까지의 누적합(0부터 계속 더해짐)
	cumprod : 처음부터 각 성분까지의 누적곱(1에서부터 곱해짐)

##이렇게 씁니다
	import numpy as np
	np.abs()
	np.sqrt()
	np.add(arr1, arr2)
	np.sum()

##정렬
	np.sort()
	np.sort()[::-1] : 내림차순 정렬
	np.sort(x, axis=0) : 열끼리 
	np.sort(x, axis=1) : 행끼리만



	





