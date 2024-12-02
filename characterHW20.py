char = '@'
if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z'):
    print("The character is alphabet")
elif (char >= '0' and char <= '9'):
    print("The character is digit")
else :
    print("The character is special character")