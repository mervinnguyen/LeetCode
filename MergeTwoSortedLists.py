# You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists into one sorted list. THe list should be made by splicing together the nodes of the first two lists.
#Return the head of the merged linked list.

#Example 1: 
#Input: list1 = [1,2,4], list2 = [1,3,4]
#Output: [1,1,2,3,4,4]

#Example 2:
#Input: list1 = [], list2 = [0]
#Output: [0]

#Constraints:
#The number of nodes in list1 and list2 is in the range [0, 50].
#-100 <= Node.val <= 100
#Both list1 and list2 are sorted in non-decreasing order.

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2