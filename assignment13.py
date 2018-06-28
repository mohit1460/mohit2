#question1

#exception occcured is  ZeroDivisionError
try:
    a=3

    a=a/(a-3)
except ZeroDivisionError:
    print("error")
else:
    print(a)
finally:
    print("handeled")

#question 2

#IndexError

try:
    l=[1,2,3]
    a=l[3]
except IndexError:
    print("list index is out of bounds")
else:
    print(l)
finally:
    print("handeled")

#question3

#output is "an exceptiion"

#question4

#AbyB(2.0, 3.0)   output -5
#AbyB(3.0, 3.0)   output "a/b result in 0"

#question5
 #import error
try:
    import kuchbhi
except ImportError:
    print("error")

#value error
try:
    n=int(input("enter"))
except ValueError:
    print("please enter an integer")
#index error
try:
    l=[1,2]
    n=l[4]
except IndexError:
    print("index out of bounds")









#question6
i=0
class Agetosmall(Exception):
    pass

while(i<18):
    try:
        i=int(input("E:"))
        if (i<18):
            raise Agetosmall

    except Agetosmall:
       print("age is less than 18")
else:
    while(False):
        pass
