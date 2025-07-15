#You are climbing a staircase. It takes n steps to reach the top.
#
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#
#
#Example 1:
#
#Input: n = 2
#Output: 2
#Explanation: There are two ways to climb to the top.
#1. 1 step + 1 step
#2. 2 steps
#
#Example 2:
#
#Input: n = 3
#Output: 3
#Explanation: There are three ways to climb to the top.
#1. 1 step + 1 step + 1 step
#2. 1 step + 2 steps
#3. 2 steps + 1 step
#
#
#
#Constraints:
#
#    1 <= n <= 45
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)
    

    def _insert(self, data, curr_node):
        if data < curr_node.data:
            if curr_node.left is None:
                new_left_value = curr_node.data + 1
                curr_node.left = Node(new_left_value)
                print(new_left_value)
            else:
                self._insert(data, curr_node.left)
        elif data < curr_node.data:
            if curr_node.right is None:
                new_right_value = curr_node.data + 2
                curr_node = Node(new_right_value)
                print(new_right_value)
            else:
                self._insert(data,curr_node.right)



class Solution:
    def climbstairs(self):
        data = 0
        tree = BinaryTree(data)
        print(tree.root.data)
        print(tree.root.left)
        print(tree.root.right)


solution = Solution()
solution.climbstairs()
#n = 2
#solution = Solution()
#result = solution(n)

