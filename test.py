# pi = 3.14159
# print(pi)

# first_num =  input ('Please enter a number')
# second_num = input ('Please enter a another number')
# print (int(first_num) + int(second_num))

# days_in_August = 31
# print(str(days_in_August) + ' ' +'total days in August')
# from datetime import datetime
# current_date = datetime.now()
# print('Today is :'+ ' ' +str(current_date))
# from datetime import datetime,timedelta
# today = datetime.now()
# one_day = timedelta(days=1)
# yesterday = today - one_day
# print('Yesterday was :' + str(yesterday))

# price = input('how much did you pay?')
# price = float(price)
# if price >= 1.00:
#     tax = .07
#     print('Tax rate is: ' + str(tax))

# price = input('how much did you pay?')
# price = float(price)

# if price >= 1.00:
#     tax = .07

# else: 
#     tax = 0
# print('Tax rate is :' + str(tax))

# country = input('Enter the name of your country: ')
# if country.lower() == 'Kenya':
#     print('so you must love kipchoge!')
# else:
#     print('Your not from kenya')
# province = input ('What province do you live in ?')
# tax = 0

# if province in('Alberta','Nunavut','Yukon'):
#     tax = 0.05
# elif province == 'Ontario':
#     tax = 0.13
# else:
#     tax= 0.15
# print(tax)

# country = input(' What country do you live in?')

# if country == 'Canada':
#     province = input("What province/state do you live in? ") 
#     if province in('Alberta',\
#         'Nunavut','Yukon'):
#         tax = 0.05
#     elif province == 'Ontario':
#         tax = 0.13 
#     else:
#         tax = 0.15 
# else:
#     tax = 0.0
# print(tax)

# gpa = int(input('What was your Grade Point Average? '))
# lowest_Grade = int(input('What was your lowest Grade? '))

# if gpa >= 85 and lowest_Grade >= 70:
#     print ('You made the honour roll')

gpa = int(input('What was your Grade Point Average? '))
lowest_Grade = int(input('What was your lowest Grade? '))

if gpa >= 85 and lowest_Grade >= 70:
    honour_roll = True
else:
    honour_roll = False

if honour_roll:
    print ('You made the honour roll')
