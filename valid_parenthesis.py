"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""

# Tags: string - stack
class Solution:
    def isValid(self, s: str) -> bool:
        """
        The function checks if a given string of parentheses, brackets, and braces is valid by using a stack
        to keep track of opening symbols and popping them when a corresponding closing symbol is
        encountered.
        
        Args:
          s (str): The parameter 's' is a string that represents a sequence of parentheses, brackets, and
        braces. The function 'isValid' checks if the sequence is valid, meaning that every opening
        parenthesis, bracket, or brace has a corresponding closing parenthesis, bracket, or brace in the
        correct order.
        
        Returns:
          a boolean value indicating whether the input string 's' is valid or not.
        """
        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False
        if s[-1] == '(' or s[-1] == '[' or s[-1] == '{':
            return False
        
        if len(s) % 2 != 0:
            return False
        
        s_list = []
        
        for i in s:
            if len(s_list) > 0 and (i == ')' and s_list[-1] == '(' or i == ']' and s_list[-1] == '[' or i == '}' and s_list[-1] == '{'):
                s_list.pop()
            else:
                s_list.append(i)

        if s_list == []:
            return True

        return False
    
solution = Solution()
print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("()[{}]"))
print(solution.isValid("(])"))
print(solution.isValid("[])"))
print(solution.isValid("[])))"))
print(solution.isValid("([}}])"))


