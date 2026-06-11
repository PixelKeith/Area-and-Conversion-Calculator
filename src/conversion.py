def convert_units(value, current_unit, units_dict):

    base_value = value * units_dict[current_unit]

    converted_results = {}
    for target_unit, target_factor in units_dict.items():
        converted_results[target_unit] = base_value / target_factor

    return converted_results

def length_converter(value, current_unit):
    units = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1.0,
        "km": 1000.0,
        "mi": 1609.34,
        "yd": 0.9144,
        "ft": 0.3048,
        "inch": 0.0254
    }
    return convert_units(value, current_unit, units)

def mass_converter(value, current_unit):
    units = {
        "mg": 0.001,
        "g": 1.0,
        "kg": 1000.0,
        "t": 1000000.0,
        "oz": 28.3495,
        "lb": 453.592,
        "st": 6350.29
    }
    return convert_units(value, current_unit, units)

def speed_converter(value, current_unit):
    units = {
        "m/s": 1.0,
        "ft/s": 0.3048,
        "mi/h": 0.44704,
        "km/h": 0.277778
    }
    return convert_units(value, current_unit, units)

def time_converter(value, current_unit):
    units = {
        "sec": 1.0,
        "min": 60.0,
        "hr": 3600.0,
        "day": 86400.0,
        "week": 604800.0,
        "month": 2628000.0,
        "year": 31536000.0
    }
    return convert_units(value, current_unit, units)

def volume_converter(value, current_unit):
    units = {
        "ml": 0.001,
        "cl": 0.01,
        "dl": 0.1,
        "l": 1.0,
        "m3": 1000.0,
        "cm3": 0.001,
        "in3": 0.0163871,
        "ft3": 28.3168
    }
    return convert_units(value, current_unit, units)

def temp_converter(value, current_unit):
    if current_unit == "c":
        celsius = value
    elif current_unit == "f":
        celsius = (value - 32) * 5 / 9
    elif current_unit == "k":
        celsius = value - 273.15
    else:
        return {}

    return {
        "c": celsius,
        "f": (celsius * 9 / 5) + 32,
        "k": celsius + 273.15
    }