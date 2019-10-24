# Heap Sort
## 目錄
* Heap
  * [簡介](https://github.com/HTY62006/MyLearningNote/tree/master/Week6#%E7%B0%A1%E4%BB%8B)
## Heap
### 簡介
Heap，堆積，為一種**樹狀結構**。每個頂點稱為節點(Node)，值儲存在節點中。
* Min heap
<br>所有父節點 **<** 子節點。

![image](https://github.com/HTY62006/MyLearningNote/blob/master/large_image/HS01.png)
* Max heap
<br>所有父節點 **>** 子節點。

![image](https://github.com/HTY62006/MyLearningNote/blob/master/large_image/HS02.png)
#### Heap的插入與刪除
```Text
以下以min heap來進行說明。
```
* 插入
1. 從**最尾部**的節點開始插入值。若最下方的階層被填滿，便產生新的階層，從**左方**開使插入值。
2. 判斷是否需要將插入的節點向上移動。（若小於父節點，則需上移，將其與父節點對調。）
* 刪除
1. 從heap取出值時，從**最上方**取出值。
2. 因此時最上方的值為空，需將heap**最尾部**的數，移至最上方。
3. 子節點與父節點進行比對，
   * 若父節點皆大於子節點，將兩子節點中較小的一方與父節點對調。
   * 子節點2 > 父節點 > 子節點1，則將子節點1與父節點對調。
```Text
* 最上方永遠是最小的值。
* 刪除值，重整結構時需反覆將上提的最尾部數據與子節點反覆比較，往下排序。
* 插入值，需反覆與父節點比較後往上移動。
→ 直到滿足heap的條件。
```
