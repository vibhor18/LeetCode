class Solution:
    def hammingWeight(self, n: int) -> int:
        count_of_one = 0
        while n:
            n = n & (n-1)
            count_of_one += 1
        return count_of_one
        