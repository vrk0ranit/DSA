# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k==0:
            return head
        curr=head
        n=1
        while curr.next:
            curr=curr.next
            n+=1
        k=k%n
        if k==0:
            return head
        curr.next=head
        steps=n-k
        curr=head
        for __ in range(steps-1):
            curr=curr.next
        new_head=curr.next
        curr.next=None
        return new_head              
        