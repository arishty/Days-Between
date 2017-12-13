def days(date1,date2):
    

    regyeardict = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
    leapyeardict = {1 : 31, 2 : 29, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}  # February has 29 days in leap year
    

    # Splits incoming date strings on "/" deliminator and converts to 3 separate integers
    date1 = date1.split('/')
    date2 = date2.split('/')
    for x in range(3):
        date1[x] = int(date1[x])
        date2[x] = int(date2[x])

    
    countdays = 0
    currentdate = date1                 # Start counting from first input date
    

    while currentdate[2] != date2[2]:   # While current date isn't within same year of end date
        if currentdate[2] % 4 != 0:     # It isn't a leap year
            countdays += regyeardict[currentdate[0]] - currentdate[1]       # Add the amount of days in current month to count variable, minus days passed already
        else:                           # It is a leap year
            countdays += leapyeardict[currentdate[0]] - currentdate[1]
        currentdate[0] += 1             # Go to next month
        currentdate[1] = 0              # Start from beginning of month
        if currentdate[0] == 13:        # If you pass the 12th month...
            currentdate[0] = 1          # go to the 1st month...
            currentdate[2] += 1         # of the following year
       
    while currentdate[2] == date2[2]:   # While current date is within same year of end date
        if currentdate[0] == date2[0]:  # If current date is within same month of end date
            break
        if currentdate[2] % 4 == 0:
            countdays += leapyeardict[currentdate[0]] - currentdate[1]
        else:
            countdays += regyeardict[currentdate[0]] - currentdate[1]
        currentdate[0] += 1
        currentdate[1] = 0  
       
    countdays += date2[1] - currentdate[1]      # Collect the leftover days of the current month until end date


    return countdays