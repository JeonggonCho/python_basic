# 문제
# 정수 한 개를 입력 받고, 1부터 입력 값 사이의 정수 중 홀수만 출력하세요.
# 입력 값이 1보다 작으면 False를 출력하세요.

# 코드

num1 = int(input('정수를 입력하세요 > '))

if num1 >= 1:
    for i in range(num1):
        if i % 2 == 0:
            continue
        else:
            print(i)
else:
    print('False')