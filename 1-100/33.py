from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rotation_idx = self.find_rotation_idx(nums)
        rectified_nums = nums[rotation_idx:] + nums[:rotation_idx]

        search_idx = self.search_helper(rectified_nums, target)

        if search_idx == -1:
            return -1

        return (search_idx + rotation_idx) % len(nums)

    def search_helper(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        start = 0
        end = len(nums) - 1
        mid = (start + end)//2

        if nums[mid] == target:
            return mid

        if len(nums) % 2 == 0:
            if nums[mid] > target:
                return self.search_helper(nums[start:mid+1], target)
            else:
                search_idx = self.search_helper(nums[mid+1:end+1], target)
                if search_idx == -1:
                    return -1
                return mid + 1 + search_idx
        else:
            if nums[mid] > target:
                return self.search_helper(nums[start:mid], target)
            else:
                search_idx = self.search_helper(nums[mid:end+1], target)
                if search_idx == -1:
                    return -1
                return mid + self.search_helper(nums[mid:end+1], target)

    def find_rotation_idx(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        mid = (start + end)//2
        if end == 0:
            return 0
        if end == 1:
            if nums[0] < nums[1]:
                return 0
            else:
                return 1
        if nums[end] > nums[mid]:
            end = mid
            return self.find_rotation_idx(nums[start:end + 1])
        else:
            start = mid + 1
            return start + self.find_rotation_idx(nums[start:end+1])


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    s = Solution()
    print(s.search(nums, target))
