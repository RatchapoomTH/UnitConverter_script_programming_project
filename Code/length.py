# length.py
%%writefile converter2/length.py
def meter_to_kilometer(m: float):
    if m < 0:
        return None, "❌ Length cannot be negative."
    km = m / 1000
    return km, f"{m:.4f} m = {km:.4f} km"

def kilometer_to_meter(km: float):
    if km < 0:
        return None, "❌ Length cannot be negative."
    m = km * 1000
    return m, f"{km:.4f} km = {m:.4f} m"

def centimeter_to_meter(cm: float):
    if cm < 0:
        return None, "❌ Length cannot be negative."
    m = cm / 100
    return m, f"{cm:.4f} cm = {m:.4f} m"

def meter_to_centimeter(m: float):
    if m < 0:
        return None, "❌ Length cannot be negative."
    cm = m * 100
    return cm, f"{m:.4f} m = {cm:.4f} cm"
