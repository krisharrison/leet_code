"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

 

Constraints:

    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.

"""
haystack = "sadbutsad"
needle = "sad"
haystack2 = "leedcode"
needle2 = "leeto"
haystack3 = "mississippi"
needle3 = "issip"

class Solution:
    def strStr(self, haystack:str, needle:str) -> int:
        
        #Outer loop traverses haystack
        #Inner loop traverses needle and compares needle at j to haystack at i + n
        for i in range(0, len(haystack) - len(needle) + 1):
            #Reset count after the conclusion of inner loop
            #i is assigned to haystack in order to perform arithmetic on i without altering the original value
            haystack_index = i
            count = 0
            for j in range(len(needle)):
                #Move on the next iteration in haystack[i] if any characters do not match
               if needle[j] != haystack[haystack_index]:
                   break
                # Count determines how many characters match
                # Haystack_index is used to compare characters from haystack to needle
               count = count + 1
               haystack_index = haystack_index + 1

            #Return index of first character of matched substring
            if count == len(needle):
               return i
        
        return -1


solution = Solution()
index = solution.strStr(haystack3, needle3)
print("Index: ", index)
