# pi = 3.14159
# print(pi)

# first_num =  input ('Please enter a number')
# second_num = input ('Please enter a another number')
# print (int(first_num) + int(second_num))

days_in_August = 31
print(str(days_in_August) + ' ' +'total days in August')
from datetime import datetime
current_date = datetime.now()
print('Today is :'+ ' ' +str(current_date))
from datetime import datetime,timedelta
today = datetime.now()
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was :' + str(yesterday))