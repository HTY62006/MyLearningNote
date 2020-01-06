# Leetcode
## Week2: Linked List
Leetcode練習題：707. Design Linked List
## 簡介
![image](https://images.plurk.com/3WmW9M1NCnoNrKKQ8pYY2T.png)

Linked list是由 **Node（節點）** 和 **Pointer** 組成，Node為儲存資料資料的實際位置，散落在記憶體中不同的位置，Pointer則是將各個Node與Node串接在一起。而NULL則是Linked list的結尾。以上圖為例：

* Node1：Node1裡頭的值為1，經由Pointer（接在1後方的空格）接續到Node2。
* Node2：Node2裡頭的值為3，經由Pointer接續到Node3。
* Node3：Node3裡頭的值為2，Pointer後沒有內容(NULL)，故Linked list結束。

Linked list是不連續的，故可有效利用記憶體的空間。

## Design Linked List
### 需求：
1. `get(index)`：輸入**index**可取得Linked list中對應的值。
2. `addAtHead(val)`：將輸入新的值作為第一個節點插入Linked list的首位。
3. `addAtTail(val)`：將輸入新的值作為最後一個節點插入Linked list的尾部。
4. `addAtIndex(index, val)`：在對應的**Index**插入輸入的值。
    * 當index = Linked list長度，則將值插入Linked list尾部。
    * 當index > Linked list長度，則不會插入Linked list。
    * 當index < 0，則將值插入Linked list的首位。
5. `deleteAtIndex(index)`：若**index**為有效的，則刪除Linked list中對應的值。

### 我的作法：
1. 利用`ListNode`這個class來創建新的節點。`MyLinkedList`中定義self.head=None（Linked list為空），self.len=0為Linked list長度，self.len是為了以便後續作為判斷用。
2. `get(index)`是利用for迴圈將index對應的值抓取出來。
3. `addAtHead(val)`則創建值為val的新節點，若Linked list為空（長度為0），新節點直接定義為self.head；若Linked list不為空，則將新節點連接至原先Linked list的首位(self.head)，再定義新節點為self.head。
4. `addAtTail(val)`同樣創建值為val的新節點，將其插入原先Linked list的尾部。
5. `addAtIndex(index, val)`是若Linked list為空或index=0時，直接以`addAtHead(val)`來處理；若index>0，則創建值為val的新節點，將其插入對應位置。
6. `deleteAtIndex(index)`若長度為0，直接將Linked list化為空值；若index=0，則將該節點其後的節點直接設為self.head。其餘除不存在之情況，則將指定index對應的值刪除。
## Week3: Stack and Queue
Leetcode練習題：155. Min Stack、232. Implement Queue using Stacks
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
   <br>★如果list=[1,2,3]，那麼作為Stack的實際排序由上至下其實是3→2→1★
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
3. pop()：移除位於Front的元素，利用`.pop()`將位於list的[0]項（Queue的Front）刪除。
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

## [回首頁](https://github.com/HTY62006/MyLearningNote)
