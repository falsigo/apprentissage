decimalKnownAs = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}


print(decimalKnownAs["1"])
print(decimalKnownAs.get("0"))
print(decimalKnownAs.get("11", "Not a valid decimal digit"))