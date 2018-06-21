#question1
print("we represent time in a way that's easy for us understand python stores in tuples,these python are made of nine no"
      "index (0) field (years) value(1995)"
      "index (1) field (month) value(1 to 12)"
      "index (2) field (day) value(1 to 31)"
      "index (3) field (hour) value(0 to 23)"
      "index (4) field (minutes) value(0 to 59)"
      "index (5) field (second) value(0 to 61)"
      "index (6) field (day of week) value(0 to 6)"
      "index (7) field (day of year) value(1 to 366)"
      "index (8) field (dst) value(-1,0,1)")

#question2

import datetime
d=datetime.datetime.now().strftime('7,41,54')
print(d)

#question3

import datetime
from datetime import date
d=datetime.date.today()
print(d.month)

#question4
import datetime
from datetime import date
d=datetime.date.today()
print(d.day)

#question 5
import datetime
from datetime import date
d=datetime.date.today()
d.strftime("%d%m%Y")
print(d.day)

#question6
import time
d=time.asctime(time.localtime())
print(d)

#question7
import math
d=math.factorial(5)
print(d)

#question8

import math
d=math.gcd(10,18)
print(d)

#question9

import os
d=os.getcwd()
print(d)
n=os.environ
print(n)


