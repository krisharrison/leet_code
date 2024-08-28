"""


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
        
          #Horizontal Scan
        #Check if length is 0
        if len(strs) == 0:
            return ""

        #Make first index of strs the initial prefix
        prefix = strs[0]

        #Find longest common prefix
        #Outler loop cycles through strs
        for i in range(1, len(strs)):
                #Compare current index at i to current value of prefix
                while len(prefix) != 0:
                    #Check the comparison of index
                    if strs[i].startswith(prefix):
                        break
                    elif prefix == "":
                        return ""
                    
                    #If no match remove last char of prefix
                    prefix = prefix[:len(prefix)-1]

                
        #Return correct prefix
        #Empty string is returned if prefix is not found
        return prefix

            
solution = Solution()
result = solution.longestCommonPrefix(["flower","flow","flight"])
