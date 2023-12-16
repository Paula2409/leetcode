"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        """
        The function 'searchInsert' takes in a sorted list of integers 'nums' and a target integer
        'target', and returns the index where the target should be inserted in order to maintain the
        sorted order of the list.
        
        Args:
          nums ([int]): The 'nums' parameter is a list of integers that represents a sorted array.
          target (int): The target parameter is the number that we are searching for in the given list
        of numbers (nums).
        
        Returns:
          the index at which the target element should be inserted in the given sorted array.
        """
        
        left_index = 0
        right_index = len(nums) - 1
        
        while left_index <= right_index:
            
            middle = (left_index + right_index) // 2
            
            if nums[middle] == target:
                return middle
            
            elif nums[middle] < target:
                left_index = middle + 1
            
            else:
                right_index = middle - 1
            
        else:
            return left_index
        
solution = Solution()
print(solution.searchInsert([1,3,5,6], 5))
print(solution.searchInsert([1,3,5,6], 2))
print(solution.searchInsert([1,3,5,6], 7))