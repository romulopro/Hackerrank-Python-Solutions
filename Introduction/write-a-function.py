def is_leap(year):
    leap = False
    
    # Write your logic here
    
    if(int(year%4) == 0):
        if(int(year%100) == 0):
            if(int(year%400) == 0):
                leap = True
        else:
            leap = True
    return leap
