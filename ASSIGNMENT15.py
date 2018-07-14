#question1

emailid = "zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"
import re
emails=re.findall('[\w_$+-=]{1,20}[@][\w]{1,20}[.]{\w]{1,3}',emailid)
t=[('zuck26','facebook','com'),('page33','google','com','jeff42','amazon','com')]
print(t)

#question2

str= "Betty bought a bit of butter, But the  butter was so bitter , so she bought some better butter, to make the bitter butter better"
import re
word= re.findall('[Bb][\w]{1,20}',str)
print(word)


#question3

s= "A, very very; irregular_sentence"
import re
d=s.replace("_"," ")
sentence= re.sub(r'[^\w\s]',' ', d)
print(sentence)