max_num= 0
max_i = 0

for i in range (0,9):
    a = int(input())
    if a > max_num:
        max_num = a 
        max_i = i
        
print (max_num)
print (max_i + 1) 