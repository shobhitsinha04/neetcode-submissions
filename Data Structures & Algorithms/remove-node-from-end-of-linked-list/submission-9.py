# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        dummy = ListNode(0, prev)
        curr = dummy

        for _ in range(n-1):
            curr = curr.next
        curr.next = curr.next.next 

        curr = dummy.next
        prev_new = None
        while curr:
            temp_new = curr.next
            curr.next = prev_new
            prev_new = curr
            curr = temp_new
        
        return prev_new



        # count = 0 
        # curr = head
        # while curr:
        #     count += 1
        #     curr = curr.next
        
        # remidx = count - n 
        # if remidx == 0:
        #     return head.next
        # curr = head
        # for i in range(count-1):
        #     if i+1 == remidx:
        #         curr.next = curr.next.next
        #         break
        #     curr = curr.next
        
        # return head