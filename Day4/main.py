# import random

#����̶�?
#�̸� ������� ������ ����� �� - �Լ��� ���� ���� �ȴ�

#���� ���� 
""" random_integer = random.randint(1, 3)
print(random_integer) """

#�ε��Ҽ��� ����
#random.random() ��ȣ�� �׻� �ٴ°� ����
#0.xxxxxx�� ����
""" random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1) """


#������ ������ �ε��Ҽ���

""" random_float = random.uniform(0, 10)
print(random_float) """

#�ո� �޸� �̾߱��ϴ°Ű���
""" Head_or_Tail = random.randint(0,1)
if(Head_or_Tail == 0) :
    print("Head")
else :
    print("Tail") """


#����Ʈ�� ���� ����
# \�� �ٹٲ��� �ص� �̾����ٴ� ��
# ����Ʈ�� 0���� �����Ѵ�
""" states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", \
                     "Connecticut", "Massachusetts", "Maryland", "South Carolina",\
                     "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",\
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",\
                     "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",\
                     "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia",\
                     "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington",\
                     "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"] """
#-1�� ������ �Ͽ��� -> �� ������ �����Ѵ�
# 0�� ������ ������ ����Ʈ ������ 0������ �����ϱ⶧���̴�
# print(states_of_america[1])

#������ �ڷ� ��ȯ
""" states_of_america[1] = "pecil"
print(states_of_america[1]) """

#append �̾߱� -> �� ������ �߰���
""" states_of_america.append("3rd world")
print(states_of_america[-1]) """

#extend -> �����Ǵ� ��� ���� ������ �߰���
""" states_of_america.extend(["another1", "another222"])
print(states_of_america) """




###�ڵ� �������� 1
# import random
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#���� �� �� - �ش�2
""" random_friend = random.randint(0,4)
print(friends[random_friend]) """

#�ش�1
# print(random.choice(friends))



#�ε��� ������ ���� ����!!
#�迭, �ε��� �ǵ帮�� �ʴ� �̻� 0���� ������
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", \
                     "Connecticut", "Massachusetts", "Maryland", "South Carolina",\
                     "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",\
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",\
                     "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",\
                     "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia",\
                     "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington",\
                     "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(len(states_of_america[50]))

#����Ʈ���� �߰�
# states_of_america.extend(["aaa","bbb","ccc"])
# print(states_of_america)

#����Ʈ���� ����
# states_of_america.pop(52)
# print(states_of_america)


#�ƴϳ� ����
""" dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines",\
                "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"] """

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
# vegetables = ["Spinach", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen)

# ���� ��������
import random

#���� �ʿ� ���������� ��Ģ
#���� 0 ���� 1 �� 2
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
#0�� 1�� �̱�� 1�� 2�� �̱��, 2�� 0�� �̱�
# ���� 0 ���� 1 �� 2
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

