"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of
the first two lists.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1

        n1 = l1
        n2 = l2
        m = None
        head = m

        while n1 is not None and n2 is not None:
            if m is None:
                if n1.val <= n2.val:
                    m = n1
                    n1 = n1.next
                else:
                    m = n2
                    n2 = n2.next
            else:
                if n1.val <= n2.val:
                    m.next = n1
                    m = m.next
                    n1 = n1.next
                else:
                    m.next = n2
                    m = m.next
                    n2 = n2.next

        if n1 is None:
            m.next = n2
        else:
            m.next = n1

        return head
