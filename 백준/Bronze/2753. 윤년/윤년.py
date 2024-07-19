year = int(input())

yn = 0

con1 = year % 4
#true 
con2 = year % 100
#false
con3 = year % 400
#true

if(con1 == 0) and (con2 != 0):
    yn = 1
elif(con3 == 0):
    yn = 1
else:
    yn = 0
    
print(yn)

    