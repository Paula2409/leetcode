"""
First Unique Character

    The function takes a string 's' as input and returns the index of the first unique
    character in the string, or -1 if there are no unique characters.
    
    :param s(str): The parameter 's' is a string that represents the input string

    :return: the function returns the index of the first unique character in the given
    string 's'. If there are no unique characters, it returns -1.
    
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:

            
        hash_s = {}
            
        for letter in s:
            if letter in hash_s:
                hash_s[letter] = hash_s[letter] + 1
            else:
                hash_s[letter] = 1
            
        for h in hash_s:
            if hash_s[h] == 1:
                return s.index(h)
        return -1

solution = Solution()
print(solution.firstUniqChar('aabb'))