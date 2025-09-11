#main.py(version ที่เชื่อมกับกับ Google sheet)
import importlib
from converter2 import temperature, weight, time, length, volume
import datetime
import gspread
import google.auth

# ==== Google Sheet setup ====
SPREADSHEET_NAME = "UnitConverterHistory"

creds, _ = google.auth.default()
gc = gspread.authorize(creds)

try:
    sh = gc.open(SPREADSHEET_NAME)
except gspread.SpreadsheetNotFound:
    sh = gc.create(SPREADSHEET_NAME)
    print(f"Created new spreadsheet: {SPREADSHEET_NAME}")
ws = sh.sheet1

# create header if empty
if not ws.get_all_values():
    header = ["id", "timestamp", "category", "from_unit", "to_unit", "input", "output", "message"]
    ws.append_row(header)

# ==== helper for saving ====
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

# ==== main loop ====
def run():
    record_id = 1
    while True:
        print("=== 🗿 Welcome to Unit Converter 🗿 ===")
        print("[1]🌡️ Fahrenheit → Celsius | °F → °C")
        print("[2]🌡️ Celsius → Fahrenheit | °C → °F")
        print("[3]🌡️ Celsius → Kelvin | °C → K")
        print("[4]🌡️ Kelvin → Celsius | K → °C")
        print("[5]⚖️ Kilogram → Pound | kg → lb")
        print("[6]⚖️ Pound → Kilogram | lb → kg")
        print("[7]⌚ Hours → Minutes | hr → min")
        print("[8]⌚ Minutes → Hours | min → hr")
        print("[9]⌚ Minutes → Seconds | min → sec")
        print("[10]⌚ Seconds → Minutes | sec → min")
        print("[11]📏 Meters → Kilometers | m → km")
        print("[12]📏 Kilometers → Meters | km → m")
        print("[13]📏 Centimeters → Meters | cm → m")
        print("[14]📏 Meters → Centimeters | m → cm")
        print("[15]🧪 Liters → Milliliters | L → mL")
        print("[16]🧪 Milliliters → Liters | mL → L")
        print("[17]🧪 Liters → Tablespoons | L → Tbsp")
        print("[18]🧪 Tablespoons → Liters | Tbsp → L")
        print("[19]🧪 Liters → Teaspoons | L → Tsp")
        print("[20]🧪 Teaspoons → Liters | Tsp → L")
        print("[21]🧪 Milliliters → Tablespoons | mL → Tbsp")
        print("[22]🧪 Tablespoons → Milliliters | Tbsp → mL")
        print("[23]🧪 Milliliters → Teaspoons | mL → Tsp")
        print("[24]🧪 Teaspoons → Milliliters | Tsp → mL")
        print("[25]🧪 Tablespoons → Teaspoons | Tbsp → Tsp")
        print("[26]🧪 Teaspoons → Tablespoons | Tsp → Tbsp")
        print("[27] Exit")
        print("====================================\n")

        try:
            choice = int(input("Choose your Choice: "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.\n")
            continue

        message = None
        result = None
        category = ""
        from_unit = ""
        to_unit = ""
        value = None

        try:
            if choice == 1:
                fr = float(input("Enter Fahrenheit: "))
                result, message = temperature.fahrenheit_to_celsius(fr)
                category, from_unit, to_unit, value = "temperature", "°F", "°C", fr
            elif choice == 2:
                c = float(input("Enter Celsius: "))
                result, message = temperature.celsius_to_fahrenheit(c)
                category, from_unit, to_unit, value = "temperature", "°C", "°F", c
            elif choice == 3:
                c = float(input("Enter Celsius: "))
                result, message = temperature.celsius_to_kelvin(c)
                category, from_unit, to_unit, value = "temperature", "°C", "K", c
            elif choice == 4:
                k = float(input("Enter Kelvin: "))
                result, message = temperature.kelvin_to_celsius(k)
                category, from_unit, to_unit, value = "temperature", "K", "°C", k
            elif choice == 5:
                kg = float(input("Enter Kilogram: "))
                result, message = weight.kilogram_to_pound(kg)
                category, from_unit, to_unit, value = "weight", "kg", "lb", kg
            elif choice == 6:
                lb = float(input("Enter Pound: "))
                result, message = weight.pound_to_kilogram(lb)
                category, from_unit, to_unit, value = "weight", "lb", "kg", lb
            elif choice == 7:
                hr = float(input("Enter Hours: "))
                result, message = time.hours_to_minutes(hr)
                category, from_unit, to_unit, value = "time", "hr", "min", hr
            elif choice == 8:
                minutes = float(input("Enter Minutes: "))
                result, message = time.minutes_to_hours(minutes)
                category, from_unit, to_unit, value = "time", "min", "hr", minutes
            elif choice == 9:
                minutes = float(input("Enter Minutes: "))
                result, message = time.minutes_to_seconds(minutes)
                category, from_unit, to_unit, value = "time", "min", "sec", minutes
            elif choice == 10:
                sec = float(input("Enter Seconds: "))
                result, message = time.seconds_to_minutes(sec)
                category, from_unit, to_unit, value = "time", "sec", "min", sec
            elif choice == 11:
                m = float(input("Enter Meters: "))
                result, message = length.meter_to_kilometer(m)
                category, from_unit, to_unit, value = "length", "m", "km", m
            elif choice == 12:
                km = float(input("Enter Kilometers: "))
                result, message = length.kilometer_to_meter(km)
                category, from_unit, to_unit, value = "length", "km", "m", km
            elif choice == 13:
                cm = float(input("Enter Centimeters: "))
                result, message = length.centimeter_to_meter(cm)
                category, from_unit, to_unit, value = "length", "cm", "m", cm
            elif choice == 14:
                m = float(input("Enter Meters: "))
                result, message = length.meter_to_centimeter(m)
                category, from_unit, to_unit, value = "length", "m", "cm", m
            elif choice == 15:
                l = float(input("Enter Liters: "))
                result, message = volume.liter_to_milliliter(l)
                category, from_unit, to_unit, value = "volume", "L", "mL", l
            elif choice == 16:
                ml = float(input("Enter Milliliters: "))
                result, message = volume.milliliter_to_liter(ml)
                category, from_unit, to_unit, value = "volume", "mL", "L", ml
            elif choice == 17:
                l = float(input("Enter Liters: "))
                result, message = volume.liter_to_tbsp(l)
                category, from_unit, to_unit, value = "volume", "L", "Tbsp", l
            elif choice == 18:
                tbsp = float(input("Enter Tablespoons: "))
                result, message = volume.tbsp_to_liter(tbsp)
                category, from_unit, to_unit, value = "volume", "Tbsp", "L", tbsp
            elif choice == 19:
                l = float(input("Enter Liters: "))
                result, message = volume.liter_to_tsp(l)
                category, from_unit, to_unit, value = "volume", "L", "Tsp", l
            elif choice == 20:
                tsp = float(input("Enter Teaspoons: "))
                result, message = volume.tsp_to_liter(tsp)
                category, from_unit, to_unit, value = "volume", "Tsp", "L", tsp
            elif choice == 21:
                ml = float(input("Enter Milliliters: "))
                result, message = volume.milliliter_to_tbsp(ml)
                category, from_unit, to_unit, value = "volume", "mL", "Tbsp", ml
            elif choice == 22:
                tbsp = float(input("Enter Tablespoons: "))
                result, message = volume.tbsp_to_milliliter(tbsp)
                category, from_unit, to_unit, value = "volume", "Tbsp", "mL", tbsp
            elif choice == 23:
                ml = float(input("Enter Milliliters: "))
                result, message = volume.milliliter_to_tsp(ml)
                category, from_unit, to_unit, value = "volume", "mL", "Tsp", ml
            elif choice == 24:
                tsp = float(input("Enter Teaspoons: "))
                result, message = volume.tsp_to_milliliter(tsp)
                category, from_unit, to_unit, value = "volume", "Tsp", "mL", tsp
            elif choice == 25:
                tbsp = float(input("Enter Tablespoons: "))
                result, message = volume.tbsp_to_tsp(tbsp)
                category, from_unit, to_unit, value = "volume", "Tbsp", "Tsp", tbsp
            elif choice == 26:
                tsp = float(input("Enter Teaspoons: "))
                result, message = volume.tsp_to_tbsp(tsp)
                category, from_unit, to_unit, value = "volume", "Tsp", "Tbsp", tsp
            elif choice == 27:
                print("Exiting the converter. 👋 Goodbye!\n")
                break
            else:
                print("❌ Invalid choice. Please select a valid number.\n")
                continue
        except ValueError:
            print("❌ Invalid input! Please enter a number.\n")
            continue

        print(message, "\n")

        # save history
        if category and message:
            save_conversion_to_sheet(
                record_id,
                category,
                from_unit,
                to_unit,
                value,
                result,
                message
            )
            record_id += 1

if __name__ == "__main__":
    run()
