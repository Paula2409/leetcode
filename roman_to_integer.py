"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""
# tags: hash table - math - string
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        The function 'romanToInt' takes a string representing a Roman numeral and returns its
        corresponding integer value.
        
        Args:
          s (str): The parameter 's' is a string representing a Roman numeral.
        
        Returns:
          an integer value, which represents the conversion of a Roman numeral string to its
        corresponding integer value.
        """
        roman_numbers = {'I': 1, 'V': 5, 'X': 10,'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_to_integer = 0
        i = len(s) - 1
        while i > 0:
        
            if roman_numbers[s[i]] > roman_numbers[s[i-1]]:
                roman_to_integer += roman_numbers[s[i]] - roman_numbers[s[i-1]]
                i -= 2
            else:
                roman_to_integer += roman_numbers[s[i]]
                i -= 1
        
        if i == 0:
            return roman_to_integer + roman_numbers[s[0]]
        else:
            return roman_to_integer
        
                
    


solution = Solution()
# Tests
print(solution.romanToInt("III"))
print(solution.romanToInt("LVIII"))
print(solution.romanToInt("MCMXCIV"))

