# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        dummy=ListNode(0)  
        dummy.next=head  
        before=dummy
        pos=1
        t=head
        while pos<left:
            before=t
            t=t.next
            pos+=1
            continue
        curr=t
        prev=None
        times=right-left+1
        while(times>0):
            nxt=curr.next 
            curr.next=prev
            prev=curr
            curr=nxt
            times-=1
        t.next=curr
        before.next=prev
        return dummy.next    

        