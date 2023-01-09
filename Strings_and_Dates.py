user_date = input("Enter date: ")
while user_date != '-1':
    tokens = user_date.split()
    month = tokens[0]
    if month == 'January':
        month_int = 1
    elif month == 'February':
        month_int = 2
    elif month == 'March':
        month_int = 3
    elif month == 'April':
        month_int = 4 
    elif month == 'May':
        month_int = 5
    elif month =='June':
        month_int = 6
    elif month == 'July':
        month_int = 7
    elif month == 'August':
        month_int = 8
    elif month == 'September':
        month_int = 9
    elif month== 'October': 
        month_int = 10
    elif month =='November':
        mmonth_int = 11
    elif month == 'December':
        month_int = 12
    else:
        month_int = 0
    if len(tokens) >= 3 and month_int != 0 :
        date_string = tokens [1]
        if date_string[len(date_string) -1] == ',':
          date_string = date_string[0:len(date_string) -1]
          year = tokens[2]
          print(str(month_int)+'/'+date_string+'/'+str(year))
        else:
          print('Date entered is not valid')
    else:
        print('Date entered is not valid')
    user_date = input('Enter date: ')

















































































































































































