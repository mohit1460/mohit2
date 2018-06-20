# question 1
year = input("enter an year")
if (int(year) % 4 == 0):
    print("leap year")
else:
    print("not a leap year")
# question 2
length = input("enter length")
breadth = input('enter breadth')
if (length == breadth):
    print("square")
else:
    print("rectangle")
# question3
a = input("enter a")
b = input("enter b")
c = input("enter c")
if (a > b and a > c):
    print("a is oldest")
elif (b > a and b > c):
    print("b is oldest")
elif (c > a and c > b):
    print("c is oldest")
else:
    print("equal age")
# question 4
points = int(input("enter points"))
if (points >= 1 and points <= 50):
    print("no prize")
elif (points >= 51 and points <= 150):
    print('congratulation')
    print('wooden dog')
elif (points >= 151 and points <= 180):
    print('congratulation')
    print("book")
elif (points >= 181 and points <= 200):
    print('congratulation')
    print("chocolates")
else:
    print("sorry! no prize this time")

# question 5

x = int(input('enter a number'))
a=100*x
if(a>1000):
    b=a*0.1
    print("discount=")
    print(b)
    c=a-b

    print("cost after discount")
    print(c)
else:
    print (a)
