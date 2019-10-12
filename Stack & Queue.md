# Week3: Stack and Queue
Leetcode練習題：155. Min Stack、232. Implement Queue using Stacks

這是我練習的[完整程式碼(Stack)](https://github.com/HTY62006/MyLearningNote/blob/master/Leetcode/week3/155.%20Min%20Stack.py)、[完整程式碼(Queue)](https://github.com/HTY62006/MyLearningNote/blob/master/Leetcode/week3/232.%20Implement%20Queue%20using%20Stacks.py)
## 目錄
  * 簡介
    * [Stack](https://github.com/HTY62006/MyLearningNote/blob/master/Stack%20%26%20Queue.md#stack)
    * [Queue](https://github.com/HTY62006/MyLearningNote/blob/master/Stack%20%26%20Queue.md#queue)
## 簡介
### Stack
#### 為什麼要有Stack？
  * 編譯器(word、sublime)的 undo 。
  * 網頁瀏覽器中回到上一頁功能。
  * 任何遞迴(recursion)形式的演算法都可以用 Stack 改寫，例如 Depth-First Search（DFS，深度優先搜尋）。
#### 概念
![image](https://images.plurk.com/uSBU6dR5mM2KECR0Kxlzu.png)
  * 先進後出，後進先出。
  * `先插入的後刪除`
  * 堆疊（一層一層往上疊的概念）。
#### 功能
  * **`Push(data)`**：將資料放進Stack。
  * **`Pop`**：將「最上方」（最新）的資料從Stack中移除。
  * **`Top`**：回傳「最上方」（最新）的資料。
  * **`IsEmpty`**：確認Stack中是否有資料。
  * **`getSize`**：回傳Stack中的資料個數。

## [↑回目錄](https://github.com/HTY62006/MyLearningNote/blob/master/Stack%20%26%20Queue.md#%E7%9B%AE%E9%8C%84)

### Queue
#### 為什麼要有Queue？
  * 演算法──Bread-First Search（廣度優先搜尋）和Tree的Level-Order Traversal會用到Queue。
  * 因作業系統一次只能執行一個需求，故在多個應用程式共享資源時，須使用Queue來安排多個程式的執行順序。
#### 概念
![image](https://images.plurk.com/1OipRi9PnsLT8T65EwOiEK.png)
  * 先進先出，後進後出。
  * `先插入的先刪除`
  * 像排隊一樣
![image](https://images.plurk.com/40mSgBftqNG1TIIgbCURQo.png)
#### 功能
  * **`Push(data)`**：將資料從「後方」放入Queue，並更新成新的Back。
  * **`Pop`**：把位於Front的資料從Queue中刪除，並更新Front。刪除Queue中的資料又稱為dequeue。
  * **`grtFront`**：回傳Front所指向的資料。
  * **`getBack`**：回傳Back所指向的資料。
  * **`IsEmpty`**：確認Queue中是否有資料。
  * `**getSize**`：回傳Queuek中的資料個數。

## [↑回目錄](https://github.com/HTY62006/MyLearningNote/blob/master/Stack%20%26%20Queue.md#%E7%9B%AE%E9%8C%84)

## Min Stack
