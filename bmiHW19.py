weight = 70
height = 1.77

BMI = weight / (height**2)
if BMI < 18.5:
    print(f"Your BMI is {BMI}. You are underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print(f"Your BMI is {BMI}, Tou are normal")
elif BMI >= 25 and BMI <= 29.9:
    print(f"Your BMI is {BMI}, Tou are overweight")
elif BMI >= 30 :
    print(f"Your BMI is {BMI}, Tou are obese")
else:
    print("You have entered invalid weight and height")