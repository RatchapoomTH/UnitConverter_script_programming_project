# temperature.py
%%writefile converter2/temperature.py
def fahrenheit_to_celsius(fr: float):
    c = (fr - 32) * 5 / 9
    return c, f"{fr:.2f} °F = {c:.2f} °C"

def celsius_to_fahrenheit(c: float):
    f = (c * 9 / 5) + 32
    return f, f"{c:.2f} °C = {f:.2f} °F"

def celsius_to_kelvin(c: float):
    k = c + 273.15
    return k, f"{c:.2f} °C = {k:.2f} K"

def kelvin_to_celsius(k: float):
    c = k - 273.15
    return c, f"{k:.2f} K = {c:.2f} °C"
