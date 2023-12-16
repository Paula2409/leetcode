"""You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        
        n = len(digits)
        
        if digits[-1] != 9:
            digits[-1] += 1
            
            return digits
        
        if  digits == [9]:
            return [1,0]
    
        for i in range(n-1,-1,-1):
            
            while digits[i] == 9:
                digits[i] = 0
                
                i -= 1
            
                if digits[i] != 9:
                    
                    if digits[0] == 0:
                        digits.insert(0,1)
                        return digits
                    
                    digits[i] += 1
                    return digits
        
        return digits
    
solution = Solution()
print(solution.plusOne([1,2,3]))
print(solution.plusOne([4,3,2,1]))
print(solution.plusOne([9]))
print(solution.plusOne([9,9,9]))
