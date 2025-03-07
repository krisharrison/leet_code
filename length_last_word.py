"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal

consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

 

Constraints:

    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.
"""

class Solution:
    def lengthOfLastWord(self,s: str) -> int:
        s_list = s.split()
        last_index = len(s_list) - 1
        last_word = s_list[last_index]
        last_word_len = len(last_word)

        return last_word_len

    
  
s = "   fly me   to   the moon  "
s2 = "luffy is still joyboy"

solution = Solution()
answer = solution.lengthOfLastWord(s2)
print(answer)
