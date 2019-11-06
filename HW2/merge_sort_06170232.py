###### merge_sort_06170232.py

class Solution(object):
    def merge_sort(self, nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        if len(nums)<=1:
            return(nums)
        else:
            split_point = len(nums)//2 # 分割點
            left = self.merge_sort(nums[:split_point])
            right = self.merge_sort(nums[split_point:])
            return self.merge(left, right) # 合併
        
    def merge(self, left, right):
        m = left+right # 先合併提供一個空間供稍後將正確的數放入list
        i=0
        j=0
        r=0
        while i < len(left) and j < len(right): 
            # m的第r位會是left[i]和right[j]中較小的一方
            if left[i] < right[j]: 
                m[r] = left[i] 
                i+=1
            else: 
                m[r] = right[j] 
                j+=1
            r+=1
        # 處理因為i或j一方已經比left或right的長度短而沒處理到的部分
        while i < len(left):
            m[r] = left[i]
            i+=1
            r+=1
        while j < len(right):
            m[r] = right[j]
            j+=1
            r+=1
        return m 
