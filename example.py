year= int(input("Enter a year:"))
if(year%400==0 or year%4==0 and year%100!=0):
    print("its a leap year")
else:
    print("its not a leap year")