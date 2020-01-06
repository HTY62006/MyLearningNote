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
## Week4: Set and Insertion Sort
## Set Mismatch
Leetcode練習題：645. Set Mismatch
### 需求
nums應為一個內容為1~n的list：nums = [1, 2, 3, 4,..., n]。
1. 回傳nums的重複項
2. 回傳nums的缺失值
* Example:
```Text
Input: nums = [1,2,2,4]
Output: [2,3]
```
### 實作與想法
假設nums = [1,2,2,4]
1. 由於正確的內容一定是[1,2,3,...,n]，所以先以`set()`來將輸入的nums去除重複值後輸出成non_dup。
   > 此時non_dup = {1,2,4}
   ```Python
   non_dup = set(nums)
   ```
2. 將nums與non_dup各自加總，相減後可得到重複的值(dup)。
   > 此時dup = 2
   ```Python
   dup = sum(nums) - sum(non_dup)
   ```
3. 創建一擁有正確內容的list。
   > 此時correct = [1,2,3,4]
   ```Python
   correct = []
   for i in range(1, len(nums)+1):
       correct.append(i)
   ```
4. 以`set()`將coorect與nums去除重複值後相減。
   > 因此時資料型態為<class 'set'>，再加上結果只會有一數字，故以將相減的結果加總的方式將值轉為int。
   >> 此時miss = 3
   ```Python
   miss = sum(set(correct) - set(nums))
   ```
5. 最後可回傳結果為[2,3]
## Insertion Sort
Leetcode練習題：147. Insertion Sort List
## 簡介
Insertion Sort（插入排序法）：
1. 將資料分為**已排序**與**未排序**。
2. 將未排序的**第一筆資料**插入已排序中適當的位置。
   * 已排序的值**大於等於**正在處理的值→已排序的值往右移。
   * 遇到第一個**小於**正在處理的值時，才進行插入。

![image](https://images.plurk.com/7pFxYHFs6R9cbdqE3hy7ot.png)

如上圖所示：
* 綠色：未排序的資料
* 橘色：已排序的資料
* 白色：正在處理的資料
> 參考：[【演算法】插入排序法(Insertion Sort)](http://notepad.yehyeh.net/Content/Algorithm/Sort/Insertion/1.php)
## [↑回目錄](https://github.com/HTY62006/MyLearningNote/tree/master/Week4#%E7%9B%AE%E9%8C%84)
## Insertion Sort List
### 需求
使用Insertion Sort對Linke list進行排序。
* Example 1
  ```Text
  Input: 4->2->1->3
  Output: 1->2->3->4
  ```
* Example 2
  ```Text
  Input: -1->5->3->4->0
  Output: -1->0->3->4->5
  ```
### 實作與想法
假設輸入的節點依序為4->2->1->3。
1. 默認Linked list原先的首位為已排序的資料，`head.next`成為後方未排序資料的`head`。
   > 此時已排序的資料值 out = 4，未排序的資料值 head = 2，t = 4。
   ```Python
   out = head
   head = head.next
   t = out
   ```
2. 以while迴圈在Linked list未結束時進行判斷。
   * 先設定要進行測試的元素，及其餘未排序資料新的head。
   * 如果測試的元素**小於等於**已排序的元素，則已排序值往右移。
   > 第一輪：test值 = 2，head值 = 1，out值 = 4。因2<4，可得到out為2->4。
   >> 第二輪：test值 = 1，head值 = 3，out為2->4。因1<2<4，可得到out為1->2->4。
   >>> 第三輪：test值 = 3，Linke list已到底，head = None，out為1->2->4。因測試元素既不小於已排序，也不大於後方的元素（已經是最後一次排序）。
   >>>> 令n=out（已排序元素），當n.next≠後方元素且n.next的值<測試元素(test)的值時，n = n.next（結果：n的值為2）
   >>>>> n.next為4，test為3，test.next = n.next（3->4）
   >>>>>> test(3->4)，n(1->2)，n.next = test（1->2->3->4）
     ```Python
     while head != None:
            test = head # 測試值
            head = head.next
            if test.val <= out.val:
                test.next = out
                out = test
            elif test.val >= t.val:
                t.next = test
                t = test
            else:
                n = out
                while n.next != t and n.next.val < test.val:
                    n = n.next
                test.next = n.next
                n.next = test
     ```
3. 將Linked list尾部設為None，並回傳結果out。
   > t.val = 4，t.next = None
   >> 1->2->3->4->None，Linked list結束。out為經insertion sort排序後的結果。
   ```Python
   t.next = None
   return out
   ```
## 解題說明圖(Insertion Sort List)
![image](https://github.com/HTY62006/MyLearningNote/blob/master/large_image/IS02.png)
[點此可看大圖](https://raw.githubusercontent.com/HTY62006/MyLearningNote/master/large_image/IS02.png)

## [回首頁](https://github.com/HTY62006/MyLearningNote)
