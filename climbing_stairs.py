#You are climbing a staircase. It takes n steps to reach the top.
#
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#
#
#Example 1:
#
#Input: n = 2
#Output: 2
#Explanation: There are two ways to climb to the top.
#1. 1 step + 1 step
#2. 2 steps
#
#Example 2:
#
#Input: n = 3
#Output: 3
#Explanation: There are three ways to climb to the top.
#1. 1 step + 1 step + 1 step
#2. 1 step + 2 steps
#3. 2 steps + 1 step
#
#
#
#Constraints:
#
#    1 <= n <= 45
class Solution:
    def __init__(self):
        #Cache to store evals of subproblems
        self.memo = {1:1,2:2}

    def climbStairs(self, n:int) -> int:

        return self.f(n)


    #Helper function to check memo dict for previous evalutaion of subproblems
    #Add to dict to store for future evaluations in tree if not already stored


    def f(self,x):
        if x in self.memo:
            return self.memo[x]
        else:
            self.memo[x] = self.f(x - 1) + self.f(x - 2)
            return self.memo[x]



n = 38
solution = Solution()
result = solution.climbStairs(n)
print("result:",result)
