"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

"""

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         pass



#Things to keep in mind
#Compare elements of two strings
#Once you find the first element that doesn't match between the two strings, break the for loop and continue to next iteration
#Don't compare over the same two strings twice, move on to two completely different index of the string at n index of input array

#Sorting posibilities - switch current index with the next index - allows you to constantly compare each element in the array with the first element
#Just compare every element to the first element





class Solution:
    def longestCommonPrefix(self, strs: str) -> str:
        
        i = 0 #index
        counter = 0 #prefix counter
        largest_prefix_number = 0
        largest_prefix = ""
        prefix = ""


        # while i < len(strs):
            
        #     if i < len(strs) - 1:
        #         current_word = strs[i]
        #         next_word = strs[i+1]
            
        #         for j in range(len(strs)):
        #             if current_word[j] != next_word[j]:
        #                 pass
        #                 #if character of current does not match the character at current index of any of the other characters of the other index, move current word to the front of the array
        #                 #Else add character to largest_prefix
                        
           
                

        #Get longest prefix
        while i < len(strs):
            
            if i < len(strs) - 1:
                current_word = strs[i]
                next_word = strs[i+1]
            
                for j in range(len(strs)):
                    if current_word[j] == next_word[j]:
                        print("Match!")
                        prefix += current_word[j]
                        
                        
            print("prefix length", len(prefix))        
            if len(prefix) > len(largest_prefix):
                largest_prefix = prefix
        
                
            i+=2

        print("Largest prefix: ", largest_prefix)
        return largest_prefix
                


words = ["flower","flow","flight"]
solution = Solution()
solution.longestCommonPrefix(words)



