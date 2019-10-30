# Heap Sort
## 目錄
* [文字說明](https://github.com/HTY62006/MyLearningNote/blob/master/HW2/Heap_Sort_%E8%AA%AA%E6%98%8E.md#%E6%96%87%E5%AD%97%E8%AA%AA%E6%98%8E)
  * [Heap觀念](https://github.com/HTY62006/MyLearningNote/blob/master/HW2/Heap_Sort_%E8%AA%AA%E6%98%8E.md#heap%E8%A7%80%E5%BF%B5)
  * [Heap Sort觀念](https://github.com/HTY62006/MyLearningNote/blob/master/HW2/Heap_Sort_%E8%AA%AA%E6%98%8E.md#heap-sort%E8%A7%80%E5%BF%B5)
* [學習歷程]
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
        if (left < len(A)-1) and (A[left] > A[root]):
            MaxIndex = left
        else:
            MaxIndex = root
            
        if (right < len(A)-1) and (A[right] > A[MaxIndex]):
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
