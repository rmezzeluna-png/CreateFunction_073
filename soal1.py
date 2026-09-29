

def convert_temperature (value, unit):
    if (unit == 'C'):
        return (value * 9 / 5) + 32
    elif (unit == 'F'):
        return (value - 32) * 5 / 9
    else:
        print("unit harus 'C' atau 'F'") 

print("------ KONVERSI SUHU ------")

input_value = float(input("masukkan value: "))
input_unit = input("masukkan unit (C/F): ")
konversi = convert_temperature(input_value, input_unit)
if (input_unit == 'C'):
    print(f"{input_value} derajat Celsius = {konversi} derajat Fahrenheit")
elif (input_unit == 'F'):
    print(f"{input_value} derajat Fahrenheit = {konversi} derajat Celsius")
