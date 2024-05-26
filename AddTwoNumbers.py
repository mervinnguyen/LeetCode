#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit.
#Add the two numbers and return the sum as a linked list. 
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        temp = ListNode()
        current = temp
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            current.next = ListNode(carry % 10)
            current = current.next
            carry = carry // 10
        return temp.next