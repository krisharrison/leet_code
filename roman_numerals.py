"""13. Roman to Integer
Easy
Topics
Companies
Hint
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999]."""



#Set up a cursor that starts in the midde of the dict
#Cut elements in half
#Initial number is translated to decimal equivilent
#If num read is less than next num minus to total; else add tot total


# class Solution:
#     def romanToInt(self, s: str) -> int:
#         nums ={"I":1, "V":5, "X":10, "L":20, "C":100,"D":500,"M":1000}
#         key = len(nums)//2

    
        
        
class Solution:
    def romanToInt(self, s: str) -> int:
        nums ={"I":1, "V":5, "X":10, "L":50, "C":100,"D":500,"M":1000}

        self.total = 0
        self.decimal_nums=[]

        for i in range(len(s)):
            for key in nums.keys():
                if s[i] == key:
                    self.decimal_nums.append(nums[key])
        

        for i in range(len(self.decimal_nums)):
            if (i < len(self.decimal_nums)-1) and (self.decimal_nums[i] < self.decimal_nums[i+1]):
                self.total -= self.decimal_nums[i]
            else:
                self.total += self.decimal_nums[i]
        
        return self.total


    
solution = Solution
solution.romanToInt(solution, "III")
