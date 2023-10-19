
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        arr1 = []
        while curr != None:
            arr1.append(curr.val)
            curr = curr.next

        curr = l2
        arr2 = []
        while curr != None:
            arr2.append(curr.val)
            curr = curr.next

        result = None
        carry = 0
        while arr1 or arr2 or carry:
            val1 = arr1.pop() if arr1 else 0
            val2 = arr2.pop() if arr2 else 0

            carry, val = divmod(val1 + val2+ carry, 10)

            new_node = ListNode(val)
            new_node.next = result
            result = new_node

        return result or ListNode(0) 
