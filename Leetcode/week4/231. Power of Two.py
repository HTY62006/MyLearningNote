# 如果n是2的次方，回傳True
# 設一while迴圈，當n可以被2整除且大於1時，做n = n/2
# 直到n為1時回傳True
# 範例：
# n=16
# 1. n/2→n=8
# 2. n/2→n=4
# 3. n/2→n=2
# 4. n/2→n=1

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n % 2 == 0 and n > 1:
            n /= 2
        if n == 1:
            return True
        else:
            return False
