#parser
%%writefile converter3/parser.py
import re
from converter3.temperature import *
from converter3.weight import *
from converter3.time_converter import *
from converter3.length import *
from converter3.volume import *

def parse_input(user_input: str):
    user_input = user_input.strip().lower()
    match = re.match(r"([-+]?[0-9]*\.?[0-9]+)\s*([a-z]+)", user_input)
    if not match:
        return None, None, None, "❌ Invalid format. Example: 20C, 5kg, 10m"

    value, unit = match.groups()
    value = float(value)

    # Temperature
    if unit in ["c", "°c"]:
        return "temperature", "c", value, ""
    if unit in ["f", "°f"]:
        return "temperature", "f", value, ""
    if unit in ["k"]:
        return "temperature", "k", value, ""

    # Weight
    if unit in ["kg"]:
        if value < 0: return "weight", unit, value, "❌ Weight cannot be negative."
        return "weight", "kg", value, ""
    if unit in ["lb"]:
        if value < 0: return "weight", unit, value, "❌ Weight cannot be negative."
        return "weight", "lb", value, ""

    # Time
    if unit in ["hr", "h"]:
        if value < 0: return "time", unit, value, "❌ Time cannot be negative."
        return "time", "hr", value, ""
    if unit in ["min"]:
        if value < 0: return "time", unit, value, "❌ Time cannot be negative."
        return "time", "min", value, ""
    if unit in ["sec", "s"]:
        if value < 0: return "time", unit, value, "❌ Time cannot be negative."
        return "time", "sec", value, ""

    # Length
    if unit in ["m"]:
        if value < 0: return "length", unit, value, "❌ Length cannot be negative."
        return "length", "m", value, ""
    if unit in ["km"]:
        if value < 0: return "length", unit, value, "❌ Length cannot be negative."
        return "length", "km", value, ""
    if unit in ["cm"]:
        if value < 0: return "length", unit, value, "❌ Length cannot be negative."
        return "length", "cm", value, ""

    # Volume
    if unit in ["l"]:
        if value < 0: return "volume", unit, value, "❌ Volume cannot be negative."
        return "volume", "l", value, ""
    if unit in ["ml"]:
        if value < 0: return "volume", unit, value, "❌ Volume cannot be negative."
        return "volume", "ml", value, ""
    if unit in ["tbsp"]:
        if value < 0: return "volume", unit, value, "❌ Volume cannot be negative."
        return "volume", "tbsp", value, ""
    if unit in ["tsp"]:
        if value < 0: return "volume", unit, value, "❌ Volume cannot be negative."
        return "volume", "tsp", value, ""

    return None, None, None, "❌ Unknown unit."
