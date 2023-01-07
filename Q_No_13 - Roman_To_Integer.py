# Link to the Problem : https://leetcode.com/problems/roman-to-integer/

import time

def romanToInt(s: str) -> int:
    integer_value = 0

    special_cases = ["IV", "IX", "XL", "XC", "CD", "CM"]

    roman_map = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    for each in special_cases:
        if each in s:
            s = s.replace(each, "")
            integer_value += roman_map[each]

    for each in s:
        integer_value += roman_map[each]

    return integer_value

"""
Another Solution :
 
integer_value = 0
    
def romanToInt(s: str) -> int:
        s = s.replace("IV", "IIII")\
        .replace("IX", "VIIII")\
        .replace("XL", "XXXX")\
        .replace("XC", "LXXXX")\
        .replace("CD", "CCCC")\
        .replace("CM", "DCCCC")
    
        roman_map = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
    
        for each in s:
            integer_value += roman_map[each]
    
        return integer_value
"""

def main():
    start = time.perf_counter()

    roman_value = input("Enter the roman value : ")

    print(romanToInt(roman_value))

    end = time.perf_counter()
    print(f"Total time taken : {end - start}")

if __name__ == "__main__":
    main()