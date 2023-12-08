"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list."""

# Tags: Linked list - Recursion
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        list1 = ListNode()
        list2 = ListNode()
        curr = ListNode()
        head = curr
        if not list1 or not list2:
            return list1 or list2
        
        while list1 != None and list2 != None:
            
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            
            else:
                curr.next = list2
                list2 = list2.next 
            
            curr = curr.next 
        curr.next = list1 or list2
        return head.next  

solution = Solution()
print(solution.mergeTwoLists([1,2,4],[1,3,4]))
print(solution.mergeTwoLists([], []))
print(solution.mergeTwoLists([], [0]))