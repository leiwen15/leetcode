class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)-1

        while right >= left:
            mid = (right + left) // 2
            temp = nums[mid]
            if temp == target:
                return mid
            elif temp > target:
                right = mid - 1
            elif temp < target:
                left = mid + 1
        return right + 1

# class Solution:
#     def searchInsert(self, nums, target):
#         left, right = 0, len(nums)-1
#         while right >= left:
#             mid = (right + left) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 right = mid - 1
#             elif nums[mid] < target:
#                 left = mid + 1
#         return right + 1

m = Solution()
mid = m.searchInsert([1, 3, 5, 6], 2)
print(mid)
