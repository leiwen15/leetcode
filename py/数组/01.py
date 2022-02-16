class Solution:
    def twoSum(self, nums, target):
        hashtable = {}
        for i in range(len(nums)):
            if target - nums[i] in hashtable:
                return [i, hashtable[target-nums[i]]]
            hashtable[nums[i]] = i
        return []

# T = Solution()
# print(T.twoSum([3,3], 6))
