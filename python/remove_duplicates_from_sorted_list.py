from typing import Optional

class ListNode():
    def __init__(self,val=0,next=None):
        self.val = val
        self. next = next

class Solution:
    def removeDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Check there is more than one node in the list
        if not head:
            return head
        if not head.next:
            return head

        #Remove duplicates
        curr_node = head
        while curr_node and curr_node.next:
            if curr_node.val == curr_node.next.val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
        
        return head


#Create Linkedlist - 11233
head = ListNode(val=1)
head.next = ListNode(val=1)
head.next.next=ListNode(val=2)
head.next.next.next=ListNode(val=3)
head.next.next.next.next=ListNode(val=3)
solution = Solution()
result = solution.removeDuplicates(head)

#display result
while result:
    print(result.val)
    result = result.next
