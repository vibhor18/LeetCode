class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n>0:
                number, digit = divmod(n,10)
                digit = digit ** 2
                total_sum += digit
                n = number
            return total_sum

        slow = n
        fast = get_next(n) 
        while fast != 1 and fast != slow:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1       