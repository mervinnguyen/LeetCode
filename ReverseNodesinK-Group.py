#Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

#k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

#You may not alter the valyes in the list's nodes, only nodes themselves may be changed.

#Example 1:
#Input: head = [1,2,3,4,5], k = 2
#Output: [2,1,4,3,5]

#Example 2:
#Input: head = [1,2,3,4,5], k = 3
#Output: [3,2,1,4,5]

class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        end = dummy
        
        while end.next:
            for i in range(k):
                end = end.next
                if not end:
                    return dummy.next
            start = pre.next
            next = end.next
            end.next = None
            pre.next = self.reverse(start)
            start.next = next
            pre = start
            end = pre
        return dummy.next