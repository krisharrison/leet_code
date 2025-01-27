
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        x_copy = x
        result = 0

        while x_copy != 0:
            result *= 10
            result += x_copy % 10
            x_copy //= 10
        
        
        if result == x:
            return True
        return False