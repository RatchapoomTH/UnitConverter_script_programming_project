#parser.py
%%writefile converter2/parser.py
import re
from . import temperature, weight, time, length, volume

def parse_input(user_input: str):
    pattern = r"^\s*(-?\d+(\.\d+)?)\s*([a-zA-Z]+)\s*$"
    match = re.match(pattern, user_input.strip())
    if not match:
        return None, None, None, None, "❌ Invalid format. Example: 20C, 5kg, 10m"

    value = float(match.group(1))
    unit = match.group(3).lower()

    # Allow negative only for temperature
    temperature_units = ["c", "°c", "celsius", "f", "°f", "fahrenheit", "k", "kelvin"]
    if value < 0 and unit not in temperature_units:
        return None, None, None, None, "❌ [⚖️]Weight, [📏]Length, [⌚]Time & [🧪]Volume cannot be negative."

    # Temperature
    if unit in ["c", "°c", "celsius"]:
        f, msg1 = temperature.celsius_to_fahrenheit(value)
        k, msg2 = temperature.celsius_to_kelvin(value)
        return value, "temperature", "C", "F/K", f"Input: {value} °C\n→ {msg1}\n→ {msg2}"
    if unit in ["f", "°f", "fahrenheit"]:
        c, msg1 = temperature.fahrenheit_to_celsius(value)
        k, msg2 = temperature.celsius_to_kelvin(c)
        return value, "temperature", "F", "C/K", f"Input: {value} °F\n→ {msg1}\n→ {msg2}"
    if unit in ["k", "kelvin"]:
        c, msg1 = temperature.kelvin_to_celsius(value)
        f, msg2 = temperature.celsius_to_fahrenheit(c)
        return value, "temperature", "K", "C/F", f"Input: {value} K\n→ {msg1}\n→ {msg2}"

    # Weight
    if unit in ["kg", "kilogram"]:
        lb, msg = weight.kilogram_to_pound(value)
        return value, "weight", "kg", "lb", msg
    if unit in ["lb", "pound"]:
        kg, msg = weight.pound_to_kilogram(value)
        return value, "weight", "lb", "kg", msg

    # Length
    if unit in ["m", "meter", "meters"]:
        km, msg1 = length.meter_to_kilometer(value)
        cm, msg2 = length.meter_to_centimeter(value)
        return value, "length", "m", "km/cm", f"Input: {value} m\n→ {msg1}\n→ {msg2}"
    if unit in ["km", "kilometer"]:
        m, msg = length.kilometer_to_meter(value)
        return value, "length", "km", "m", msg
    if unit in ["cm", "centimeter"]:
        m, msg = length.centimeter_to_meter(value)
        return value, "length", "cm", "m", msg

    # Time
    if unit in ["hr", "hour", "hours"]:
        mins, msg = time.hours_to_minutes(value)
        return value, "time", "hr", "min", msg
    if unit in ["min", "mins", "minute", "minutes"]:
        hr, msg1 = time.minutes_to_hours(value)
        sec, msg2 = time.minutes_to_seconds(value)
        return value, "time", "min", "hr/sec", f"Input: {value} min\n→ {msg1}\n→ {msg2}"
    if unit in ["sec", "second", "seconds"]:
        mins, msg = time.seconds_to_minutes(value)
        return value, "time", "sec", "min", msg

    # Volume
    if unit in ["l", "liter", "liters"]:
        ml, msg1 = volume.liter_to_milliliter(value)
        tbsp, msg2 = volume.liter_to_tbsp(value)
        tsp, msg3 = volume.liter_to_tsp(value)
        return value, "volume", "L", "mL/Tbsp/Tsp", f"Input: {value} L\n→ {msg1}\n→ {msg2}\n→ {msg3}"
    if unit in ["ml", "milliliter", "milliliters"]:
        l, msg1 = volume.milliliter_to_liter(value)
        tbsp, msg2 = volume.milliliter_to_tbsp(value)
        tsp, msg3 = volume.milliliter_to_tsp(value)
        return value, "volume", "mL", "L/Tbsp/Tsp", f"Input: {value} mL\n→ {msg1}\n→ {msg2}\n→ {msg3}"
    if unit in ["tbsp", "tablespoon"]:
        l, msg1 = volume.tbsp_to_liter(value)
        ml, msg2 = volume.tbsp_to_milliliter(value)
        tsp, msg3 = volume.tbsp_to_tsp(value)
        return value, "volume", "Tbsp", "L/mL/Tsp", f"Input: {value} Tbsp\n→ {msg1}\n→ {msg2}\n→ {msg3}"
    if unit in ["tsp", "teaspoon"]:
        l, msg1 = volume.tsp_to_liter(value)
        ml, msg2 = volume.tsp_to_milliliter(value)
        tbsp, msg3 = volume.tsp_to_tbsp(value)
        return value, "volume", "Tsp", "L/mL/Tbsp", f"Input: {value} Tsp\n→ {msg1}\n→ {msg2}\n→ {msg3}"

    return None, None, None, None, "❌ Unsupported unit. Try: C, F, K, kg, lb, m, km, cm, hr, min, sec, L, mL, Tbsp, Tsp"
