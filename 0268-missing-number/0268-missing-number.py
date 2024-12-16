class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_sum = 0
        for i in range(len(nums)):
            xor_sum ^= i ^ nums[i]
        xor_sum ^= len(nums)
        return xor_sum
        