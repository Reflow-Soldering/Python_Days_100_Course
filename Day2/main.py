# print(len("Hello"))

# print(len(12345))  타입에러

# print("Hello"[0]) # "Hello" 뒤에 [0]이면 0번째 자리만 출력

# 그럼 이렇게 하면?
# print("Hello"[])
# print("Hello"[9])
# 특정 인덱스만 찾네... 문자열의 포지션이 아니거나, empty로 두면 에러남

# print("Hello"[4])

# 이건 놀랍네
# print("Hello"[-1])

# 문자열에 대한 이야기
# 아래는 문자열로 취급함
# "123" 
# print("123" + "456")
# 결과값은 123456

# 정수에 대한 이야기
# print(123 + 345)
# 실질적인 정수값 얻을 수 있음

#사람이 사용하는 쉼표 대체법 큰 값일 경우 좋음
# print(123_456_789)

#부동소수점 타입
# print(3.14569)

#부울 타입 True/False
# print(True)
# print(False)
#그럼 파이썬의 부울값이 0과 0이 아닌 값을 보는건가? 아니면 0과 1인가?

# len("1")

# 위처럼 쓰면 데이터 타입은 어찌 알겠는가?
# print(type(123)) 
# type이란 함수가 있네

"""
#타입 구분!
print(type(123))
print(type(22.333))
print(type("data"))
print(type(True))
"""

#타입 캐스팅 - 어떠한 특정한 타입으로 변환하는거지...(int)"123"
# 타입캐스팅이 좀 다르네
# print("123" + "456")
# print(int("123") + int("456"))
#신기하네....
# print(int("abc") + int("456"))
# 문자의 경우 숫자로 변환할 수 없는 값이기때문에 불가능
# 결국 적절한 타입 캐스팅이 중요하다는것 얘는 그것만 맞춰주면 알아서 해줌


"""
name_of_the_user = input("Enter your name ") # 문자열
length_of_name = len(name_of_the_user) # 정수

print("Number of letters in your name: " + str(length_of_name))
"""


# print("My age : " + str(12))
# print(123 + 456)
# print(7 - 3)
# print(4 * 3)
# print(int(2/22))
# print(6 // 3)
# #제곱
# print(2 ** 3)
#이것도 제곱될까?
# print(2^3)
#안되네

# 나눗셈 /과 //는 다르다 /는 부동소수점 //은 정수로

# PEMDASLR은 모르겠고 사칙연산
# 3이 나오게 해보시오
# print(3 * 3 / 3 + 3 - 3)

"""
코드실습 1
"""
"""
height = 1.65 # meter
weight = 84   # kilo grams

bmi = (weight / (height ** 2))

print(bmi)

"""
"""
# 정수로 변환

height = 1.65 # meter
weight = 84   # kilo grams

bmi = (weight / (height ** 2))

#정수 미만 자름
print(int(bmi))

#소수점 반올림
print(round(bmi))

#반올림 테스트 round(값, 나타낼 소수점 자리)
print(round(bmi, 3))

"""


# f-string 관련

"""
score = 0
height = 1.8
is_winning = True

# f-string????뭔소리야
# C#의 $,@ 사용이랑 유사
print(f"Your score is = {score}, your height is {height}. Your are winning is {is_winning}")

"""

# 팁 계산기

print("Welcom to the tip claculator!\n")
Bill = float(input("What was thr total bill? "))
Tips = float(input("How much tip would you like to give? 10, 12, or 15? "))
Split = float(input("How many people to split the bill? "))
Total = float((Bill + (Bill * Tips / 100))/Split)
Final = round(Total,2)
print(f"Each person shoud pay :  {Final}")