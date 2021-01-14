"""
人一生不会踏进同一条河流
__author__ = 'marseille'
__date__ = '2021/1/13 17:02'
"""
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last = None
        while head:
            last, head.next, head = head, last, head.next
        return last
class Solution():
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next = head.next
            head.next = prev
            prev = curr
            curr = next
        return prev