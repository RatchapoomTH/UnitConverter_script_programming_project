# time.py
%%writefile converter2/time.py
def hours_to_minutes(hr: float):
    minutes = hr * 60
    return minutes, f"{hr:.2f} hr = {minutes:.2f} min"

def minutes_to_hours(minutes: float):
    hr = minutes / 60
    return hr, f"{minutes:.2f} min = {hr:.2f} hr"

def minutes_to_seconds(minutes: float):
    sec = minutes * 60
    return sec, f"{minutes:.2f} min = {sec:.2f} sec"

def seconds_to_minutes(sec: float):
    minutes = sec / 60
    return minutes, f"{sec:.2f} sec = {minutes:.2f} min"
