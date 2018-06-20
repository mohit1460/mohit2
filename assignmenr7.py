#question1
radius=float(input("enter no."))
def area(rad):
    area=3.14*rad*rad
    return area
ar=area(radius)
print(ar)

#question2
n=6
def perfect(n):
    sum = 0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
        return True
    else:
        return False
for i in range(1,1001):

    if (perfect(i)==True):
        print(i)

#question3

def mul(n,i=1):
    print(i * n)
    if i!=10:
        mul(n,i+1)

print(mul(12))

#question4

def power(a,b):
    if (b==1):
        return(a)
    if (b!=1):
        return(a*power(a,b-1))
a=int(input("enter a"))
b=int(input("enter b"))
print("result",power(a,b))

#question5

def fact(n):
    if(n<=1):
        return 1
    else:
        return(n*fact(n-1))
d={}
n=int(input("enter"))
print ("fact")
print(fact(n))
d[n]=fact(n)
print(d)