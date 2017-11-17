"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        v1 = self.convert_to_int(l1)
        v2 = self.convert_to_int(l2)
        print(v1)
        print(v2)
        return self.convert_to_list(v1 + v2)

    @staticmethod
    def convert_to_int(list):
        rep = str(list.val)
        while list.next is not None:
            rep = str(list.next.val) + rep
            list = list.next
        return int(rep)

    @staticmethod
    def convert_to_list(int):
        rep = str(int)[::-1]
        return rep
        head = ListNode(rep[0])
        list = head

        for s in rep[1:]:
            node = ListNode(s)
            list.next = node
            list = list.next

        return head
