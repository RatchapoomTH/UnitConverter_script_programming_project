#main.py
import datetime
from converter2 import parser

record_id = 1

def save_conversion_to_sheet(record_id, category, from_unit, to_unit, input_val, output_val, message=""):
    ts = datetime.datetime.utcnow().isoformat()
    row = [
        record_id,
        ts,
        category,
        from_unit,
        to_unit,
        input_val,
        output_val,
        message
    ]
    ws.append_row(row)
    print("✅ Saved to Google Sheet.")

print("=== 🗿 Welcome to Unit Converter 🗿 ===")
print("[🌡️] C, F, K | [⚖️] kg, lb | [⌚] hr, min, sec | [📏] m, km, cm | [🧪] L, mL, Tbsp, Tsp")
print("Example inputs: 20C, 5kg, 10m, 3hr, 100ml")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("Enter value with unit: ").strip()
    if user_input.lower() in ["exit", "quit", "q"]:
        print("👋 Goodbye!")
        break

    value, category, from_unit, to_unit, message = parser.parse_input(user_input)
    print(message, "\n")

    if value is not None:
        save_conversion_to_sheet(record_id, category, from_unit, to_unit, value, "see message", message)
        record_id += 1
