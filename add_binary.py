"""
Given two binary strings a and b, return their sum as a binary string.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        The function 'addBinary' takes two binary numbers as input, converts them to decimal, adds them
        together, and returns the sum as a binary number.
        
        Args:
          a (str): The parameter "a" is a string representing a binary number.
          b (str): The parameter "b" in the given code is a string representing a binary number.
        
        Returns:
          the sum of the binary numbers 'a' and 'b' as a binary string.
        """
        
        if a == "0" and b == "0":
            return "0"
        
        # Para recorrerlo, invertimos el orden
        a = a[::-1]
        b = b[::-1]

        # Convertimos a decimal
        result_a,result_b = 0,0
        for i in range(len(a)-1,-1,-1):
            result_a += int(a[i]) * 2**i
        
        
        for i in range(len(b)-1,-1,-1):
            result_b += int(b[i]) * 2**i
        
        result = (bin(result_a + result_b).lstrip("0b"))
        return result 
    
    
solution = Solution()
print(solution.addBinary("11", "1")) # 100    
print(solution.addBinary("1010", "1011")) # 10101     