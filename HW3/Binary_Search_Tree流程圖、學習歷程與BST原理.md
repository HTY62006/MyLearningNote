# Binary Search Tree
## 目錄
* [原理](https://github.com/HTY62006/MyLearningNote/blob/master/HW3/Binary_Search_Tree%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87BST%E5%8E%9F%E7%90%86.md#bst%E5%8E%9F%E7%90%86)
* [流程圖](https://github.com/HTY62006/MyLearningNote/blob/master/HW3/Binary_Search_Tree%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87BST%E5%8E%9F%E7%90%86.md#%E6%B5%81%E7%A8%8B%E5%9C%96)
* [學習歷程](https://github.com/HTY62006/MyLearningNote/blob/master/HW3/Binary_Search_Tree%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87BST%E5%8E%9F%E7%90%86.md#%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B)
  * [新增](https://github.com/HTY62006/MyLearningNote/blob/master/HW3/Binary_Search_Tree%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87BST%E5%8E%9F%E7%90%86.md#%E6%96%B0%E5%A2%9E)
  * [查詢](https://github.com/HTY62006/MyLearningNote/blob/master/HW3/Binary_Search_Tree%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87BST%E5%8E%9F%E7%90%86.md#%E6%9F%A5%E8%A9%A2)
  * [刪除](https://github.com/HTY62006/MyLearningNote/blob/master/HW3/Binary_Search_Tree%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87BST%E5%8E%9F%E7%90%86.md#%E5%88%AA%E9%99%A4)
* [參考資料總整理](https://github.com/HTY62006/MyLearningNote/blob/master/HW3/Binary_Search_Tree%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87BST%E5%8E%9F%E7%90%86.md#%E5%8F%83%E8%80%83%E8%B3%87%E6%96%99%E7%B8%BD%E6%95%B4%E7%90%86)
## BST原理
參考老師上課講義中的影片與網路文章的說明後，歸納出bianry search tree的原理：
1. 選定一個root。
2. 較小的往左邊。
   * 任意左子樹只要不為空的話，左子樹上所有節點的值都小於根節點的值。
3. 較大的往右邊。
   * 任意右子樹只要不為空的話，右子樹上所有節點的值都大於根節點的值。
4. 不存在任何值相等的節點
![image](https://github.com/HTY62006/MyLearningNote/blob/master/large_image/BST01.png)
> 參考資料：[Binary Tree and Binary Search Tree in Data Structure](https://www.youtube.com/watch?v=7vw2iIdqHlM&feature=emb_title)、[[資料結構] 二元搜尋樹 (Binary Search Tree)](https://ithelp.ithome.com.tw/articles/10205875)
## 流程圖
1. 新增
![image](https://github.com/HTY62006/MyLearningNote/blob/master/large_image/_20191122_231048.JPG)
2. 刪除
![image](https://github.com/HTY62006/MyLearningNote/blob/master/large_image/DSC_0079.JPG)
![image](https://github.com/HTY62006/MyLearningNote/blob/master/large_image/DSC_0083.JPG)
3. 查詢
![image](https://github.com/HTY62006/MyLearningNote/blob/master/large_image/_20191122_231111.JPG)
4. 修改
![image](https://github.com/HTY62006/MyLearningNote/blob/master/large_image/DSC_0078.JPG)
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
```Text
* 符合條件的節點下方沒有子節點的話，直接刪除該節點。
* 如果欲刪除的節點下方還有一個子節點，先刪除該節點，然後再將子節點移到該節點原本的位置。
* 如果欲刪除的節點下方有兩個子節點，先刪除該節點，往左子節點開始的樹中找出最大節點並移到被刪除的位置。
```
```Python
def delete(self, root, target):
    # 如果還找得到
    while self.search(root, target) != None:
        check_point = self.search(root, target)
        # 沒有子節點
        if check_point.left == None and check_point.right == None:
            # 該節點刪除
            check_point = None
            return check_point
        # 有一端有子節點
        elif check_point.left != None and check_point.right == None:
            # 子節點移上來
            check_point = check_point.left
            # 刪除
            check_point.left = None
            return check_point
        # 有一端有子節點
        elif check_point.right != None and check_point.left == None:
            # 子節點移上來
            check_point = check_point.right
            # 刪除
            check_point.right = None
            return check_point
        else: # check_point.right != None and check_point.left != None
            # 找左子樹中最大子節點
            left_max_node = self.search_left_max_target(check_point.left)
            # 刪除&重整結構
            return self.delete(check_point.left, left_max_node)
            # 上移
            check_point = left_max_node
            return check_point

def search_left_max_target(self, root):
    if root.left == None and root.right == None:
        return root
    else:
        # 取左子樹最大值
        left_tree = self.bst_to_array(root)
        return TreeNode(max(left_tree))

# BST轉Array
def bst_to_array(root):
    array = []
    while root != None:
        array.append(root.val)
        if root.left != None:
            if root.left.left == None and root.left.right == None:
                array.append(root.left.val)
#                 root = None
            else:
                root = root.left
                return bst_to_array(root)
            print(array)
        elif root.right != None:
            if root.right.left == None and root.right.right == None:
                array.append(root.right.val)
#                 root = None
            else:
                root = root.right
                return bst_to_array(root)
            print(array)
```
 bst_to_array(root)發生問題：會變成無限迴圈。
 <br>決定每次都只新增輸入的root進入Array。
 ```Python
 def bst_to_array(root):
    if root != None:
        array = []
        array.append(root.val)

    return array+bst_to_array(root.left)+bst_to_array(root.right)
```
錯誤：**UnboundLocalError: local variable 'array' referenced before assignment**
<br>因為我把array放在if裡面，可是這時候會發生問題就是，假設現在root=None，那return裡的array他會找不到東西可以return。
```Python
def bst_to_array(self, root):
    array=[]
    if root != None:
        array.append(root.val)
        return array+bst_to_array(root.left)+bst_to_array(root.right)
    else:
        return array
```
改成這樣就成功可以將BST轉成Array了！接著來測試有沒有刪除成功。
![image](https://images.plurk.com/2I0rUNcfikHtwLf0bhBo4m.png)

沒有刪除成功（該刪除的節點還在BST內），因此來一步步釐清問題發生在哪。
1. 先只看第一種刪除的情況──可以直接刪除
```Python
def delete(root, target):
    while Solution().search(root, target) != None:
        check_point = Solution().search(root, target)
        print(check_point.val)
        if check_point.left == None and check_point.right == None:
            check_point = None
            print(check_point)
```
While條件出錯，會變成無限迴圈。改轉成Array候用for來計算target的出現次數。
```Python
check = Solution().bst_to_array(root)
count = 0
for i in check:
    if i == target:
        count+=1
```
但修改過後，雖然不會變成無限迴圈了，但還是沒修改成功。假設改變check_point刪除時會等於什麼，也是一樣情況，所以很顯然並不是這個問題。
```Python
# 還是沒刪除成功
def delete(root, target):
    check = Solution().bst_to_array(root)
    count = 0
    for i in check:
        if i == target:
            count+=1
    while count != 0:
        check_point = Solution().search(root, target)
        print(check_point.val)
        if check_point.left == None and check_point.right == None:
            check_point = check_point.left
            print(check_point)
            return check_point
        count-=1
```
我應該是哪有設定錯誤，因此查詢資料後得知，我應該是要讓check_point的根結點指向check_point的位子，再變成None，而不是直接將check_point=None。
> 參考資料：[Deleting a node from a BST --- Part 1 (easy cases)](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/BST-delete.html)、[Traversing/searching in a BST](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/BST-search.html)
* 要刪除的值作為子節點，將他上一層的根節點的左方或右方指向None即可維持BST的正確性
```Python
def delete(root, target):
    check = Solution().bst_to_array(root)
    count = 0
    for i in check:
        if i == target:
            count+=1
    while count != 0:
        check_point = Solution().search(root, target)
        print(check_point.val)
        if check_point.left == None and check_point.right == None:
            if check_point == root:
                root = None
#                 return
            else:
                r = parent_node(root, target)
                if r.left == check_point:
                    r.left = None
                elif r.right == check_point:
                    r.right = None
#                 return
        count-=1
```
嘗試將root.left或root.right指向None，有取代成功！

2. 刪除情況2──下方還有一個子節點
```Python
def delete(root, target):
    check = Solution().bst_to_array(root)
    count = 0
    for i in check:
        if i == target:
            count+=1
    while count != 0:
        check_point = Solution().search(root, target)
        if check_point.left != None and check_point.right == None:
            if check_point == root:
                root = root.left
            else:
                r = parent_node(root, target)
                if r.left == check_point:
                    r.left = check_point.left
                elif r.right == check_point:
                    r.right = check_point.left
        elif check_point.left == None and check_point.right != None:
            if check_point == root:
                root = root.right
            else:
                r = parent_node(root, target)
                if r.left == check_point:
                    r.left = check_point.right
                elif r.right == check_point:
                    r.right = check_point.right
