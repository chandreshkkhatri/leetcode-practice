from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        def convert_to_BST(left, right):
            if left > right:
                return None

            mid = (left+right)//2
            node = TreeNode(nums[mid])
            node.left = convert_to_BST(left, mid-1)
            node.right = convert_to_BST(mid+1, right)

            return node

        return convert_to_BST(0, len(nums)-1)


if __name__ == "__main__":
    sol = Solution()
    nums = [-10, -3, 0, 5, 9]
    ans = sol.sortedArrayToBST(nums)
    print(ans)
