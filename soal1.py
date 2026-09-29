

def convert_temperature (value, unit):
    if (unit.upper == 'c'):
        return (value * 9 / 5) + 32
    elif (unit.upper == 'f'):
        return (value - 32) * 5 / 9
    else:
        print("unit harus 'C' atau 'F'") 

