class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(head, size):
            prev = None
            curr = head
            for i in range(size):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        size = 2
        if head == None:
            return head
        left = head
        res = None
        prevleft = None
        while True:
            right = left
            for i in range(0, size - 1):
                if right == None:
                    break
                right = right.next
            if right:
                nextleft = right.next
                rev(left, size)
                if prevleft:
                    prevleft.next = right
                else:
                    res = right
                prevleft = left
                left = nextleft
            else:
                if prevleft:
                    prevleft.next = left
                else:
                    res = left    
                break
        return res