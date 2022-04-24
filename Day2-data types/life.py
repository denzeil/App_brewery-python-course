age=int(input("How old are you? "))
#365 days a year
#12 months in a year
#a year has 54 weeks
#output must be "you have x days,y weeks and z months left"
#90 years as our pass mark
days=(90-age)*365
weeks=(90-age)*54
months=(90-age)*12
print(f"You have {days} days, {weeks} weeks and {months} months left")