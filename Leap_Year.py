import random
yr=random.randint(100,2020)
print("The chosen year:",yr)
if(yr%4==0 and yr%100!=0 or yr%400==0):
    print(yr,"is a leap year.")
else:
    print(yr,"is not a leap year.")
