"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

 

Constraints:

    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.

"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #Always make a the larger number
        if len(a) < len(b):
            temp = a
            a = b
            b = temp

        #variables for returned result and carried over digit
        result = ""
        carry = 0

        #Track the length of each input string since they are both different lengths
        a_index = len(a) - 1
        b_index = len(b) - 1

        #Get result
        while a_index > -1:
            #Cast each character individual character into int type
            #If b is out of ranges assign 0
            a_digit = int(a[a_index])
            if b_index >= 0:
                b_digit = int(b[b_index])
            else:
                b_digit = 0


            #Need carry from the result of 1 + 1 or 1 + 1 + 1
            total = a_digit + b_digit + carry

            #Mod2 from total is used to get binary digit
            #New new digit is parsed back into a string
            #E.g. 3 % 2 = 1
            #E.g. 2 % 2 = 0
            char_digit = str(total % 2)

            #Add new binary character digit to result
            result = char_digit + result
            #Floor divide two from total to get carried over binary digit
            #E.g. 3 /floor 2 = 1 = 1
            #E.g. 2 /floor 2 = 1
            carry = total // 2

            a_index = a_index - 1
            b_index = b_index - 1
        
        if carry != 0:
            result = "1" + result

        return result

 
a = "11010"
b = "1011"
a2 = "111"
b2 = "1010"

solution = Solution()
result = solution.addBinary(a2,b2)

print(result)

