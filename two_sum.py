"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

# Tags: array - hash table

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        """
        The function 'twoSum' takes in a list of integers 'nums' and a target integer 'target', and returns
        a pair of indices from 'nums' whose corresponding values add up to 'target'.
        
        Args:
          nums ([int]): A list of integers
          target (int): The target parameter is an integer representing the desired sum of two numbers in
        the given list.
        
        Returns:
          a tuple containing the indices of the two numbers in the input list 'nums' that add up to the
        target value. If no such pair is found, it returns 'None'.
        """
   
        my_dict = {}
        
        for i in range(len(nums)):
            x = target - nums[i]
            
            if x in my_dict:
                return my_dict[x],i
            else:
                my_dict[nums[i]] = i
        return None


solution = Solution()
print(solution.twoSum([3,2,4], 6))