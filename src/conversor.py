def celsius_a_fahrenheit(celsius): 
    return (celsius * 9/5) + 32 
def fahrenheit_a_celsius(fahrenheit): 
    return (fahrenheit - 32) * 5/9 
def celsius_a_kelvin(celsius): 
    return celsius + 273.15 
def kelvin_a_celsius(kelvin): 
    if kelvin < 0: 
        raise ValueError('La temperatura en Kelvin no puede ser negativa') 
    return kelvin - 273.15