# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.n2l(self.l2n(l1)+self.l2n(l2))
    
    def l2n(self, l):
        t = l
        n = 0
        d = 0
        while t.next is not None:
            n += t.val * 10**d
            d += 1
            t = t.next
        n += t.val * 10**d
        return n
    
    def n2l(self, n):
        l = ListNode(n % 10)
        t = l
        for d in str(n)[-2::-1]:
            t.next = ListNode(int(d))
            t = t.next
        return l

    def addTwoNumbers2(self, l1, l2):
        p, q, carry, dummy = l1, l2, 0, ListNode(0)
        curr = dummy
        while p is not None or q is not None:
            x = p.val if p else 0
            y = q.val if q else 0
            carry, s = divmod(x+y+carry, 10)
            curr.next = ListNode(s)
            curr = curr.next
            p = p.next if p else None
            q = q.next if q else None
        if carry != 0:
            curr.next = ListNode(carry)
        return dummy.next
