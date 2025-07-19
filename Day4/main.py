# import random

#모듈이란?
#미리 만들어진 내용을 사용한 것 - 함수와 같이 보면 된다

#정수 랜덤 
""" random_integer = random.randint(1, 3)
print(random_integer) """

#부동소수점 랜덤
#random.random() 괄호는 항상 붙는게 맞음
#0.xxxxxx만 나옴
""" random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1) """


#지정된 범위의 부동소수점

""" random_float = random.uniform(0, 10)
print(random_float) """

#앞면 뒷면 이야기하는거같음
""" Head_or_Tail = random.randint(0,1)
if(Head_or_Tail == 0) :
    print("Head")
else :
    print("Tail") """


#리스트에 관한 정의
# \는 줄바꿈을 해도 이어진다는 것
# 리스트는 0부터 시작한다
""" states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", \
                     "Connecticut", "Massachusetts", "Maryland", "South Carolina",\
                     "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",\
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",\
                     "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",\
                     "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia",\
                     "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington",\
                     "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"] """
#-1을 넣으면 하와이 -> 맨 끝에서 시작한다
# 0을 못쓰는 이유는 리스트 시작이 0번부터 시작하기때문이다
# print(states_of_america[1])

#내부의 자료 교환
""" states_of_america[1] = "pecil"
print(states_of_america[1]) """

#append 이야기 -> 맨 끝으로 추가함
""" states_of_america.append("3rd world")
print(states_of_america[-1]) """

#extend -> 나열되는 모든 것을 끝에서 추가함
""" states_of_america.extend(["another1", "another222"])
print(states_of_america) """




###코딩 연습문제 1
# import random
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#내가 한 것 - 해답2
""" random_friend = random.randint(0,4)
print(friends[random_friend]) """

#해답1
# print(random.choice(friends))



#인덱스 에러에 대한 내용!!
#배열, 인덱스 건드리지 않는 이상 0부터 시작함
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", \
                     "Connecticut", "Massachusetts", "Maryland", "South Carolina",\
                     "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",\
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",\
                     "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",\
                     "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia",\
                     "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington",\
                     "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(len(states_of_america[50]))

#리스트에서 추가
# states_of_america.extend(["aaa","bbb","ccc"])
# print(states_of_america)

#리스트에서 삭제
# states_of_america.pop(52)
# print(states_of_america)


#아니네 쓰네
""" dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines",\
                "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"] """

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
# vegetables = ["Spinach", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen)

# 최종 연습문제
import random

#개선 필요 가위바위보 규칙
#가위 0 바위 1 보 2
while(1) :
    myhand = int(input("Gawee(0), Bawee(1), Bo(2) "))
    urhand = random.randint(0,2)
    print("my hand " + str(myhand))
    print("your hand " + str(urhand))
    if myhand >= 0 and myhand < 3 :
        if(myhand == urhand) :
            print("draw")
        elif((urhand - myhand) == 1) :
            print("lose")
        elif((myhand - urhand) == 1) :
            print("win")
        elif ((myhand - urhand) == 2) :
            print("lose")
        else :
            print("win")
    else :
        print("again")


""" 
while(1) :
    myhand = int(input("Gawee(0), Bawee(1), Bo(2) "))
    urhand = random.randint(0,2)
#0을 1이 이기고 1을 2가 이기고, 2를 0이 이김
# 가위 0 바위 1 보 2
    if myhand == "0" :
        if(urhand == 1) :
            print("Lose\n")
        elif(urhand == 2) :
            print("Win\n")
        else :
            print("Draw\n")
    elif myhand == "1" :
        if(urhand == 2) :
            print("Lose\n")
        elif(urhand == 0) :
            print("Win\n")
        else :
            print("Draw\n")
    elif myhand == "2" :
        if(urhand == 0) :
            print("Lose\n")
        elif(urhand == 1) :
            print("Win\n")
        else :
            print("Draw\n")
    else :
        print("Again")  """