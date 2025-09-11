# length.py
%%writefile converter2/length.py
def meter_to_kilometer(m: float):
    km = m / 1000
    return km, f"{m:.2f} m = {km:.2f} km"

def kilometer_to_meter(km: float):
    m = km * 1000
    return m, f"{km:.2f} km = {m:.2f} m"

def centimeter_to_meter(cm: float):
    m = cm / 100
    return m, f"{cm:.2f} cm = {m:.2f} m"

def meter_to_centimeter(m: float):
    cm = m * 100
    return cm, f"{m:.2f} m = {cm:.2f} cm"
