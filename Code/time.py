#time_converter.py
%%writefile converter3/time_converter.py
def hr_to_min(hr: float):
    m = hr * 60
    return m, f"{hr:.4f} hr = {m:.4f} min"

def min_to_hr(m: float):
    hr = m / 60
    return hr, f"{m:.4f} min = {hr:.4f} hr"

def min_to_sec(m: float):
    s = m * 60
    return s, f"{m:.4f} min = {s:.4f} sec"

def sec_to_min(s: float):
    m = s / 60
    return m, f"{s:.4f} sec = {m:.4f} min"
