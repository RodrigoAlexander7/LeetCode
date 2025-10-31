#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
head = L1[i]

current = a -> L1[i] 
a -> L1[i] # head a
b -> L2[j] # head b
"""
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #using centinel node
        centinel = ListNode()
        tail = centinel # tail points to centine
        a = list1
        b = list2
        while a and b:
            if a.val > b.val:
                tail.next = b
                b = b.next
            else:
                tail.next = a
                a = a.next
            tail = tail.next    # points the last elemnt
        tail.next = a if a else b
            
        return centinel.next
    

    
            
             

                
        
        

        
# @lc code=end

