import datetime

# date

b_day  = datetime.date(2025,12,30)
print(b_day)

today = datetime.date.today()
print(today)

print(b_day.strftime('%A,%B %d,%Y'))

age = today - b_day  #  calculate age
print(age)
 
 # Time
t = datetime.time(9,30,45,100000)
print(t)
print(t.hour)
print(t.minute)


#Date and time

T = datetime.datetime.today()
print(T)

T_delta = datetime.timedelta(days = 20)
print(T + T_delta)