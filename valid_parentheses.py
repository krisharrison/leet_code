"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.


"""

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peak(self):
        last_index = len(self.items) - 1
        return self.items[last_index]
    
    def is_empty(self):
        return self.items == []
    
    def get_stack(self):
        return self.items


class Solution:
    def isValid(self, s: str) -> bool:
       stack = Stack()
       open_brackets = ["(", "[", "{"]
       closed_brackets = [")", "]", "}"]

       for bracket in s:
            if bracket in open_brackets:
                stack.push(bracket)


       for bracket in s:
            top = stack.peak()
            

            if bracket in closed_brackets:
                closed_index = closed_brackets.index(bracket)
                open_index = closed_brackets.index(bracket)
                if top == open_brackets[open_index] and bracket == closed_brackets[closed_index]:
                    stack.pop()
                else:
                    return False
        

       return True
