def is_leap(year):
    if year % 4==0:
        if year %100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True 
    else:
        return False
value=is_leap(int(input("Enter a year: ")))
print(value) 

def days_in_month(year,month):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    index_month=month-1
    if is_leap(year) and index_month==1:
        return 29
    else:    
       return month_days[index_month]
    
year=int(input("Enter a year:"))
month=int(input("Enter a month: "))

days=days_in_month(year,month)
print(days)
    