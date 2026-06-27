from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def dfs(i):
            if i >= len(nums) - 1:
                return True

            if i in memo:
                return memo[i]

            furthest = min(len(nums) - 1, i + nums[i])

            for j in range(furthest, i, -1):  # try farther jumps first
                if dfs(j):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dfs(0)