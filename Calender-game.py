#Calenders :
name=input("Enter your name : ")
print("Welcome",name,"to our calender game\n")    
d=int(input("Enter the date :"))
m=int(input("Enter the month :"))
y1=int(input("Enter first two digits of the year :"))
y2=int(input("Enter last two digits of the year :"))

    
  
r=str(y1)+str(y2)
r=int(r)

if y2 == 0 or y2 == 1 or y2 == 2 or y2 == 3 or y2 == 4 or y2 == 5 or y2 == 6 or y2 == 7 or y2 == 8 or y2 == 9:
    a = y2//4
    a = a-1
else:
    a = y2//4
       
    

b=0
month = 0
if m == 1:
    month = 0
elif m == 2:
    month = 3
elif m == 3:
    month = 3
elif m == 4:
    month = 6 
elif m == 5:
    month = 1 
elif m == 6:
    month = 4 
elif m == 7:
    month = 6 
elif m == 8:
    month = 2 
elif m == 9:
    month = 5 
elif m == 10:
    month = 0 
elif m == 11:
    month = 3 
elif m == 12:
    month = 5
    

if r in range(1600,1699):
    b = 5
    
elif r in range(1700,1799):
    b = 4
    
elif r in range(1800,1899):
    b = 2
    
elif r in range(1900,1999):
    b = 0

elif r in range(2000,2099):
    b = 6
 
if b == 5:
    b = b+1
    day = (d + month + y2 + a + b) % 7
    
elif b == 4:
    day = (d + month + y2 + a + b) % 7
    
elif b == 2:
    day = (d + month + y2 + a + b) % 7
    

elif b == 0:
    day = (d + month + y2 + a + b) % 7


elif b == 6:
    day = (d + month + y2 + a + b) % 7
    

if d>31 or d<1:
    print("Enter the correct date")
elif m<1 or m>31:
    print("Enter correct month")    
elif r>2099: 
    print("Enter the correct year")
else:    
    if day == 0:
        day = 'Sunday'
        print("The day is or was :",day)
    
    elif day == 1:
        day = 'Monday'
        print("The day is or was :",day)

    elif day == 2:
        day = 'Tuesday'
        print("The day is or was :",day)

    elif day == 3:
        day = 'wednesday'
        print("The day is or was :",day)
    
    elif day == 4:
        day = 'Thursday'
        print("The day is or was :",day)

    elif day == 5:
        day = 'Friday'
        print("The day is or was :",day)

    elif day == 6:
        day = 'Saturday'
        print("The day was or is:",day)
     

"""
jan=0
feb=3
mar=3
apr=6
may=1
jun=4
jul=6
aug=2
sep=5
octo=0
nov=3
dec=5

sun=0
mon=1
tue=2
wen=3
thu=4
fri=5
sat=6

1600-1699=6
1700-1799=4
1800-1899=2
1900-1999=0
2000-2099=6
"""
