# This is a program to convert roman numbers to decimal.
values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
print(values)


def RomanToDecimal(s):
    n = len(s)
    sum = 0
    i = 0

    while (i < n):
        if (i != n-1 and values[s[i]] < values[s[i+1]]):
            sum += values[s[i+1]] - values[s[i]]
            i += 2
        else:
            sum += values[s[i]]
            i += 1
    return sum


if __name__ == "__main__":
    roman = input("Enter roman Number: ").upper()
    print(f"Decimal value of {roman} number is", RomanToDecimal(roman))
