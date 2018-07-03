# ques 1
f=open("file.txt", encoding="utf8")
a=(f.readlines())
a.reverse()
n=int(input("enter number of lines"))
for i in range(0,n):
    print(a[i])
f.close()

## ques 2
a="kill"
f=open("file.txt","r")
k=f.read()
m=k.split()
print(k.count(a))

### ques 3
f=open("file.txt",encoding="utf8")
a=(f.readlines())
c=open("files3.txt","w")
c.writelines(a)

#### ques 4
i=0
f=open("file1.txt","r")
a=(f.read())
f.writelines(a)