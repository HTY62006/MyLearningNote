# MyLearningNote

巨資三B 06170232 洪敦媛
# 資料結構與演算法
## 目錄
1. Leetcode作業
* Week2: [Linked List](https://github.com/HTY62006/MyLearningNote#week2-linked-list)

## Leetcode作業
### Week2: Linked List
Leetcode練習題：707. Design Linked List

這是我練習的[完整程式碼](https://github.com/HTY62006/MyLearningNote/blob/master/Leetcode/week2/707.%20Design%20Linked%20List.py)
#### 簡介
![image](https://images.plurk.com/3WmW9M1NCnoNrKKQ8pYY2T.png)

Linked list是由 **Node（節點）** 和 **Pointer** 組成，Node為儲存資料資料的實際位置，散落在記憶體中不同的位置，Pointer則是將各個Node與Node串接在一起。而NULL則是Linked list的結尾。以上圖為例：

* Node1：Node1裡頭的值為1，經由Pointer（接在1後方的空格）接續到Node2。
* Node2：Node2裡頭的值為3，經由Pointer接續到Node3。
* Node3：Node3裡頭的值為2，Pointer後沒有內容(NULL)，故Linked list結束。

Linked list是不連續的，故可有效利用記憶體的空間。

#### Design Linked List
需求：
1. `get(index)`：輸入**index**可取得Linked list中對應的值。
2. `addAtHead(val)`：將輸入新的值作為第一個節點插入Linked list的首位。
3. `addAtTail(val)`：將輸入新的值作為最後一個節點插入Linked list的尾部。
4. `addAtIndex(index, val)`：在對應的**Index**插入輸入的值。
    * 當index = Linked list長度，則將值插入Linked list尾部。
    * 當index > Linked list長度，則不會插入Linked list。
    * 當index < 0，則將值插入Linked list的首位。
5. `deleteAtIndex(index)`：若**index**為有效的，則刪除Linked list中對應的值。

我的作法：
