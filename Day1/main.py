#print("Hello")
#주석처리 완료

"""
텍스트 실습 1
"""
"""
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")
"""


###########

#print("Hello world!\nHello World\nHello woooorld")

#자꾸 printf를 쓰게 된다
#+사용시 띄어쓸거면 공백 넣으라 이말이야 
#print("Hello" + " Mister")
#print("Hello"+" "+"Mister")

#습관적으로 tab이나 space 사용 금지

#print ("핥짝")
#원칙적으로는 print("핥짝") 이어야함. 경고뜸

#print("핥짝")

"""
텍스트 실습2
"""

# Fix the code below 👇
"""
print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")
"""


#input("What is your name? ")

#print("Hello " + input("What is your name?"))
# print("Hello " + input("What is your name?") + "!!")

# name = input("What is your name?")
# print("Hello" + name + "!!")
# name = "Jack"
# print(name)

# name = "Mister"
# print(name)


# print(len(input("What is your name?")))

# username = input("What is your name?")
# length = len(username)
# print(length)

"""
텍스트 실습2
"""

glass1 = "milk"
glass2 = "juice"
glass3 = glass2
glass2 = glass1
glass1 = glass3

print(glass1,glass2)