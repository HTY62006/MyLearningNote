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
可是這時候會發生一個問題，雖然確實有成功插入，但會出現一個問題：
* 若root不存在，會無法成功插入（root沒成功變成4）。
![image](https://images.plurk.com/6mRYa0i9zSNaYn07XJSgrn.png)
