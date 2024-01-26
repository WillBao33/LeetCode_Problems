class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #roman_numerals = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
        roman_numerals_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

        total = 0
        prev_value = 0

        for symbol in s:
            value = roman_numerals_dict[symbol]

            if prev_value < value:
                total += value - 2*prev_value
            else:
                total += value
            
            prev_value = value

        return total
