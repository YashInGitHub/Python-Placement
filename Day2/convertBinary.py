n = int(input())

def binToDec(n):
    i = 0
    dec = 0
    while(n != 0):
        m = n % 10
        dec += m * (2**i)
        n = n // 10
        i += 1
    return dec

def binToOct(n):
    oct = 0
    i = 0
    while(n != 0):
        m = n % 1000
        oct = oct + (binToDec(m) * (10**i))
        n = n // 1000
        i +=1
    return oct

def convert_to_hex(number):
    match number:
        case 10:
            return "A"
        case 11:
            return "B"
        case 12:
            return "C"
        case 13:
            return "D"
        case 14:
            return "E"
        case 15:
            return "F"
        case _:
            return "Invalid number. Please enter a number between 10 and 15."
#110110110
def binToHex(n):
    i = 0
    hex = ""
    while(n != 0):
        m = n % 10000

        hexVal = binToDec(m)

        if hexVal > 9:
            hexValAlpha = convert_to_hex(hexVal)
            hex = hexValAlpha + hex
        else:
            hex = str(hexVal) + hex

        n = n // 10000
        i +=1
    return hex

print("Decimal: ", binToDec(n))
print("Octal: ", binToOct(n))
print("Hexadecimal: ", binToHex(n))
