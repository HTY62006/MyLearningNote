# Heap Sort
## 目錄
* [文字說明](https://github.com/HTY62006/MyLearningNote/blob/master/HW2/Heap_Sort_%E8%AA%AA%E6%98%8E.md#%E6%96%87%E5%AD%97%E8%AA%AA%E6%98%8E)
  * [Heap觀念](https://github.com/HTY62006/MyLearningNote/blob/master/HW2/Heap_Sort_%E8%AA%AA%E6%98%8E.md#heap%E8%A7%80%E5%BF%B5)
  * [實踐Heap的影片參考]
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
> 參考資料：[Python heapq.heapify() Examples](https://www.programcreek.com/python/example/2770/heapq.heapify)、[heapq --- 堆積佇列 (heap queue) 演算法](https://docs.python.org/zh-tw/3/library/heapq.html)
#### 實踐Heap的影片參考
1. Max Heapify
[![](http://img.youtube.com/vi/5iBUTMWGtIQ/0.jpg)](http://www.youtube.com/watch?v=5iBUTMWGtIQ "")
2. Build Max Heap
[![](http://img.youtube.com/vi/WsNQuCa_-PU/0.jpg)](http://www.youtube.com/watch?v=WsNQuCa_-PU "")
