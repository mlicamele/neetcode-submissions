# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        res = head
        t1 = head
        t1p = None
        t2 = head
        for i in range(left - 1):
            t1p = t1
            t1 = t1.next
        for i in range(right - 1):
            t2 = t2.next
        if left == 1:
            res = t2
        for i in range(right - left):
            temp = t2.next
            t2.next = t1
            t1 = t1.next
            t2.next.next = temp
        if left != 1:
            t1p.next = t1
        return res
