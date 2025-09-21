#weight.py
%%writefile converter3/weight.py
def kg_to_lb(kg: float):
    lb = kg * 2.20462
    return lb, f"{kg:.2f} kg = {lb:.2f} lb"

def lb_to_kg(lb: float):
    kg = lb / 2.20462
    return kg, f"{lb:.2f} lb = {kg:.2f} kg"
