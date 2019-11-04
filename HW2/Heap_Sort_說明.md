# Heap Sort
## 目錄
* [文字說明](https://github.com/HTY62006/MyLearningNote/blob/master/HW2/Heap_Sort_%E8%AA%AA%E6%98%8E.md#%E6%96%87%E5%AD%97%E8%AA%AA%E6%98%8E)
  * [Heap觀念](https://github.com/HTY62006/MyLearningNote/blob/master/HW2/Heap_Sort_%E8%AA%AA%E6%98%8E.md#heap%E8%A7%80%E5%BF%B5)
  * [Heap Sort觀念](https://github.com/HTY62006/MyLearningNote/blob/master/HW2/Heap_Sort_%E8%AA%AA%E6%98%8E.md#heap-sort%E8%A7%80%E5%BF%B5)
* [學習歷程](https://github.com/HTY62006/MyLearningNote/blob/master/HW2/Heap_Sort_%E8%AA%AA%E6%98%8E.md#%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B)
  * [嘗試創建Heap](https://github.com/HTY62006/MyLearningNote/blob/master/HW2/Heap_Sort_%E8%AA%AA%E6%98%8E.md#%E5%98%97%E8%A9%A6%E5%89%B5%E5%BB%BAheap)
  * [嘗試進行Heap Sort](https://github.com/HTY62006/MyLearningNote/blob/master/HW2/Heap_Sort_%E8%AA%AA%E6%98%8E.md#%E5%98%97%E8%A9%A6%E9%80%B2%E8%A1%8Cheap-sort)
## 文字說明
### Heap觀念
對於Heap的觀念詳細說明---->[【請點我】](https://github.com/HTY62006/MyLearningNote/blob/master/Week6/README.md)
#### 重點整理
1. Heap是一種樹狀結構。
2. 視max heap或min heap的不同，呈現兩種情況：
   * `Max heap`：父節點 > 子節點
   * `Min heap`：父節點 < 子節點
3. Heap的插入與刪除：
   * `插入`：從最尾部插入，與父節點比較是否需向上移動
   * `刪除`：從最上方移出，需重整結構（將最尾部資料移至最上方後，向子節點比較是否需向下移動）
> 參考資料：[[資料結構]堆積(Heap)](https://ithelp.ithome.com.tw/articles/10206479)、[演算法圖鑑](https://www.books.com.tw/products/0010771263)p.42~p.45
### Heap Sort觀念
#### 簡介
```Text
以下為假設使用Max heap的情況之下。
```
步驟：
1. 以Max Heap的形勢將所有數儲存進heap中。
2. 將root取出，排到數列**最右側**。
3. 將最尾部的資料移至最上方，重新將heap排序，得到**新的root**。
4. 新root排到數列**右側第二個位子**。
5. 以此類推，不斷重複取root和重新排列heap的動作，**直到取出所有的數**。
6. 完成排序。
> 參考資料：[演算法圖鑑](https://www.books.com.tw/products/0010771263)p.66~p.68

![image](https://raw.githubusercontent.com/HTY62006/MyLearningNote/master/large_image/HS04.jpg)
## 學習歷程
### 嘗試創建Heap
1. 原先的想法
> 參考資料：[Heap - Max Heapify](https://www.youtube.com/watch?v=5iBUTMWGtIQ)
```Python
def MaxHeapify(A):
    for i in range(len(A)):
        root = i
        left = i*2+1
        right = i*2+2
        if (left < len(A)) and (A[left] > A[root]):
            MaxIndex = left
        else:
            MaxIndex = root
            
        if (right < len(A)) and (A[right] > A[MaxIndex]):
            MaxIndex = right
        else:
            MaxIndex = root
            
        if MaxIndex != root:
            change = A[root]
            A[root] = A[MaxIndex]
            A[MaxIndex] = change
        print(A)
```
假設我輸入的list為[3,2,1,1,7,8]，會出現問題是：**最後回傳的是[3, 7, 1, 1, 2, 8]**。
![image](https://images.plurk.com/1NTrL2FBVUmxlhYtukjdbh.png)

----> 不符合heap規則

2. 參考別人的教學，再次確定自己是否哪裡想法有誤。
> 參考資料：[Heap - Build Max Heap](https://www.youtube.com/watch?v=WsNQuCa_-PU)

依照影片的說明，從最底一層往上確認回去。
```Python
def build_maxheap(A):
    for i in range(len(A)-1, -1, -1):
        root = i/2
        maxheapify(A, root)
```
此處執行時發生**TypeError: list indices must be integers or slices, not float**，檢查後發現是在設置root對應的index時用錯除法。
> 參考資料：[給自學者的Python教學(5)：算術運算子](https://medium.com/@ChunYeung/%E7%B5%A6%E8%87%AA%E5%AD%B8%E8%80%85%E7%9A%84python%E6%95%99%E5%AD%B8-5-%E7%AE%97%E8%A1%93%E9%81%8B%E7%AE%97%E5%AD%90-6fd923561349)

在python之中，算術運算子「/」和「//」的差異是：

運算子 | 說明
------|-------------------------------------
/     | 結果包含小數點，資料型態為float
//    | 整數除法，結果不含小數點，資料型態為int

因原本root想求整數，卻使用成/，故會出現此錯誤。因此修改成root = i//2。
```Python
def build_maxheap(A):
    for i in range(len(A)-1, -1, -1):
        root = i//2 # 取整數結果
        maxheapify(A, root)
```
將list轉為heap。
<br>發現原先在檢查右方子節點時，else:  MaxIndex = root是多此一舉。此外，每次調整結構應是整個進行調整，不是僅調整部分。

修改後的程式碼：
```Python
def maxheapify(A, root):
    left = root*2+1 # 左子節點
    right = root*2+2 # 右子節點
    # 如果left值>root值，那目前此階段最大值的index為left
    if (left < len(A)) and (A[left] > A[root]):
        MaxIndex = left
    else:
        MaxIndex = root # 沒有的話就仍是root
    # 和最大值比較，right值若較大，則取代原先max_index成為新的最大值的index        
    if (right < len(A)) and (A[right] > A[MaxIndex]):
        MaxIndex = right
    # 若最大值的index和輸入的root不一致，則代表需要互換
    if MaxIndex != root:
        change = A[root]
        A[root] = A[MaxIndex] #互換
        A[MaxIndex] = change
        maxheapify(A,MaxIndex) #檢查下一層是否符合heap規則
```
![image](https://raw.githubusercontent.com/HTY62006/MyLearningNote/master/large_image/HS03.jpg)
### 嘗試進行Heap Sort
```Text
採用Max heap來進行heap sort。
```
我的想法是先讓Max heap後的root(第一個值)和最後一個值交換，再針對除了已排序好的部分繼續做重新建構heap、取root、重新建構heap......的步驟。

因為寫在class中，呼叫class中的其他函式須加上self在前面。
```Python
def heap_sort(self, nums):
    self.buildMaxHeap(nums)
        
    for i in range(len(nums)-1, -1, -1):
        check_max_index = nums[0]
        nums[0] = nums[i]
        nums[i] = check_max_index
            
        self.buildMaxHeap(nums[:i])
    return nums
```
可是在回傳結果時發生了一個問題，沒有排序成功，因此檢查是哪部分出錯。
![image](https://images.plurk.com/3g2YVirwAYWflF3tx3sygW.png)

仔細想想，發現不對，我似乎也沒必要將值互換，如果照我原先的邏輯的話，我完全可以這麼做：
1. 將list轉為max heap。
2. max heap中index=0的值是最大值，將他取出。
3. 重整heap 結構。

這樣的話我似乎可以在heap sort的部分更簡單點的解決，因此我改以這種方式呈現。
```Python
def heap_sort(self, nums):
    numd = self.buildMaxHeap(nums)
    max_now = nums[0]       
    n = len(nums)-1
    return self.heap_sort(nums[:n])+[max_now]
```
此處執行時發生**IndexError: list index out of range**，後來發現自己是被原先的寫法給影響在設置後續要重整結構的部份時，將值給誤設為[:n]。因為假設原本我用互換的方式，比如說在第一次執行的時候[5,2,3]會先變成[3,2,5]，再對剩餘部分進行判斷。但現在我沒互換的前提下，我可以直接從1開始判斷。

另外我也發現我沒考慮到假設我想用return A+B的方式來實現遞迴的話，去排除如果已經沒法再分類的情況，因此也對此做出修改。

def heap_sort(self, nums)中修改後的程式：
```Python
if len(nums)>1:
    nums = self.buildMaxHeap(nums)
    max_now = nums[0]
    return self.heap_sort(nums[1:])+[max_now]
    else:
        return nums
```
