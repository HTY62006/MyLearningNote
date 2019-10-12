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
  * 堆疊（一層一層往上疊的概念）。
  * 以上圖為例，此時的最上層(Top)為3。
#### 功能
  * **`Push(data)`**：將資料放進Stack。
  * **`Pop`**：將「最上方」（最新）的資料從Stack中移除。
  * **`Top`**：回傳「最上方」（最新）的資料。
  * **`IsEmpty`**：確認Stack中是否有資料。
  * **`getSize`**：回傳Stack中的資料個數。

### Queue
