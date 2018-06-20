# question 1

m = (1, 2, "hello")
print(len(m))

#question 2

a=(1,2,3)
print(min(a))
print(max(a))

#question3

a=(1*2*3*4)
print (a)

#question1

a=set([1,2,3])
b=set([1,2,4,6])
print(b-a)
print(a&b)


#question1

a={"name":input("enter a name"),"marks":input("enter a marks")}
print(a)

#question2
a={"marks":17,"marks1":7,"marks2":4}
print(sorted(zip(a.values(), a.keys())))

#question3
l=["M","I","S","S","I","S","S","I","P","P","I"]
m=l.count("M")
i=l.count("I")
s=l.count("S")
p=l.count("P")
z={'m':m,'i':i,'s':s,'p':p}
print (z)
