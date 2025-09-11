#main.py
from converter2 import temperature, weight, time, length

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
    print("[15] Exit")
    print("====================================\n")

    try:
        choice = int(input("Choose your Choice: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.\n")
        continue

    #Temperature
    if choice == 1:
        fr = float(input("Enter Fahrenheit: "))
        _, message = temperature.fahrenheit_to_celsius(fr)
    elif choice == 2:
        c = float(input("Enter Celsius: "))
        _, message = temperature.celsius_to_fahrenheit(c)
    elif choice == 3:
        c = float(input("Enter Celsius: "))
        _, message = temperature.celsius_to_kelvin(c)
    elif choice == 4:
        k = float(input("Enter Kelvin: "))
        _, message = temperature.kelvin_to_celsius(k)
    #Weight
    elif choice == 5:
        kg = float(input("Enter Kilogram: "))
        _, message = weight.kilogram_to_pound(kg)
    elif choice == 6:
        lb = float(input("Enter Pound: "))
        _, message = weight.pound_to_kilogram(lb)
    #Time
    elif choice == 7:
        hr = float(input("Enter Hours: "))
        _, message = time.hours_to_minutes(hr)
    elif choice == 8:
        minutes = float(input("Enter Minutes: "))
        _, message = time.minutes_to_hours(minutes)
    elif choice == 9:
        minutes = float(input("Enter Minutes: "))
        _, message = time.minutes_to_seconds(minutes)
    elif choice == 10:
        sec = float(input("Enter Seconds: "))
        _, message = time.seconds_to_minutes(sec)
    #Length
    elif choice == 11:
        m = float(input("Enter Meters: "))
        _, message = length.meter_to_kilometer(m)
    elif choice == 12:
        km = float(input("Enter Kilometers: "))
        _, message = length.kilometer_to_meter(km)
    elif choice == 13:
        cm = float(input("Enter Centimeters: "))
        _, message = length.centimeter_to_meter(cm)
    elif choice == 14:
        m = float(input("Enter Meters: "))
        _, message = length.meter_to_centimeter(m)
    #Exit
    elif choice == 15:
        print("Exiting the converter. 👋 Goodbye!\n")
        break
    else:
        print("❌ Invalid choice. Please select a valid number.\n")
        continue

    print(message, "\n")
