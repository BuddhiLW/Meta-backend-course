import sys

loc = sys.path
for i in loc:
print(i)

import calendar

leapdays = calendar.leapdays(2000, 2050)
print(leapdays)
