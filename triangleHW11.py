side1 = 7
side2 = 4
side3 = 4
if (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
    print("The sides can form a triangle")
elif (side1 <= 0 or side2 <= 0 or side3 <= 0 ):
    print("The lengths of the sides must be positive")
else :
    print("The sides can form a triangle")