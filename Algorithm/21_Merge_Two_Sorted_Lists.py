# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        ret = cur = None
        if l1 == None and l2 == None:
            return ret
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            if l1.val < l2.val:
                ret = cur = l1
                l1 = l1.next
            else:
                ret = cur = l2
                l2 = l2.next
            while(l1 != None or l2 != None):
                if l1 == None:
                    cur.next = l2
                    l2 = l2.next
                elif l2 == None:
                    cur.next = l1
                    l1 = l1.next
                else:
                    if l1.val < l2.val:
                        cur.next  = l1
                        l1 = l1.next
                    else:
                        cur.next = l2
                        l2 = l2.next
                cur = cur.next
        return ret
