%%writefile converter.py

def fahrenheit_to_celsius(fr):
    fr = (fr - 32) * 5 / 9
    return fr, f"Fahrenheit equal {fr:.2f} Celsius"

def celsius_to_fahrenheit(c):
    c = (c * 9 / 5) + 32
    return c, f"Celsius equal {c:.2f} Fahrenheit"

def celsius_to_kelvin(c):
    k = c + 273.15
    return k, f"Celsius equal {k:.2f} Kelvin"

def kilogram_to_pound(kg):
    lb = kg * 2.20462
    return lb, f"{kg:.2f} Kilogram equal {lb:.2f} Pound"

def pound_to_kilogram(lb):
    kg = lb / 0.453592
    return kg, f"{lb:.2f} Pound equal {kg:.2f} Kilogram"
