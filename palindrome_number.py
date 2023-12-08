""" Given an integer x, return true if x is a palindrome, and false otherwise. """
# tags: Math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        The function checks if a given integer is a palindrome by reversing the digits of the integer and
        comparing it to the original integer.
        
        Args:
          x (int): An integer that we want to check if it is a palindrome.
        
        Returns:
          The function isPalindrome returns a boolean value indicating whether the input integer x is a
        palindrome or not.
        """
        
        number_reverse = 0
        x_modified = x
        
        while x_modified > 0:
            last_index = x_modified % 10
            number_reverse = number_reverse * 10 + last_index
            x_modified = x_modified // 10
        
        if x == number_reverse:    
            return True
        return False
        
solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))

# Another solution with str()
        # x = str(x)
        # if x == x[::-1]:
        #     return True
        # return False