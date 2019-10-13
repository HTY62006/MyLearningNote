# Week3: Stack and Queue
Leetcode練習題：155. Min Stack、232. Implement Queue using Stacks

這是我練習的[完整程式碼(Stack)](https://github.com/HTY62006/MyLearningNote/blob/master/Leetcode/week3/155.%20Min%20Stack.py)、[完整程式碼(Queue)](https://github.com/HTY62006/MyLearningNote/blob/master/Leetcode/week3/232.%20Implement%20Queue%20using%20Stacks.py)

## [回首頁](https://github.com/HTY62006/MyLearningNote)

## 目錄
  * 簡介
    * [Stack](https://github.com/HTY62006/MyLearningNote/blob/master/Stack%20%26%20Queue.md#stack)
    * [Queue](https://github.com/HTY62006/MyLearningNote/blob/master/Stack%20%26%20Queue.md#queue)
  * [Min Stack](https://github.com/HTY62006/MyLearningNote/blob/master/Stack%20&%20Queue.md#min-stack)
  * [Implement Queue using Stacks](https://github.com/HTY62006/MyLearningNote/blob/master/Stack%20&%20Queue.md#implement-queue-using-stacks)
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
  * **`getSize`**：回傳Queuek中的資料個數。

## [↑回目錄](https://github.com/HTY62006/MyLearningNote/blob/master/Stack%20%26%20Queue.md#%E7%9B%AE%E9%8C%84)

## Min Stack
### 需求
  * **`Push(x)`**：新增一個元素進入Stack。
  * **`pop()`**：移除Stack中位於Top的元素。
  * **`top()`**：得到位於Top的元素。
  * **`getMin()`**：回傳最小值。
### 實作與想法
利用List來實行。
1. 先創建一個空的list。
   ```Python
   def __init__(self):
       self.items = []
   ```
2. Push(x)：新增元素進入Stack（位於Top），利用`.append()`將元素新增入list形成Stack。
   ★如果list=[1,2,3]，那麼作為Stack的實際排序由上至下其實是3→2→1★
   ```Python
   def push(self, x: int) -> None:
       self.items.append(x)
   ```
3. pop()：因Stack的實際排序是list的相反，故在移除位於Top的元素時，需移除位於list中最後一位的值（利用`.pop()`）。
   ```Python
   def pop(self) -> None:
       self.item.pop()
   ```
4. top()：Top需取list中最後一位，故回傳list的[-1]項。
   ```Python
   def top(self) -> int:
       return self.item[-1]
   ```
5. getMin()：回傳最小值，使用`min()`可得到最小值。
   ```Python
   def getMin(self) -> int:
       return min(self.item)
   ```
   
## [↑回目錄](https://github.com/HTY62006/MyLearningNote/blob/master/Stack%20%26%20Queue.md#%E7%9B%AE%E9%8C%84)

## Implement Queue using Stacks
### 需求
  * **`push(x)`**：自Queue的Back新增元素進入Queue。
  * **`pop()`**：刪除Queue中位於Front的元素。
  * **`peek()`**：得到位於Front的元素。
  * **`empty()`**：判斷Queue是否為空。
### 實作與想法
利用List來實行。
1. 先創建一個空的list。
   ```Python
   def __init__(self):
       self.items = []
   ```
2. push(x)：自Back新增元素進入Queue，利用`.append()`新增。
   ```Python
   def push(self, x: int) -> None:
       self.items.append(x)
   ```
3. pop()：移除位於Front的元素，利用`pop()`將位於list的[0]項（Queue的Front）刪除。
   ```Python
   def pop(self) -> int:
       return self.items.pop(0)
   ```
4. peek()：回傳位於Front的元素，故取list的[0]項。
   ```Python
   def peek(self) -> int:
       return self.item[0]
   ```
5. empty()：如果Queue為空，意味著長度為0，故當長度為0時回傳。
   ```Python
   def empty(self) -> bool:
       return len(self.item) == 0
   ```
   
## [↑回目錄](https://github.com/HTY62006/MyLearningNote/blob/master/Stack%20%26%20Queue.md#%E7%9B%AE%E9%8C%84)
## [回首頁](https://github.com/HTY62006/MyLearningNote)
