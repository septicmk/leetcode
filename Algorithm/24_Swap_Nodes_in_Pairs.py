# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        cur = head;
        fir = True
        while( cur != None and cur.next != None):
            hand1 = cur
            hand2 = cur.next
            hand1.next = hand2.next
            hand2.next = hand1
            if fir:
                head, fir= hand2, False
            else:
                last.next = hand2
            last = cur
            cur = cur.next
        return head


