#length.py
%%writefile converter3/length.py
def m_to_km(m: float):
    km = m / 1000
    return km, f"{m:.2f} m = {km:.2f} km"

def km_to_m(km: float):
    m = km * 1000
    return m, f"{km:.2f} km = {m:.2f} m"

def m_to_cm(m: float):
    cm = m * 100
    return cm, f"{m:.2f} m = {cm:.2f} cm"

def cm_to_m(cm: float):
    m = cm / 100
    return m, f"{cm:.2f} cm = {m:.2f} m"
