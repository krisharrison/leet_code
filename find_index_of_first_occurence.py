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
needle3 = "issi"

class Solution:
    def strStr(self, haystack:str, needle:str) -> int:
        if needle not in haystack:
            return -1
        if len(haystack) == 1:
            if needle not in haystack:
                return -1

        needle_len = len(needle)
        start = 0
        end = needle_len
        haystack_len = len(haystack)
        
        print(haystack[start:end])

        while end <= haystack_len:
            if needle in haystack[start:end]:
                index = start
                break
            else:
                start = start + 1
                end = end + 1

        
        return index


solution = Solution()
index = solution.strStr(haystack3, needle3)
print(index)

