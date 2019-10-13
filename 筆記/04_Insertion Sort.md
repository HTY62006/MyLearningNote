# Insertion Sort
Leetcode練習題：147. Insertion Sort List

這是我練習的[完整程式碼](https://github.com/HTY62006/MyLearningNote/blob/master/Leetcode/week4/147.%20Insertion%20Sort%20List.py)
## [回首頁](https://github.com/HTY62006/MyLearningNote)
## 目錄
   * [簡介](https://github.com/HTY62006/MyLearningNote/blob/master/%E7%AD%86%E8%A8%98/04_Insertion%20Sort.md#%E7%B0%A1%E4%BB%8B)
   * [Insertion Sort List](https://github.com/HTY62006/MyLearningNote/blob/master/%E7%AD%86%E8%A8%98/04_Insertion%20Sort.md#insertion-sort-list)
## 簡介
Insertion Sort（插入排序法）：
1. 將資料分為**已排序**與**未排序**。
2. 將未排序的**第一筆資料**插入已排序中適當的位置。
   * 已排序的值 **>=** 正在處理的值→已排序的值往右移。
   * 遇到第一個**小於**正在處理的值時，才進行插入。

![image](https://images.plurk.com/7pFxYHFs6R9cbdqE3hy7ot.png)

如上圖所示：
* 綠色：未排序的資料
* 橘色：已排序的資料
* 白色：正在處理的資料
> 參考：[【演算法】插入排序法(Insertion Sort)](http://notepad.yehyeh.net/Content/Algorithm/Sort/Insertion/1.php)
## [↑回目錄](https://github.com/HTY62006/MyLearningNote/blob/master/%E7%AD%86%E8%A8%98/04_Insertion%20Sort.md#%E7%9B%AE%E9%8C%84)
## Insertion Sort List
### 需求
使用Insertion Sort對Linke list進行排序。
* Example 1
  ```Text
  Input: 4->2->1->3
  Output: 1->2->3->4
  ```
* Example 2
  ```Text
  Input: -1->5->3->4->0
  Output: -1->0->3->4->5
  ```
### 實作與想法
假設輸入的節點依序為4->2->1->3。
1. 默認Linked list原先的首位為已排序的資料，`head.next`成為後方未排序資料的`head`。
   > 此時已排序的資料 out = 4，未排序的資料 head = 2，t = 4。
   ```Python
   out = head
   head = head.next
   t = out
   ```
2. 以while迴圈在Linked list未結束時進行判斷。
   * 先設定要進行測試的元素test，及其餘未排序資料新的head。
     ```Python
     while head != None:
            test = head # 測試值
            head = head.next
            if test.val <= out.val:
                test.next = out
                out = test
            elif test.val >= t.val:
                t.next = test
                t = test
            else:
                n = out
                while n.next != t and n.next.val < test.val:
                    n = n.next
                test.next = n.next
                n.next = test
     ```
## [↑回目錄](https://github.com/HTY62006/MyLearningNote/blob/master/%E7%AD%86%E8%A8%98/04_Insertion%20Sort.md#%E7%9B%AE%E9%8C%84)
