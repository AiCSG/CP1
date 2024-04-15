"""""""""
# 직각삼각형


## 설명
삼각형의 높이 또는 너비 N이 주어지면 문자 ' * '로 삼각형을 그리세요.

## 입력 설명
삼각형의 높이 또는 너비 N (N>=0)

## 출력 설명
' * '로 삼각형을 그려 출력합니다.


### 입력 예시 1 
3
### 출력 예시 1
*
**
***

### 입력 예시 2 
5
### 출력 예시 2
*
**
***
****
*****

### 입력 예시 3 
10
### 출력 예시 3
*
**
***
****
*****
******
*******
********
*********
**********

##힌트
print("=", end='') 로 출력하면 줄이 바뀌지 않습니다.
print("") 로 출력하면 줄만 바뀝니다.
"""""""""

n = int(input())

for i in range(1, n+1):
    print('*'*i)
