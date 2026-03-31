print("Welcome to the Password Checker")
print("Please enter your password :")


password = input(" ").strip()


def pass_len(password):
    
    has_upper = False
    has_number = False
    has_special = False

    
    for char in password:
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_number = True
        if not char.isalnum():
            has_special = True

    
    if len(password) <=7 and not has_upper and not has_number:
        print("Weak")
        print("Tip: Try using more than 8 characters and at least one uppercase letter.")
    elif len(password) <=7 and has_upper and not has_number:
        print("Weak")
        print("Tip: Try using more than 8 characters.")
    elif len(password) >= 8 and not has_number and not has_upper:
        print("Poor")
        print("Tip: Include at least one uppercase letter and a number.")
    elif len(password) >= 8 and has_upper and not has_number:
        print("Fair")
        print("Tip: Include at least one number.")
    elif len(password) > 8 and has_upper and has_number and not has_special:
        print("Medium")
        print("Tip: Include at least one special character.")
    elif len(password) > 8 and has_upper and has_number and has_special:
        print("Perfect and Strong.")
   
    
    

pass_len(password)