class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        non_dup = set(nums) # type(non_dup)為<class 'set'>
        dup = sum(nums) - sum(non_dup) # 將加總值相減得到重複的值
        correct = []
        for i in range(1, len(nums)+1):
            correct.append(i)
        miss = sum(set(correct) - set(nums))
        # 將兩者的重複值去除並相減，得到遺失值
        # 因為是<class 'set'>，故加總後變為int
        return dup,miss
        
