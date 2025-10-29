print("\n______________****2****________________\n")
import datetime as i 
a=i.datetime.now()

print("current  date and time",a)
print("current year:",a.year)
print("month:",a.strftime("%b"))
print("week number of the year:",a.strftime("%U"))
print("weekday of the week:",a.strftime("%w"))
print("day of the year:",a.strftime("%j"))
print("day of the month:",a.day)
print("day of week:",a.weekday())

print("\n______________****2****________________\n")

#2
y=int(input("enter the year:"))

if y % 4:
    print(y,"is a leap year")
else:
    print(y,"not a leap year")


print("\n______________****3****________________\n")

#3
from datetime import datetime as d

x=int(input("enter the date:"))
y=input("enter the month:")
z=int(input("enter  the year:"))

date=f"{x} {y} {z}"

print("date:",d.strptime(date,"%d %B %Y"))   


print("\n______________****4****________________\n")

#4
from datetime import datetime

ct=datetime.now().time()
print("current time:",ct)


print("\n______________****5****________________\n")

#5
from datetime import datetime as d

string="april 7 20 2:22PM"
print("covert datetime :",d.strptime(string,"%B %d %y %I:%M%p"))


print("\n______________****6****________________\n")

#6
from datetime import datetime as d ,timedelta
x=d.now()
z=x-timedelta(5)
z=x-timedelta(days=5)
print("Current days:", x)
print("sunday before:",z)


print("\n______________****7****________________\n")

#7
from datetime import datetime as d ,timedelta
x=d.now()
yester=x-timedelta(1)
tmr=x+timedelta(1)
print("yesterday:", yester)
print("today:",x)
print("tomorrow :", tmr)

print("\n______________****8****________________\n")

#8th

from datetime import datetime as d, timedelta
x=d.strptime("28:33.0","%M:%S.%f")
add=x+timedelta (seconds=5)
print(add.strftime("%M:%S.%f") [::-3])

print("\n______________****9****________________\n")

#9th
from datetime import datetime as d
x=d.now()
print("current ",x)
print("in millsecond: ",x.timestamp())

print("\n______________****10****________________\n")
#10th

from datetime import datetime as d
x=d.strptime("2015,6,16", "Y, sm, d")
print("week number:",x.strftime("%U"))
print("\n______________****11****________________\n")
#11

from datetime import datetime as d
x=d(2001,2,28)
y=d (2000,2,28)
z=x-y
print("between days:",z)


print("\n______________****12****________________\n")
#12th

from datetime import datetime as d
d1=d (2022,1,1,0,0,0)
d2=d (2022, 1,2,12,30,30)
diff=d2-dl
print("difference: ",diff.days, "days", diff.seconds//3600, "hours", ((diff.seconds//60)%60), "minutes", diff.seconda %60, "seconds")

print("\n______________****13****________________\n")

#13th

from datetime import date
def calculateage (dob):
    x=date.today()
    age-x.year-dob.year
    return age
dob=date(2005,6,9)
print("age: ",calculateage(dob))
print("\n______________***********________________\n")

