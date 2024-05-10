class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        longest_sequence = 0

        for i in nums:
            if i-1 not in nums_set:
                current_number = i
                current_streak = 1

                while current_number+1 in nums_set:
                    current_number =  current_number + 1
                    current_streak += 1
                longest_sequence = max(longest_sequence, current_streak)
        return longest_sequence
        
        

        