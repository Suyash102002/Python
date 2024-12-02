password = 'suyash@10'
if len(password) >= 8 and '@' in password:
    print("Your password is valid")
elif len(password) < 8 and '@' not in password:
    print("Your password is Invalid")
elif len(password) < 8 :
    print("Your password is Invalid. It must contain 8 characters.")
elif '@' not in password :
    print("Your password is Invalid. It must contain @")
