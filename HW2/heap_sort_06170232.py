##### heap_sort_06170232.py

class Solution(object):
    def heap_sort(self, nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        if len(nums)>1:
            nums = self.buildMaxHeap(nums) # 重整結構
            max_now = nums[0] # 取出最大值(root)
            return self.heap_sort(nums[1:])+[max_now] # 尚未分好的部分會繼續進行分類→→遞迴
        # 無法再分的話會直接回傳
        else:
            return nums
        
    # 將輸入的nums轉換成heap
    def buildMaxHeap(self, nums):
        for i in range(len(nums)-1, -1, -1):
            root = i//2 # 取整數結果
            self.maxheapify(nums, root)
        return nums
    def maxheapify(self, nums, root):
        left = root*2+1 # 左子節點
        right = root*2+2 # 右子節點
        # 如果left值>root值，那目前此階段最大值的index為left
        if left <= len(nums)-1 and nums[left] > nums[root]:
            max_index=left
        else:
            max_index=root # 沒有的話就仍是root
        # 和最大值比較，right值若較大，則取代原先max_index成為新的最大值的index
        if right <= len(nums)-1 and nums[right] > nums[max_index]:
            max_index=right
        # 若最大值的index和輸入的root不一致，則代表需要互換
        if max_index != root:
            c=nums[root]
            nums[root]=nums[max_index]#互換
            nums[max_index]=c
            self.maxheapify(nums, max_index)#檢查下一層是否符合heap規則
