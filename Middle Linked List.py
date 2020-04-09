""" Given a non-empty, singly linked list with head node head, return a middle node of linked list.

    If there are two middle nodes, return the second middle node. """

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        first = head
        middle = head
        count = 1
        while first.next != None:
            count += 1
            first = first.next
        for i in range(count / 2):
            middle = middle.next
        return middle


