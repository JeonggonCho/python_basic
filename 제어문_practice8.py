# 문제
# 정수 두 개를 입력 받고, 두 수 사이의 정수를 내림차순으로 한 줄에 모두
# 출력하세요.
# 두 값이 같으면 False를 출력하세요.

# 코드

num1 = int(input('첫 번째 정수를 입력하세요 > '))
num2 = int(input('두 번째 정수를 입력하세요 > '))

if num1 > num2:
    for i in range(num2 + 1, num1)[::-1]:
        print(i, end=" ")
elif num1 < num2:
    for j in range(num1 + 1, num2)[::-1]:
        print(j, end=" ")
else:
    print('False')