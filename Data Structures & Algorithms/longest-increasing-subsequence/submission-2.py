class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(i, j):
            if i == len(nums):
                return 0

            LIS = dfs(i + 1, j)  # skip

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i))  # include

            return LIS

        return dfs(0, -1)