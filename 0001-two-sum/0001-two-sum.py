class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_set:
                return [i, hash_set[complement]]
            else:
                hash_set[nums[i]] = i        