# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root == None:
            root = TreeNode(val)
            return root
        
        elif val <= root.val:
            if root.left == None:
                root.left = TreeNode(val)
                return root.left
            else:
#                 root = root.left
                return self.insert(root.left, val)
                
        elif val > root.val:
            if root.right == None:
                root.right = TreeNode(val)
                return root.right
            else:
#                 root = root.right
                return self.insert(root.right, val)
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        check = self.bst_to_array(root)
        count = 0
        for i in check:
            if i == target:
                count+=1
#         print(count)
        while count != 0:
            check_point = self.search(root, target)
            # 刪除節點底下沒有節點
            if check_point.left == None and check_point.right == None:
                if check_point == root:
                    root = None
    #                 return
                else:
                    r = self.parent_node(root, target)
                    if r.left == check_point:
                        r.left = None
                    elif r.right == check_point:
                        r.right = None
                        # return
            # 刪除節點下方有一邊有節點(左)
            elif check_point.left != None and check_point.right == None:
                if check_point == root:
                    root = root.left
                else:
                    r = self.parent_node(root, target)
                    if r.left == check_point:
                        r.left = check_point.left
                    elif r.right == check_point:
                        r.right = check_point.left
            # 刪除節點下方有一邊有節點(右)
            elif check_point.left == None and check_point.right != None:
                if check_point == root:
                    root = root.right
                else:
                    r = self.parent_node(root, target)
                    if r.left == check_point:
                        r.left = check_point.right
                    elif r.right == check_point:
                        r.right = check_point.right
            # 刪除節點下方兩個都有節點
            elif check_point.left != None and check_point.right != None:
                min_node_parent = check_point
                min_node = check_point.right
                # min_node.left為空，最小值一定會是min_node
                if min_node.left == None:
                    check_point.val = min_node.val
                    check_point.right = min_node.right
                else:
                    # while 推到最小值
                    # 因為是抓最小值，所以用min_node.left
                    while min_node.left != None:
                        min_node_parent = min_node
                        min_node = min_node.left
    #                 print(min_node_parent.val)
                    check_point.val = min_node.val
    #                 print(min_node_parent.val)
                    # min_node還有右子樹
                    if min_node.right != None:
                        if min_node_parent.val < min_node.val:
                            min_node_parent.right = min_node.right
                        elif min_node_parent.val > min_node.val:
                            min_node_parent.left = min_node.left
                    else:
                        if min_node.val >= min_node_parent.val:
                            min_node_parent.right = None
                        elif min_node.val < min_node_parent.val:
                            min_node_parent.left = None
            count-=1
        return root
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if root != None:
            if root.val == target:
                return root
            # 搜尋，target<root的值就往左走
            elif target < root.val:
                # 如果左邊不是None
                if root.left != None:
                    # 判斷target是否與root.left.val一致
                    if root.left.val != target:
                        # root.left取代原本的root
                        return self.search(root.left, target)
                    else:
                        return root.left
                else:
                    return None
            else: # target>root.val
                # 如果右邊邊不是None
                if root.right != None:
                    # 判斷target是否與root.left.val一致
                    if root.right.val != target:
                        # root.right取代原本的root
                        return self.search(root.right, target)
                    else:
                        return root.right
                else:
                    return None
        else:
            return None
    

    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype: None Do not return anything, modify nodes(maybe more than more) in-place instead.(cannot search())
        """
        # 如果要替換的值存在
        if self.search(root, target) != None:
            if target == new_val:
                return root
            else:
                
                check = self.bst_to_array(root)
                count = 0
                # 新增要新增幾次
                for i in check:
                    if i == target:
                        count+=1
                # 後面判斷要用的
                h = self.height(root)
                # 刪除值
                new_root = self.delete(root, target)
                # 新增值
                while count != 0:
                    self.insert(new_root, new_val)
                    count-=1
                if self.height(new_root) <= h:
                    return root
                else:
                    arr = self.bst_to_array(new_root)
                    arr.sort()
                    # 重整結構
                    new_root = self.array_to_bst(arr)
                    return new_root
#                 return new_root
        else: # target不存在
            return root


    def bst_to_array(self, root):
        array=[]
        if root != None:
            array.append(root.val)
            return array+self.bst_to_array(root.left)+self.bst_to_array(root.right)
        else:
            return array
    def parent_node(self, root, target):
        if self.search(root, target) != None:
            current = root # 用while去算有沒有到target
            parent = root # 根節點

            while current != None:
                if target < current.val:
                    parent = current
                    current = current.left# 往左
                elif target == current.val:
                    return parent
                else: # x>current.val
                    parent=current
                    current = current.right# 往右
        else:
            return None
        
    def array_to_bst(self, nums):
        if len(nums)>0:
            split = (len(nums)-1)//2
            root = TreeNode(nums[split])
            # 反覆對split左右兩邊重新取root
            if root.val == root.right.val:
                root.left.val = root.right.val
                root.right = None
            root.left = self.array_to_bst(nums[:split])
            root.right = self.array_to_bst(nums[split+1:])          
        else:
            return None
    def height(self, root):
        if root != None:

            LH = self.height(root.left) # LH最終會return -1
            LR = self.height(root.right) # LR最終會return -1

            if LH < LR:
                return(LR+1)
            else:
                return(LH+1)
        else:
            return -1 # height of root不包含root那層
    def array_to_bst(self, arr):
        if len(arr) != 0:
            split = (len(arr)-1)//2 # arr的index從0開始，所以-1
            root = TreeNode(arr[split])

            root.left = array_to_bst(arr[:split])
            root.right = array_to_bst(arr[split+1:])

            return root
        else:
            return None


# 參考資料總整理：
# [Deleting a node from a BST --- Part 1 (easy cases)](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/BST-delete.html)
# [Traversing/searching in a BST](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/BST-search.html)
# [Binary Tree and Binary Search Tree in Data Structure](https://www.youtube.com/watch?v=7vw2iIdqHlM&feature=emb_title)
# [[資料結構] 二元搜尋樹 (Binary Search Tree)](https://ithelp.ithome.com.tw/articles/10205875)
# 演算法圖鑑p.47~p.52
# [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
# [how to calculate the height of a BST in python](https://stackoverflow.com/questions/21011423/how-to-calculate-the-height-of-a-bst-in-python)
