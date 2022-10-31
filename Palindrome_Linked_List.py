# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = []
        current_Node = head
        while current_Node is not None:
            tmp.append(current_Node.val)
            current_Node = current_Node.next
        return tmp == tmp[::-1]