# Binary_Search_Tree
## 新增
根據binary search tree的規則，和裡面的節點一層一層的做比較，看是要往左子樹走還是往右子樹走，最後插入到正確的位子。
* 從bst最上方開始尋找插入的位置。
* 和目前節點相比：
  * 較小，往左邊移動。
  * 較大，往右邊移動。
* 當移動到已經沒有節點時，插入節點(新增)。
> 插入4，比2大，往右移。
>> 比5小，往左移。
>>> 比3大，往右移。
>>>> 右方已無節點，插入4。

![image](https://images.plurk.com/7qeda7IgnPihGxycGuGOCH.png)
> 參考資料：[演算法圖鑑](https://www.books.com.tw/products/0010771263)p.47~p.49
## 查詢
* 從最上方開始搜尋。
* 和目前節點相比：
  * 較小，往左邊移動。
  * 較大，往右邊移動。
* 直到找到值相等的節點
> 參考資料：[演算法圖鑑](https://www.books.com.tw/products/0010771263)p.51~p.52
## 刪除
1. 符合條件的節點下方沒有子節點的話，直接刪除該節點。
2. 如果欲刪除的節點下方還有一個子節點，先刪除該節點，然後再將子節點移到該節點原本的位置。
3. 如果欲刪除的節點下方有兩個子節點，先刪除該節點，此時有兩種選擇。
   1. 往左子節點開始的樹中找出最大節點並移到被刪除的位置。
   2. 往右子節點開始的樹中找出最小節點並移到被刪除的位置。
> 參考資料：[演算法圖鑑](https://www.books.com.tw/products/0010771263)p.49~p.51、[Deleting a node from a BST --- Part 2 (the hard case)
](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/BST-delete2.html)
## 修改
1. 刪除指定值的節點。
2. 插入指定值的節點。
3. 需要符合binary search tree的結構。
`作業要求：修改後的BST高度不能超過原本的高度`

## 參考資料總整理：
* [Deleting a node from a BST --- Part 1 (easy cases)](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/BST-delete.html)
* [Traversing/searching in a BST](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/BST-search.html)
* [Binary Tree and Binary Search Tree in Data Structure](https://www.youtube.com/watch?v=7vw2iIdqHlM&feature=emb_title)
* [[資料結構] 二元搜尋樹 (Binary Search Tree)](https://ithelp.ithome.com.tw/articles/10205875)
* 演算法圖鑑p.47~p.52
* [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
* [how to calculate the height of a BST in python](https://stackoverflow.com/questions/21011423/how-to-calculate-the-height-of-a-bst-in-python)
