class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)-1
        mid = (left + right) //2
        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            mid = (left + right) // 2
        return right + 1
