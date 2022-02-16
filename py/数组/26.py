class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left, right = 0, 1
        while right < len(nums):
            if nums[right - 1] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
        return left
