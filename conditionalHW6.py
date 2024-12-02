num1 = 5
num2 = 20
num3 = 9

if num1 >= num2:
    if num1 >= num3:
        largest = num1 
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3
        
print(largest)