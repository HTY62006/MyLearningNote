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

# Max Heap
def build_maxheap(A):
    for i in range(len(A)-1, -1, -1):
        root = i//2
        maxheapify(A, root)

def maxheapify(A, root):
    left = root*2+1
    right = root*2+2
    if (left < len(A)) and (A[left] > A[root]):
        MaxIndex = left
    else:
        MaxIndex = root
            
    if (right < len(A)) and (A[right] > A[MaxIndex]):
        MaxIndex = right
            
    if MaxIndex != root:
        change = A[root]
        A[root] = A[MaxIndex]
        A[MaxIndex] = change
        maxheapify(A,MaxIndex)
         
Array = [3,2,1,1,7,8]
build_maxheap(Array)
# [8, 7, 3, 1, 2, 1]

# Min Heap
def build_minheap(A):
    for i in range(len(A)-1, -1, -1):
        root = i//2
        minheapify(A, root)

def minheapify(A, root):
    left = root*2+1
    right = root*2+2
    if (left < len(A)) and (A[left] < A[root]):
        minIndex = left
    else:
        minIndex = root
            
    if (right < len(A)) and (A[right] < A[minIndex]):
        minIndex = right
            
    if MaxIndex != root:
        change = A[root]
        A[root] = A[minIndex]
        A[minIndex] = change
        minheapify(A,minIndex)
         
Array = [3,2,1,1,7,8]
build_maxheap(Array)
# [1, 2, 1, 3, 7, 8]
