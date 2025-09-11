# main.py
import importlib
from converter2 import temperature, weight, time, length, volume
importlib.reload(volume)

def get_number_input(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("❌ Invalid input! Please enter a number.\n")

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

    # Temperature (สามารถติดลบได้)
    if choice == 1:
        fr = get_number_input("Enter Fahrenheit: ")
        _, message = temperature.fahrenheit_to_celsius(fr)
    elif choice == 2:
        c = get_number_input("Enter Celsius: ")
        _, message = temperature.celsius_to_fahrenheit(c)
    elif choice == 3:
        c = get_number_input("Enter Celsius: ")
        _, message = temperature.celsius_to_kelvin(c)
    elif choice == 4:
        k = get_number_input("Enter Kelvin: ")
        _, message = temperature.kelvin_to_celsius(k)

    # Weight (ห้ามติดลบ)
    elif choice == 5:
        kg = get_number_input("Enter Kilogram: ")
        _, message = weight.kilogram_to_pound(kg)
    elif choice == 6:
        lb = get_number_input("Enter Pound: ")
        _, message = weight.pound_to_kilogram(lb)

    # Time (ห้ามติดลบ)
    elif choice == 7:
        hr = get_number_input("Enter Hours: ")
        _, message = time.hours_to_minutes(hr)
    elif choice == 8:
        minutes = get_number_input("Enter Minutes: ")
        _, message = time.minutes_to_hours(minutes)
    elif choice == 9:
        minutes = get_number_input("Enter Minutes: ")
        _, message = time.minutes_to_seconds(minutes)
    elif choice == 10:
        sec = get_number_input("Enter Seconds: ")
        _, message = time.seconds_to_minutes(sec)

    # Length (ห้ามติดลบ)
    elif choice == 11:
        m = get_number_input("Enter Meters: ")
        _, message = length.meter_to_kilometer(m)
    elif choice == 12:
        km = get_number_input("Enter Kilometers: ")
        _, message = length.kilometer_to_meter(km)
    elif choice == 13:
        cm = get_number_input("Enter Centimeters: ")
        _, message = length.centimeter_to_meter(cm)
    elif choice == 14:
        m = get_number_input("Enter Meters: ")
        _, message = length.meter_to_centimeter(m)

    # Volume (ห้ามติดลบ)
    elif choice == 15:
        l = get_number_input("Enter Liters: ")
        _, message = volume.liter_to_milliliter(l)
    elif choice == 16:
        ml = get_number_input("Enter Milliliters: ")
        _, message = volume.milliliter_to_liter(ml)
    elif choice == 17:
        l = get_number_input("Enter Liters: ")
        _, message = volume.liter_to_tbsp(l)
    elif choice == 18:
        tbsp = get_number_input("Enter Tablespoons: ")
        _, message = volume.tbsp_to_liter(tbsp)
    elif choice == 19:
        l = get_number_input("Enter Liters: ")
        _, message = volume.liter_to_tsp(l)
    elif choice == 20:
        tsp = get_number_input("Enter Teaspoons: ")
        _, message = volume.tsp_to_liter(tsp)
    elif choice == 21:
        ml = get_number_input("Enter Milliliters: ")
        _, message = volume.milliliter_to_tbsp(ml)
    elif choice == 22:
        tbsp = get_number_input("Enter Tablespoons: ")
        _, message = volume.tbsp_to_milliliter(tbsp)
    elif choice == 23:
        ml = get_number_input("Enter Milliliters: ")
        _, message = volume.milliliter_to_tsp(ml)
    elif choice == 24:
        tsp = get_number_input("Enter Teaspoons: ")
        _, message = volume.tsp_to_milliliter(tsp)
    elif choice == 25:
        tbsp = get_number_input("Enter Tablespoons: ")
        _, message = volume.tbsp_to_tsp(tbsp)
    elif choice == 26:
        tsp = get_number_input("Enter Teaspoons: ")
        _, message = volume.tsp_to_tbsp(tsp)

    # Exit
    elif choice == 27:
        print("Exiting the converter. 👋 Goodbye!\n")
        break
    else:
        print("❌ Invalid choice. Please select a valid number.\n")
        continue

    print(message, "\n")
