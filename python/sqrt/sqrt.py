#Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
#
#You must not use any built-in exponent function or operator.
#
#    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
#
#
#
#Example 1:
#
#Input: x = 4
#Output: 2
#Explanation: The square root of 4 is 2, so we return 2.
#
#Example 2:
#
#Input: x = 8
#Output: 2
#Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
#
#
#
#Constraints:
#
#    0 <= x <= 231 - 1

class Solution:
    def mySqrt(self, x: int) -> int:
        
        #i initiated for while loop
        #Num is for the return value with a default value of 0
        i = 1
        num = 0

        #Test for if the current value at i multplied by itself is greater the input value
        while i*i <= x:
            num = i
            i = i + 1
        
        return num
        


x = 6

solution = Solution()
result = solution.mySqrt(x)
print(result)
