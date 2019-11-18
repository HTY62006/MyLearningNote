# Binary Search Tree
## 目錄
* [原理](https://github.com/HTY62006/MyLearningNote/blob/master/HW3/Binary_Search_Tree%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87BST%E5%8E%9F%E7%90%86.md#bst%E5%8E%9F%E7%90%86)
* 學習歷程
* 流程圖
## BST原理
參考老師上課講義中的影片與網路文章的說明後，歸納出bianry search tree的原理：
1. 選定一個root。
2. 較小的往左邊。
   * 任意左子樹只要不為空的話，左子樹上所有節點的值都小於根節點的值。
3. 較大的往右邊。
   * 任意右子樹只要不為空的話，右子樹上所有節點的值都大於根節點的值。
![image](https://github.com/HTY62006/MyLearningNote/blob/master/large_image/BST01.png)
> 參考資料：[Binary Tree and Binary Search Tree in Data Structure](https://www.youtube.com/watch?v=7vw2iIdqHlM&feature=emb_title)、[[資料結構] 二元搜尋樹 (Binary Search Tree)](https://ithelp.ithome.com.tw/articles/10205875)

## 學習歷程
### 新增
我原本的想法：
* 因為binary search tree的特性是小的會往左，大的會往右。而插入的值會插入在目前還是None的位子。
* 所以，如果沒有遇到None之前，root就會改變成現在的子節點，然後繼續尋找可插入的位子。
```Python
def insert(self, root, val):
    if root == None:
        root = TreeNode(val)
        return root
    elif val <= root.val:
        if root.left == None:
            root.left = TreeNode(val)
            return root.left
        else:
#             root = root.left
            self.insert(root.left, val)                
    elif val > root.val:
        if root.right == None:
            root.right = TreeNode(val)
            return root.right
        else:
#             root = root.right
            self.insert(root.right, val)
```
這時候會出現一個問題是，**雖然有成功插入值，但Solution().insert(root,val)回傳的是None**，檢查時發現是因為我做self.insert(root.left, val)和self.insert(root.right, val)時沒有return。
```Python
def insert(self, root, val):
    if root == None:
        root = TreeNode(val)
        return root
    elif val <= root.val:
        if root.left == None:
            root.left = TreeNode(val)
            return root.left
        else:
#             root = root.left
            return self.insert(root.left, val)                
    elif val > root.val:
        if root.right == None:
            root.right = TreeNode(val)
            return root.right
        else:
#             root = root.right
            return self.insert(root.right, val)
```
### 查詢
接下來我做了查詢的部分，我的想法和做insert在找可插入位子時類似。
* 檢查target有沒有和root的值一致，如果有，回傳root。
* 如果target小於root的值，檢查root.left是否一致，如果不一致，root.left取代成新的root，繼續尋找相同的位子。
* 如果target大於root的值，檢查root.right是否一致，如果不一致，root.right取代成新的root，繼續尋找相同的位子。
```Python
def search(self, root, target):
    if root.val == target:
        return root
    elif target < root.val:
        if root.left.val != target:
            # root.left取代原本的root
            return self.search(root.left, target)
        else:
            return root.left
        else: # target>root.val
        if root.right.val != target:
            return self.search(root.right, target)
        else:
            return root.right
```
此時若去查詢位於bst內的值，結果都會是正確的，但如果輸入的值不在bst內，會跳出錯誤：
```Text
ttributeError: 'NoneType' object has no attribute 'val'
```
![image](https://images.plurk.com/3HhpVgW223uHjHHklImjLL.png)
因為輸入的值不在bst內，跑到最後root.right或root.left會是None，但root.right或root.left都沒有val，因此我做出一些修改。
* 如果root.left或root.right不等於None時才會執行原本的判斷式。
* 如果是None就回傳None(search的值不在bst內)。
```Python
def search(self, root, target):
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
```
### 刪除
