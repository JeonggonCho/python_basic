# 문제
# 이름과 태어난 년도를 입력 받고, 출력하세요.
# (단, 태어난 년도를 나이로 변환해서 출력하세요)

name = str(input('이름을 입력해주세요 > '))
age = str(2023 - int(input('태어난 년도를 입력해주세요 > ')) + 1)

print('저의 이름은', name+'이고, 올해 나이는', age+'세 입니다.')