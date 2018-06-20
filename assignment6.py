#question1

for i in range (10):
    y = int(input("enter y:"))
    print(y)
#question2
i=1
while(True):
    print(i)
    

#question3
l=[]
a=int(input())
b=int(input())
l.append(a)
l.append(b)
for i in l:
    print(i**2)


#qustion4
l=[1,"h",1.3]
for i in (l):
    p=[]
    q=[]
    r=[]
    print(*l,end="\n")
    break

#question5
even=[]
odd=[]
for i in range(1,101):
    if (i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

#question6

for i in range(1,5):
	for j in range(1,i+1):
		print("*",end ="")
	print()

#question7
d={"name":input("name:"),"age":input("age")}
for i in d:
    d.get(i)
    print(i)
#question8
l=[]
for i in range(0,5):
    num=int(input("enter "))
    l.append(num)
print(l)
l2=[]
a=int(input("enter the value:"))
x=l.index(2)
x=l.remove(2)
print(l)








