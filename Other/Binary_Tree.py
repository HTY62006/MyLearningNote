class TreeNode():
    def __init__(self, x):
        self.val = x
        # left、right類似.next
        self.left = None
        self.right = None
        # 插入
#     def append(self, value):
#             # 原本寫if value < self.data and self.left == None:，但因為還要考慮right的部分，不能寫在一起(為了要用else if)
#         if value < self.data:
#             if self.left == None:
#                 self.left=Node(value) # 因為每個都是節點，節點下方可能也可有節點，所以要創建Node存入left(原先Node的左下方)
#             else:
#                 self.left.append(value) # 如果left不為空，直接插入?
#         elif value > self.data:
#             if self.right == None:
#                 self.right=Node(value)
#             else:
#                 self.right.append(value)

n = TreeNode(10)
l = TreeNode(9)
n.left=l
print(n.val, n.left.val)


# add_root
# add_left
# add_right
# replace
# del

#參考資料1: http://www.csie.ntnu.edu.tw/~u91029/BinaryTree.html 參考資料2: https://www.youtube.com/watch?v=7vw2iIdqHlM
