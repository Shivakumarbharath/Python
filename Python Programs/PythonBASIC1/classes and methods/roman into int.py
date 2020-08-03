def romantoint():
    roman = {
        "M": 1000, "CM": 900, "D": 500, "CD": 400,
        "C": 100, "XC": 90, "L": 50, "XL": 40,
        "X": 10, "IX": 9, "V": 5, "IV": 4,
        "I": 1,
        " ": 0
    }
    rom = input('enter the roman number')
    rom += ' '
    intnum = 0
    for R in range(0, len(rom) - 1):
        if roman[rom[R]] >= roman[rom[R + 1]]:
            intnum += roman[rom[R]]
            # print(rom[R])

        if roman[rom[R]] < roman[rom[R + 1]]:
            rand = rom[R:R + 2]
            # print(rand)
            intnum = intnum + roman[rand] - roman[rom[R + 1]]
            # print(R)
            # print(intnum)
    return intnum


print(romantoint())
