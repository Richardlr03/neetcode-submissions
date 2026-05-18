# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = None
        prev = None

        while head:
            prev = cur
            cur = head
            head = head.next
            cur.next = prev

        return cur


        