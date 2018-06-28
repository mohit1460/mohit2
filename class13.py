try:
    a=[1,2,3]
    b=a[4]/0
except (ZeroDivisionError,IndexError):
    print("number is divided by zero")
else:
    print(a)
finally:
    print('i will execute')



try:
    import kuchbhi
    a=[1,2,3]
    b=a[4]/0
except ZeroDivisionError:
    print("number is divided by zero")
except IndexError:
    print("index error")
except ImportError:
    print("lib do not exist")
else:
    print(a)
class AgeError(Exception):
    pass
try:
    a=int(input("enter age"))
    if(a<18):
        raise AgeError

except ValueError:
    print("enter integer")
except AgeError:
    print("not above18")
else:
    print('eligible')

try:
    raise NameError("hi there")
except NameError:
    print("an exception")


