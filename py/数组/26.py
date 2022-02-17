class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        left, right = 0, 1
        while right < len(nums):
            if nums[right - 1] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
        return left + 1
m = Solution()
answer = m.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(answer)
