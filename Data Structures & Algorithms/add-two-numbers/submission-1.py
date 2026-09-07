# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = (l1.val + l2.val) % 10
        r = (l1.val + l2.val) // 10
        result = ListNode(s)
        res = result
        l1 = l1.next
        l2 = l2.next

        while l1 is not None and l2 is not None:
            s = (l1.val + l2.val + r) % 10
            r = (l1.val + l2.val + r) // 10
            res.next = ListNode(s)
            l1 = l1.next
            l2 = l2.next
            res = res.next
        
        if l1 is None:
            while l2 is not None:
                s = (l2.val + r) % 10
                r = (l2.val + r) // 10
                res.next = ListNode(s)
                l2 = l2.next
                res = res.next
        elif l2 is None:
            while l1 is not None:
                s = (l1.val + r) % 10
                r = (l1.val + r) // 10
                res.next = ListNode(s)
                l1 = l1.next
                res = res.next
        
        if r > 0:
            res.next = ListNode(r)

        return result

        # Create q with listnode of sum: l1.val + l2.val % 10
        # Create dummy q to iterate during assignment
        # Store carry value: l1.val + l2.val // 10

        # Iterate through l1 and l2 until one is None
        # Set next of res (dummy) to listnode of sum: l1.val + l2.val % 10
        # Store carry value: l1.val + l2.val // 10
        # l1 = l1.next and l2 = l2.next

        # Empty both l1 and l2, whichever wasn't none into res
        # Set next of res (dummy) to listnode of sum: l.val % 10
        # Store carry value: l.val // 10
        # Add last r to res

        # Return result