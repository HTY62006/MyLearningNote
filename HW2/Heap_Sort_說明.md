# Heap Sort
## 目錄
* 文字說明
  * Heap觀念
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
