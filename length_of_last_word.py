"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s_list = []
        # string_in_s = ""
        # for i in range(len(s)):
        #     if s[i] != " ":
        #         string_in_s += s[i]
        #     else:
        #         s_list.append(string_in_s)
        #         string_in_s = ""
        # s_list.append(string_in_s) 
        
        # Eliminamos espacios finales
        if len(s) == 1 and s[0] != " ":
            return 1
        
        counter = 0
        while s[-1] == " ":
            s = s[0:-1]
        
        # Recorremos ultima palabra   
        i = len(s) - 1
        while s[i] != " " and i >= 0:
            counter += 1
            i -= 1
        else:        
            return counter

solution = Solution()
print(solution.lengthOfLastWord("Hello World"))
print(solution.lengthOfLastWord("   fly me   to   the moon  "))
print(solution.lengthOfLastWord("luffy is still joyboy"))
print(solution.lengthOfLastWord("a"))
print(solution.lengthOfLastWord("a "))