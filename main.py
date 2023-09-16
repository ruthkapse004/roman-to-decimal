# This is a program to convert roman numbers to decimal.

def RomanToDecimal(roman):
    n = len(roman)
    decimal = 0
    i = 0

    while (i < n):
        if (i != n-1 and values[roman[i]] < values[roman[i+1]]):
            decimal += values[roman[i+1]] - values[roman[i]]
            i += 2
        else:
            decimal += values[roman[i]]
            i += 1
    return decimal


if __name__ == "__main__":
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman = input("Enter roman Number: ").upper()

    while ("IIII" in roman):
        print("Invalid roman number.")
        roman = input("Enter roman Number: ").upper()

    print(values)
    print(f"Decimal value of {roman} number is", RomanToDecimal(roman))
