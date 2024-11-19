def multi_password_strength_counter(passwords):
    special_Characters = "!@#^&*()-+"
    results = []
    for password in passwords:
        strength = {
            'length': len(password) >= 8,
            'digit' : any(char.isdigit() for char in password),
            'lowercase': any(char.islower() for char in password),
            'uppercase' : any(char.isupper() for char in password),
            'special_char' : any(char in special_Characters for char in password) 
        
        }

        results.append(strength)

    return results
    
    
passwords = ["password", "Pa$$w0rd", "SuperSecurePwd!", "weakpw"]
results = multi_password_strength_counter(passwords)
for result in results:
    print(result)
