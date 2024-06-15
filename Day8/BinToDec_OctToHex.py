#Write a program to convert Binary to Decimal and Octal to Hexadecimal
def binToDec(binV):
    n = len(binV)-1
    dec = 0
    for i in str(binV):
        if i == "1":
            dec += (2**n)
        n-=1
    return dec

print(binToDec("1001"))  