# Week4: Set and Insertion Sort
## 目錄
   * [SetMismatch](https://github.com/HTY62006/MyLearningNote/tree/master/Week4#set-mismatch)
   * [Insertion Sort List](https://github.com/HTY62006/MyLearningNote/tree/master/Week4#insertion-sort)
     * [解題說明圖(Insertion Sort List)](https://github.com/HTY62006/MyLearningNote/tree/master/Week4#%E8%A7%A3%E9%A1%8C%E8%AA%AA%E6%98%8E%E5%9C%96insertion-sort-list)
# Set Mismatch
Leetcode練習題：645. Set Mismatch

這是我練習的[完整程式碼](https://github.com/HTY62006/MyLearningNote/blob/master/Week4/645.%20Set%20Mismatch.py)

## [回首頁](https://github.com/HTY62006/MyLearningNote)
## 需求
nums應為一個內容為1~n的list：nums = [1, 2, 3, 4,..., n]。
1. 回傳nums的重複項
2. 回傳nums的缺失值
* Example:
```Text
Input: nums = [1,2,2,4]
Output: [2,3]
```
## 實作與想法
假設nums = [1,2,2,4]
1. 由於正確的內容一定是[1,2,3,...,n]，所以先以`set()`來將輸入的nums去除重複值後輸出成non_dup。
   > 此時non_dup = {1,2,4}
   ```Python
   non_dup = set(nums)
   ```
2. 將nums與non_dup各自加總，相減後可得到重複的值(dup)。
   > 此時dup = 2
   ```Python
   dup = sum(nums) - sum(non_dup)
   ```
3. 創建一擁有正確內容的list。
   > 此時correct = [1,2,3,4]
   ```Python
   correct = []
   for i in range(1, len(nums)+1):
       correct.append(i)
   ```
4. 以`set()`將coorect與nums去除重複值後相減。
   > 因此時資料型態為<class 'set'>，再加上結果只會有一數字，故以將相減的結果加總的方式將值轉為int。
   >> 此時miss = 3
   ```Python
   miss = sum(set(correct) - set(nums))
   ```
5. 最後可回傳結果為[2,3]
## [↑回目錄](https://github.com/HTY62006/MyLearningNote/tree/master/Week4#%E7%9B%AE%E9%8C%84)

# Insertion Sort
Leetcode練習題：147. Insertion Sort List

這是我練習的[完整程式碼](https://github.com/HTY62006/MyLearningNote/blob/master/Week4/147.%20Insertion%20Sort%20List.py)

## 簡介
Insertion Sort（插入排序法）：
1. 將資料分為**已排序**與**未排序**。
2. 將未排序的**第一筆資料**插入已排序中適當的位置。
   * 已排序的值**大於等於**正在處理的值→已排序的值往右移。
   * 遇到第一個**小於**正在處理的值時，才進行插入。

![image](https://images.plurk.com/7pFxYHFs6R9cbdqE3hy7ot.png)

如上圖所示：
* 綠色：未排序的資料
* 橘色：已排序的資料
* 白色：正在處理的資料
> 參考：[【演算法】插入排序法(Insertion Sort)](http://notepad.yehyeh.net/Content/Algorithm/Sort/Insertion/1.php)
## [↑回目錄](https://github.com/HTY62006/MyLearningNote/tree/master/Week4#%E7%9B%AE%E9%8C%84)
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
   > 此時已排序的資料值 out = 4，未排序的資料值 head = 2，t = 4。
   ```Python
   out = head
   head = head.next
   t = out
   ```
2. 以while迴圈在Linked list未結束時進行判斷。
   * 先設定要進行測試的元素，及其餘未排序資料新的head。
   * 如果測試的元素**小於等於**已排序的元素，則已排序值往右移。
   > 第一輪：test值 = 2，head值 = 1，out值 = 4。因2<4，可得到out為2->4。
   >> 第二輪：test值 = 1，head值 = 3，out為2->4。因1<2<4，可得到out為1->2->4。
   >>> 第三輪：test值 = 3，Linke list已到底，head = None，out為1->2->4。因測試元素既不小於已排序，也不大於後方的元素（已經是最後一次排序）。
   >>>> 令n=out（已排序元素），當n.next≠後方元素且n.next的值<測試元素(test)的值時，n = n.next（結果：n的值為2）
   >>>>> n.next為4，test為3，test.next = n.next（3->4）
   >>>>>> test(3->4)，n(1->2)，n.next = test（1->2->3->4）
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
3. 將Linked list尾部設為None，並回傳結果out。
   > t.val = 4，t.next = None
   >> 1->2->3->4->None，Linked list結束。out為經insertion sort排序後的結果。
   ```Python
   t.next = None
   return out
   ```
## [↑回目錄](https://github.com/HTY62006/MyLearningNote/tree/master/Week4#%E7%9B%AE%E9%8C%84)
## 解題說明圖(Insertion Sort List)
![image](https://github.com/HTY62006/MyLearningNote/blob/master/large_image/IS02.png)
[點此可看大圖](https://raw.githubusercontent.com/HTY62006/MyLearningNote/master/large_image/IS02.png)
## [↑回目錄](https://github.com/HTY62006/MyLearningNote/tree/master/Week4#%E7%9B%AE%E9%8C%84)

## [回首頁](https://github.com/HTY62006/MyLearningNote)