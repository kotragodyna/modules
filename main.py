import csv

from convector import temperature_1 as t, meters_convert as m


def read_file(data):
    with open(data, 'r') as infile:
        reader = csv.DictReader(infile)
        data = list(reader)
    return (data)


def write_file(data: list, outfile: str):
    with open(outfile, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(data)


def format_str(string: str) -> str:
    return f'"{string}'


def convert_temperature(temperature_str: str, target_unit: str):
    current_unit = temperature_str[-1:]
    if current_unit.lower() == target_unit.lower():
        return format_str(temperature_str)
    else:
        numbers_to_convert = int(temperature_str[:-2])
        if target_unit.lower() == 'c':
            converted_number = t.fahrenheit_to_celsius(numbers_to_convert)
            return format_str(f'{converted_number}C')
        elif target_unit.lower() == 'f':
            converted_number = t.celsius_to_fahrenheit(numbers_to_convert)
            return format_str(f'{converted_number}F')


def convert_distance(distance_str: str, target_unit: str) -> str:
    current_unit = distance_str[-1:]
    if current_unit.lower() == target_unit[-1:].lower():
        return distance_str
    else:
        if target_unit.lower() == 'm':
            numbers_to_convert = int(distance_str[:-2])
            converted_numbers = m.feet_to_meters(numbers_to_convert)
            return format_str(f'{converted_numbers}m')
        elif target_unit.lower() == 'ft':
            numbers_to_convert = int(distance_str[:-1])
            converted_numbers = m.meters_to_feet(numbers_to_convert)
            return format_str(f'{converted_numbers}ft')


def convert_units(data, distance_unit: str, temperature_unit: str):
    converted_data = []
    for row in data:
        converted_row = []
        if data.index(row) == 0:
            converted_data.append(row)
        else:
            Date, Temperature, Distance = row
            converted_row.append(row)
            converted_row.append(convert_temperature(Temperature, temperature_unit))
            converted_row.append(convert_distance(Distance, distance_unit))
            converted_data.append(converted_row)
    return converted_data

data = read_file("data.csv")
converted_data = convert_units(data, temperature_unit='C', distance_unit='m')
write_file(converted_data, 'outfile.csv')












