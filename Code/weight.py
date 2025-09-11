# weight.py
%%writefile converter2/weight.py
def kilogram_to_pound(kg: float):
    lb = kg * 2.20462
    return lb, f"{kg:.2f} kg = {lb:.2f} lb"

def pound_to_kilogram(lb: float):
    kg = lb / 0.453592
    return kg, f"{lb:.2f} lb = {kg:.2f} kg"
