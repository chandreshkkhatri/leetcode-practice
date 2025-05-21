from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def findPeakEl(start, end):
            mid = (start+end)//2
            if end-start == 2:
                if nums[start] > nums[start+1]:
                    return start
                else:
                    return start+1
            if end-start == 1:
                return start
            if nums[mid+1] > nums[mid]:
                return findPeakEl(mid+1, end)
            else:
                return findPeakEl(start, mid+1)

        return findPeakEl(0, len(nums))


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    ans = sol.findPeakElement(nums)
    print(ans)
