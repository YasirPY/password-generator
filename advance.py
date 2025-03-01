import random 
import string

def pass_gen():
    while True:
        try:
            length = int(input('Enter the length of the password: '))
            if length > 4:
                break
            print("Length of password must be greater than 4.")
        except ValueError :
            print('Invalid input! Enter a number.')
            continue

    while True:
        
        include_upper = input("Include Upper Case Letters? (yes/no): ").lower().strip()
        if include_upper == "yes" or include_upper == "no":
            break
        else:
            print("Invalid Input! Enter (yes/no)")
    
    while True:
        
        include_special_chr = input("Include Special Characters? (yes/no): ").lower().strip()
        if include_special_chr == "yes" or include_special_chr == "no":
            break
        else:
            print("Invalid Input! Enter (yes/no)")
    
    while True:
        
        include_digits = input("Include Digits? (yes/no): ").lower().strip()
        if include_digits == "yes" or include_digits == "no":
            break
        else:
            print("Invalid Input! Enter (yes/no)")

    lower_chr = string.ascii_lowercase
    upper_chr = string.ascii_uppercase if include_upper == "yes" else ""
    special_chr = string.punctuation if include_special_chr == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""

    total_chr = upper_chr + lower_chr + special_chr + digits
    required_chr = []
    
    if include_upper == "yes":
        required_chr.append(random.choice(upper_chr))

    if include_special_chr == "yes":
        required_chr.append(random.choice(special_chr))

    if include_digits == "yes":
        required_chr.append(random.choice(digits))
    
    remaining_len = length - len(required_chr)

    for _ in range(remaining_len):
        required_chr.append(random.choice(total_chr))
    print(required_chr)
    random.shuffle(required_chr)
    password = ""
    for i in required_chr:
        password += i
    print(password)
    

if __name__ == "__main__":
    pass_gen()
