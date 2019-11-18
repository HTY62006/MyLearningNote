# Binary_Search_Tree
> 參考資料：[Binary Search Tree: Intro(簡介)](http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html)
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
3. 如果欲刪除的節點下方有兩個子節點，先刪除該節點，往左子節點開始的樹中找出最大節點並移到被刪除的位置。
> 參考資料：[演算法圖鑑](https://www.books.com.tw/products/0010771263)p.49~p.51
## 修改
