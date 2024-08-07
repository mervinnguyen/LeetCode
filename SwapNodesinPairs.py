#Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed)

#Example 1:
#Input: head = [1,2,3,4]
#Output: [2,1,4,3]

#Example 2:
#Input: head = []
#Output: []

#Example 3:
#Input: head = [1]
#Output: [1]

class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        
        front = head
        end = head.next
        
        front.next = self.swapPairs(end.next)
        end.next = front
        
        return end