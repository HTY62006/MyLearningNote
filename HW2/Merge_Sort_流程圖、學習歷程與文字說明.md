# Merge Sort
## 目錄
* [文字說明](https://github.com/HTY62006/MyLearningNote/blob/master/HW2/Merge_Sort_%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87%E6%96%87%E5%AD%97%E8%AA%AA%E6%98%8E.md#%E6%96%87%E5%AD%97%E8%AA%AA%E6%98%8E)
  * [Merge Sort觀念](https://github.com/HTY62006/MyLearningNote/blob/master/HW2/Merge_Sort_%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87%E6%96%87%E5%AD%97%E8%AA%AA%E6%98%8E.md#merge-sort%E8%A7%80%E5%BF%B5)
* [學習歷程](https://github.com/HTY62006/MyLearningNote/blob/master/HW2/Merge_Sort_%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87%E6%96%87%E5%AD%97%E8%AA%AA%E6%98%8E.md#%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B)
  * [嘗試自己寫merge sort](https://github.com/HTY62006/MyLearningNote/blob/master/HW2/Merge_Sort_%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87%E6%96%87%E5%AD%97%E8%AA%AA%E6%98%8E.md#%E5%98%97%E8%A9%A6%E8%87%AA%E5%B7%B1%E5%AF%ABmerge-sort)
* 流程圖
## 文字說明
### Merge Sort觀念
步驟：
1. 將數列對半分割。
2. 持續分割到直到每個數列都只剩下一個數。
3. 開始逐步合併，合併完成的數列須由小排到大。
4. 合併兩個數以上的數列時，比較排在前方的數，並移動較小的部分。
5. 反覆進行合併直到排序結束。
> 參考資料：[演算法圖鑑](https://www.books.com.tw/products/0010771263)p.70~p.73

☆先拆分，再合併☆

![image](https://images.plurk.com/4k4d6k74pXge9a0LLcSqqn.png)
## 學習歷程
### 嘗試自己寫merge sort
我的想法是因為merge sort必須逐步合併，切割到不能再切後，將分割完的部分鐘左右的數比較移完再合併，形成遞迴。
![image](https://images.plurk.com/7E37W8EnuOeWl6NL06LDDi.png)

```Python
def merge_sort(nums):
    if len(nums)<=1:
        return(nums) # 如果輸入的list<=1，直接回傳
    else:
        split_point = len(nums)//2 # 分割點
        left = merge_sort(nums[:split_point])
        right = merge_sort(nums[split_point:])
        return merge(left, right) # 合併
 ```
利用`merge(left, right)`來將left與right中的數進行比較後，再合併。
```Python
def merge(left, right):
    i = 0
    j = 0
    while left and right: # 如果left和right存在
        if left[i]>=right[j]:
            move = left[i]
            left[i] = right[j]
            right[j] = move
            j+=1
        else:
            i+=1
```
此時會出現錯誤**IndexError: list index out of range**，檢查後發現是因為我是用while搭配i和j來對left和right進行判斷的，while迴圈形成的條件是當left和right存在，因此i和j無法在已經超出list範圍時停止，迴圈依舊執行。導致i和j最後超出left和right他們index的範圍。

於是我加上i<left的長度和j<right的長度這兩個條件。
```Python
while left and right and i<len(left) and j<len(right): # 如果left和right存在
    if left[i]>=right[j]:
        move = left[i]
        left[i] = right[j]
        right[j] = move
        j+=1
    else:
        i+=1
```
![image](https://images.plurk.com/6g4kWS8T1KMnG63XByu03q.png)

因為我沒有考慮到在合併時，不但要left和right比較並互換，而且互換完後的left和right也要按順序排序。所以我加上兩個while迴圈來排序已經換完的部分。
```Python
l = 0
while l+1 < len(left):
    if left[l] > left[l+1]:
        move = left[l]
        left[l] = left[l+1]
        left[l+1] = move
        l+=1
r = 0
while r+1 < len(right):
    if right[r] > right[r+1]:
         move = right[r]
         right[r] = right[r+1]
         right[r+1] = move
         r+=1
```
結果反而變成無限迴圈，我想我可能搞錯了什麼，所以從頭推一遍自己的流程看看究竟怎麼回事。
![image](https://images.plurk.com/Be5KAsOMfLkGSF6yqp57s.png)

A
> 參考資料：[Merge sort and quick sort](https://www.slideshare.net/MJabin/merge-sort-and-quick-sort)[Merge Sort | GeeksforGeeks](https://www.youtube.com/watch?v=JSceec-wEyw)
