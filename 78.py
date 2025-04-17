from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if l == 0:
            return [[]]
        if l == 1:
            return [[], nums]

        ans = self.subsets(nums[:l-1])
        l_ans = len(ans)
        ans.append([nums[l-1]])
        for i in range(1, l_ans):
            ans.append(ans[i]+[nums[l-1]])
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))
    print(s.subsets([1]))
    print(s.subsets([]))
