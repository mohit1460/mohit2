#question1

emails = '"zuck26@facebook.com page33@google.com  jeff42@amazon.com"'
#desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]
import  re

desired_output=re.findall('[\w]{1,10}[@][\w]{1,10}[.][\w]{1,4}',emails)
print(desired_output)

#question2

text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
e=re.findall('[Bb][\w]{1,20}',text)
print(e)

#question3

sentence = "A, very very; irregular_sentence"
#desired_output = "A very very irregular sentence"
d=sentence.replace("_"," ")
desired_output=re.sub('[^\w\s]',' ',d)
print(desired_output)
