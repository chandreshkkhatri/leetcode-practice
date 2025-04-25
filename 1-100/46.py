from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if l == 0:
            return []
        if l == 1:
            return [nums]

        perms = self.permute(nums[:l-1])
        ans = []
        for i, perm in enumerate(perms):
            for j in range(l):
                ans.append(perm[:j]+[nums[l-1]]+perm[j:])
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3]))
