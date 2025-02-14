"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

 

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.

"""

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = ListNode()
        cur_node = ListNode()
        
        #Both lists empty
        if not list1 and not list2:
            head = list1
            return head

        #Two statements determine if one list is empty and the other has an element
        if not list1:
            head = list2
            return list2
        
        if not list2:
            head = list1
            return head

        #Determine head pointer
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next

        else:
            head = list2
            list2 = list2.next

        #Current starts at head
        cur_node = head

        #Iterate through both lists to compare values
        #Change next pointer of each node from each list depending on value
        while list1 and list2:
         if list1.val <= list2.val:
            cur_node.next = list1
            cur_node = cur_node.next
            list1 = list1.next
         else:
            cur_node.next = list2
            cur_node = cur_node.next
            list2 = list2.next
        
        #Chang pointer of second last node
        if list1 is None:
            cur_node.next = list2
        if list2 is None:
            cur_node.next = list1

        return head

