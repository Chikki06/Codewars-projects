#Problem Statement
# Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.
#
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
#
# Input range : 1 <= n < 4000
#
# In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
#
# Examples
# RomanNumerals.to_roman(1000) # should return 'M'
# RomanNumerals.from_roman('M') # should return 1000
#
# Symbol Value
# I	1
# IV 4
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000
#
#Code


class RomanNumerals:

    def to_roman(val):

        num = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  val > 0:
            for x in range(val // num[i]):
                roman_num += syb[i]
                val -= num[i]
            i += 1
        return roman_num
