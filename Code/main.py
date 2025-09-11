import converter

while True:
    print("=== 🗿 Welcome to Unit Converter 🗿 ===")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Celsius to Kelvin")
    print("4. Kilogram to Pound")
    print("5. Pound to Kilogram")
    print("6. Exit")
    print("====================================\n")

    try:
        choice = int(input("Choose your Choice: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.\n")
        continue

    if choice == 1:
        fr = float(input("Enter Fahrenheit: "))
        result, message = converter.fahrenheit_to_celsius(fr)
        print(message, "\n")

    elif choice == 2:
        c = float(input("Enter Celsius: "))
        result, message = converter.celsius_to_fahrenheit(c)
        print(message, "\n")

    elif choice == 3:
        c = float(input("Enter Celsius: "))
        result, message = converter.celsius_to_kelvin(c)
        print(message, "\n")

    elif choice == 4:
        kg = float(input("Enter Kilogram: "))
        result, message = converter.kilogram_to_pound(kg)
        print(message, "\n")

    elif choice == 5:
        lb = float(input("Enter Pound: "))
        result, message = converter.pound_to_kilogram(lb)
        print(message, "\n")

    elif choice == 6:
        print("Exiting the converter. Goodbye!\n")
        break

    else:
        print("❌ Invalid choice. Please select between 1–6.\n")
