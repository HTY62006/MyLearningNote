# Linked List
Leetcode練習題：707. Design Linked List

這是我練習的[完整程式碼](https://github.com/HTY62006/MyLearningNote/blob/master/Leetcode/week2/707.%20Design%20Linked%20List.py)
## 簡介
![image](https://images.plurk.com/3WmW9M1NCnoNrKKQ8pYY2T.png)

Linked list是由 **Node（節點）** 和 **Pointer** 組成，Node為儲存資料資料的實際位置，散落在記憶體中不同的位置，Pointer則是將各個Node與Node串接在一起。而NULL則是Linked list的結尾。以上圖為例：

* Node1：Node1裡頭的值為1，經由Pointer（接在1後方的空格）接續到Node2。
* Node2：Node2裡頭的值為3，經由Pointer接續到Node3。
* Node3：Node3裡頭的值為2，Pointer後沒有內容(NULL)，故Linked list結束。
