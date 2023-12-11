"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        The function 'strStr' takes in two strings, 'haystack' and 'needle', and returns the index of the
        first occurrence of 'needle' in 'haystack', or -1 if 'needle' is not found.
        
        Args:
          haystack (str): The 'haystack' parameter is a string that represents the main string in which we
        want to find the occurrence of the 'needle' string.
          needle (str): The 'needle' parameter is a string that we are searching for within the 'haystack'
        string.
        
        Returns:
          the index of the first occurrence of the needle in the haystack string. If the needle is not found
        in the haystack, it returns -1.
        """
        i = 0

        while i < len(haystack):
            if haystack[i:(i+len(needle))] == needle:
                return i
            i += 1
        
        return -1
    
solution = Solution()
print(solution.strStr("sadbutsad", "sad"))
print(solution.strStr("leetcode", "leeto"))

