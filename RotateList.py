#Given the head of a linked list, rotate the list to the right by k places.

#Example 1:
#Input: head = [1,2,3,4,5], k = 2
#Output: [4,5,1,2,3]

#Example 2:
#Input: head = [0,1,2], k = 4
#Output: [2,0,1]

class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        x = head
        length = 1
        while x.next:
            x = x.next
            length += 1
        x.next = head
        k = k % length
        for i in range(length - k):
            x = x.next
        head = x.next
        x.next = None
        return head