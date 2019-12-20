# BFS and DFS
## 目錄
* [原理與比較](https://github.com/HTY62006/MyLearningNote/blob/master/HW5/BFS%26DFS.md#%E5%8E%9F%E7%90%86%E8%88%87%E6%AF%94%E8%BC%83)
* [流程圖](https://github.com/HTY62006/MyLearningNote/blob/master/HW5/BFS%26DFS.md#%E6%B5%81%E7%A8%8B%E5%9C%96)
* [學習歷程](https://github.com/HTY62006/MyLearningNote/blob/master/HW5/BFS%26DFS.md#%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B)
## 原理與比較
### BFS原理
Breadth-First-Search，廣度優先搜尋。
* 概念：
會優先搜尋離起點較近的點，因為點是「先進先出」，所以可以用佇列(Queue)來處理。如果終點距離起點很近的話，搜尋可快就會結束。
* 步驟：

步驟    | 說明
--------|-------------------------
Level 0 | 起點
Level 1 | 起點可立即訪問的其他點 
Level 2 | Level 1的點可立即訪問的其他點
...     | ...

重複以上步驟，直到所有點被走訪完畢。
> 參考資料：[上課簡報](https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.g7a5d8b85ee_0_23)、演算法圖鑑p.92~p.95
### DFS原理
Depth-First-Search，深度優先搜尋。
* 概念：
訪問單一路徑，直到無法前進則折返。因為點是「後進先出」，所以可以使用堆疊(Stack)處理。
* 步驟：
1. 先遇到的鄰點先訪問。
2. 並以該點作為搜尋起點。
3. 直到所有的點都走訪過。
> 參考資料：[上課簡報](https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.g7a5d8b85ee_0_23)、演算法圖鑑p.96~p.99
### BFS和DFS比較
* 兩者其實相似，差別在於BFS使用的是Queue；DFS使用的是Stack。
* BFS是立即訪問到該點可訪問到的點並標記。
* DFS是先遇到的點先訪問，且每個臨點都是新的搜尋起點。
* 共通點是「直到所有相連的點」都走訪過。
> 參考資料：[Difference Between BFS and DFS(techdifferences)](https://techdifferences.com/difference-between-bfs-and-dfs.html)、[Difference Between BFS and DFS(geeksforgeeks)](https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/)

在參考上述網站後，發現兩者之間還有些不同。

比較    | BFS | DFS
--------|-----|--------------------
效率 | 低效 | 高效
最佳性 | 最適合用來找最短路徑 | 不是最佳
時間複雜度 | O(V + E) | O(V + E)

## 流程圖
### BFS
![image](https://images.plurk.com/5p2wlLCtoFK1K3oV0weyWl.jpg)
![image](https://images.plurk.com/2XZN2AkUFOwx9gxZI1Xgz8.jpg)
### DFS
![image](https://images.plurk.com/tlCBIAzLTvikxcjgKD9ZM.jpg)
![image](https://images.plurk.com/t4jp6CDlj8EBd9WcpSgjf.jpg)
## 學習歷程
### BFS
以課堂中老師教過的走訪方式為發想，因為queue是先進先出，因此沒有另外設定後續可加入點需要使用的空間。（令一個變數y=0，讓它逐一指定到state2的位子。）
```Python
state1=[0]*len(self.graph)#設定一個list表該點尚未造訪過(尚未造訪=0，已造訪=1)
state2=[]#final
state2.append(s)
y = 0
while len(state2) <= len(state1):
    x = state2[y]#queue是先進先出
    if state1[x] != 1:#如果還沒被標記成造訪過
        state1[x] = 1#標記造訪過
        for i in self.graph[x]:
    if state1[i] != 1:
                state2.append(i)#還沒造訪過就加入state2
    y+=1
retrun state2
```
此時會出現一個問題是：
```Text
# IndexError: list index out of range
# 0 [2, 0, 3]
# 1 [2, 0, 3, 1]
# 2 [2, 0, 3, 1]
# 3 [2, 0, 3, 1]
```
檢查時發現是因為我的y沒設限，跑最後一圈時回超出範圍，因此在while的條件加上y < len(state1)的限制。
> 參考資料：[The Breadth First Search Graph traversal algorithm
](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/11-Graph/bfs.html)
>> enqueue(進入)、dequeue(離開)

換了一個測值進行測試，出現問題是已經加入的點會被重複加入。檢查後發現是因為我的程式會造成我有些點已經加入state2，但尚未被標成造訪過，所以加上條件排除這個情況。我是使用`.count()`來計算該點是否已在state2中。

修改過後：
```Python
state1=[0]*len(self.graph)#設定一個list表該點尚未造訪過(尚未造訪=0，已造訪=1)
state2=[]#final
state2.append(s)
y = 0
while len(state2) < len(state1) and y < len(state1):
    x = state2[y]#queue是先進先出
    if state1[x] != 1:#如果還沒被標記成造訪過
        state1[x] = 1#標記造訪過
        for i in self.graph[x]:
            if state1[i] != 1 and state2.count(i) == 0:#排除已加入，但尚未標造訪過的點
                state2.append(i)#還沒造訪過就加入state2
    y+=1
return state2
```
測試幾個測值後回傳結果均正確。
### DFS
DFS和BFS不同的地方在於它是後進先出(stack)，以及每次造訪他都會是一個新的起點。
```Python
state=[0]*len(self.graph)#設定一個list表該點尚未造訪過(尚未造訪=0，已造訪=1)
state1=[]#check
state2=[]#final
while len(state2) <= len(state) and len(state1)>0:
    x = state1[-1]
    print('x',x,state1)
    if state[x] != 1:#如果還沒被標記成造訪過
        state[x] = 1#標記造訪過
        state2.append(x)
        print(state2)
        state1.pop()
        for i in self.graph[x]:
            if state[i] != 1 and state2.count(i) == 0:#排除已加入，但尚未標造訪過的點
                state1.append(i)
return state2
```
原先我以課堂上老師教過的走訪過程來撰寫程式，會出現問題是會回傳錯誤表示：取-1超出index範圍，這是因為一開始就是空的。照我的寫法，我的state1應該要先放入起點。
```Python
state1=[s]#check
```
測試時發現，有些測值會出現無限迴圈。仔細想想，DFS和BFS在走訪過程中只有一些不同，也許我可以用類似BFS程式的結構來寫DFS。
```Python
state=[0]*len(self.graph)#設定一個list表該點尚未造訪過(尚未造訪=0，已造訪=1)
state1=[s]#check
state2=[]#final
while len(state2) <= len(state):
    x = state1.pop()#stack是後進先出，pop會回傳刪除的值並刪除
    if state[x] != 1:#如果還沒被標記成造訪過
        state[x] = 1#標記造訪過
        state2.append(x)#造訪後加入
        for i in self.graph[x]:
            if state[i] != 1 and state2.count(i) == 0:#排除已加入，但尚未標造訪過的點
                state1.append(i)#還沒造訪過就加入state1
return state2
```
修改後，加上pop()會回傳被刪除的值（直接刪除最後一個），因此我將我的程式簡化成x=state1.pop()。
> 參考資料：[The Depth First Search Graph traversal algorithm](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/11-Graph/dfs.html)

![image](https://images.plurk.com/36P7ofZAR8G7wwD9sA5t9c.png) ![image](https://images.plurk.com/1LjwVoGRjOJ8RJXHDcZmhI.png) ![image](https://images.plurk.com/Dn5KS9QwrtHMApvkyM6Pw.png)
測試後的結果應該無誤。
## 參考資料
1. [上課簡報](https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.g7a5d8b85ee_0_23)
2. 演算法圖鑑p.96~p.99
3. [The Depth First Search Graph traversal algorithm](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/11-Graph/dfs.html)
4. [The Breadth First Search Graph traversal algorithm
](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/11-Graph/bfs.html)
5. [Difference Between BFS and DFS(techdifferences)](https://techdifferences.com/difference-between-bfs-and-dfs.html)
6. [Difference Between BFS and DFS(geeksforgeeks)](https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/)
