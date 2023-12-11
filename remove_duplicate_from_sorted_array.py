"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

"""

class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        k = 1
        
        for i in range(1,len(nums)):
            
            if nums[i] != nums[i-1]:
                
                nums[k]  = nums[i]
                
                
                k += 1
        
        return k



solution = Solution()
print(solution.removeDuplicates([1,1,2]))
print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

