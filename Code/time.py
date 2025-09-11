# time.py
%%writefile converter2/time.py
def hours_to_minutes(hr: float):
    if hr < 0:
        return None, "❌ Time cannot be negative."
    minutes = hr * 60
    return minutes, f"{hr:.4f} hr = {minutes:.4f} min"

def minutes_to_hours(minutes: float):
    if minutes < 0:
        return None, "❌ Time cannot be negative."
    hr = minutes / 60
    return hr, f"{minutes:.4f} min = {hr:.4f} hr"

def minutes_to_seconds(minutes: float):
    if minutes < 0:
        return None, "❌ Time cannot be negative."
    sec = minutes * 60
    return sec, f"{minutes:.4f} min = {sec:.4f} sec"

def seconds_to_minutes(sec: float):
    if sec < 0:
        return None, "❌ Time cannot be negative."
    minutes = sec / 60
    return minutes, f"{sec:.4f} sec = {minutes:.4f} min"
