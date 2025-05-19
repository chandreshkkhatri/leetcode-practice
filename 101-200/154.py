from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find_min(start, end):
            mid = (start+end)//2
            if end-start == 2:
                if nums[start] > nums[start+1]:
                    return start+1
                else:
                    return start
            if end-start == 1:
                return start
            if nums[end-1] > nums[mid]:
                return find_min(start, mid+1)
            elif nums[mid] > nums[end-1]:
                return find_min(mid+1, end)
            else:
                return find_min(start, end-1)

        return nums[find_min(0, len(nums))]


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 4, 5, 1, 2]
    ans = sol.findMin(nums)
    print(ans)
