# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        a = float('inf')
        b = -1

        node = head
        small = False
        big = False
        first = -1
        idx = -1
        prev = -1
        count = 0

        while node:
            if prev != -1:
                if node.val < prev:
                    if big:
                        if first == -1:
                            first = count
                        if idx != -1:
                            a = min(a, count - idx)
                        idx = count
                    small = True
                    big = False
                elif node.val > prev:
                    if small:
                        if first == -1:
                            first = count
                        if idx != -1:
                            a = min(a, count - idx)
                        idx = count
                    small = False
                    big = True
                elif node.val == prev:
                    small = False
                    big = False

            prev = node.val
            node = node.next
            count += 1

        b = max(b, idx - first)
        if b == 0: b = -1
        if a == float('inf'): a = -1

        return [a, b]
            
        