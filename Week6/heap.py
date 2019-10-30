# # root = i
# # left = root*2
# # right = root*2+1
# -----------------------------------------------
# def MaxHeapify(A):
#     for i in range(len(A)):
#         root = i
#         left = i*2+1
#         right = i*2+2
#         if (left < len(A)-1) and (A[left] > A[root]):
#             MaxIndex = left
#         else:
#             MaxIndex = root
            
#         if (right < len(A)-1) and (A[right] > A[MaxIndex]):
#             MaxIndex = right
#         else:
#             MaxIndex = root
            
#         if MaxIndex != root:
#             change = A[root]
#             A[root] = A[MaxIndex]
#             A[MaxIndex] = change
#         print(A)
# -----------------------------------------------
# 錯誤：未按照Maxheap規則排序（子節點一定比父節點小）
# -----------------------------------------------
#     錯誤                理想
#      3                   8
#   7     1    →→→      7     3
# 1   2 8             1   2 1 
# -----------------------------------------------
# 錯誤的輸出結果
# -----------------------------------------------
# [3, 2, 1, 1, 7, 8]
# [3, 7, 1, 1, 2, 8]
# [3, 7, 1, 1, 2, 8]
# [3, 7, 1, 1, 2, 8]
# [3, 7, 1, 1, 2, 8]
# [3, 7, 1, 1, 2, 8]
# -----------------------------------------------
