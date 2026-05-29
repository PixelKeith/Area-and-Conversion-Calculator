import math

def convert_units(units):

    while True:
        try:
            value = float(input("\nEnter value: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    print("\nAvailable units:")

    for u in units:
        print(f"[{u}]")

    while True:

        unit = input("\nEnter unit: ").lower()

        if unit in units:
            break

        print("Invalid unit.")

    base_value = value * units[unit]

    print("\nConversions:")

    for name, factor in units.items():
        converted = base_value / factor
        print(f"{name}: {converted:.4f}")


def length_converter():
    units = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "mi": 1609.34,
        "yd": 0.9144,
        "ft": 0.3048,
        "inch": 0.0254
    }

    convert_units(units)

def mass_converter():
    units = {
        "mg": 0.001,
        "g": 1,
        "kg": 1000,
        "t": 1000000,
        "oz": 28.3495,
        "lb": 453.592,
        "st": 6350.29
    }

    convert_units(units)

def speed_converter():
    units = {
        "ft/s": 0.3048,
        "m/s": 1,
        "mi/h": 0.44704,
        "km/h": 0.277778,
    }

    convert_units(units)

def temp_converter():
    value = float(input("Enter temperature value: "))
    unit = input("Enter unit (c, f, k): ").lower()

    if unit == "c":
        celsius = value
    elif unit == "f":
        celsius = (value - 32) * 5/9
    elif unit == "k":
        celsius = value - 273.15
    else:
        print("Invalid unit.")
        return

    print("\nConversions:")

    print(f"c: {celsius:.2f}")

    fahrenheit = (celsius * 9/5) + 32
    print(f"f: {fahrenheit:.2f}")

    kelvin = celsius + 273.15
    print(f"k: {kelvin:.2f}")

def time_converter():
    units = {
        "sec" : 1/3600,
        "min" : 1/60,
        "hr" : 1,
        "day" : 24,
        "week" : 168,
        "month" : 730,
        "year" : 8760
    }

    convert_units(units)

def volume_converter():
    units = {
        "ml": 0.001,
        "cl": 0.01,
        "dl": 0.1,
        "l": 1,
        "m3": 1000,
        "cm3": 0.001,
        "in3": 0.0163871,
        "ft3": 28.3168
    }

    convert_units(units)