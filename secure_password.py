def password_strength_counter(password):
    strength = {
        'length':False,
        'digit': False,
        'lowercase':False,
        'uppercase':False,
    }
    if len(password) >= 8:
        strength['length'] = True
    for char in password:
        if char.isdigit():
            strength['digit'] = True
        elif char.islowercase():
            strength['lowercase'] = True
        elif char.isuppercase():
            strength['uppercase'] = True
    return strength