# 與231. Power of Two相同，只是此處求是否為3的某某次方

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n%3 == 0 and n>1:
            n/=3
        if n == 1:
            return True
        else:
            return False
        
