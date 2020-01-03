# Dijkstra and Kruskal
## Dijkstra和Kruskal原理
### Dijkstra
Shortest path，最短路徑。Dijkstra是一種用來找`單源最短路徑`的方法。
1. 計算一個頂點到其他所有頂點的最短路徑，直到終點為止。
2. 某一點作為起點，造訪尚未造訪過的頂點。
3. 加入與起點距離最短的點，並藉此更新距離。
4. 重複加入直到所有頂點都被加入。
> 參考資料：[代克思托演算法 (Dijkstra's algorithm)](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dijkstra.html)
### Kruskal
Minimum spanning tree，最小生成樹。Kruskal是一種用來找`最小生成樹`的方法。
1. 所有邊依權重(Weight)大小排序。
2. 依序加入最小的邊。
3. 若形成cycle則不能加入。
![image](https://images.plurk.com/6QYHrsMBTDhWVuGjztR62K.png)
4. 直到變成n-1個邊為止。
## 流程圖
### Dijkstra
![image](https://images.plurk.com/1MKo8jvvha3oWlkUw8g1BM.jpg)
### Kruskal
![image]()
## 學習歷程
### Dijkstra
原本的想法是取最小值的位子，然後再將值依位子一步步加進去。
```Python
for i in range(self.V):
    if sum(self.graph_matrix[0]) == 0:#確認self.graph_matrix是否為空
        self.graph_matrix[i]=self.graph[s]#起點&第一步
#                 print(i, self.graph_matrix)
        short = self.shortest(s)#1-2
        final[str(short)]=self.graph_matrix[i][short]
        check[short]=True
#                 print(i, final, check)
    else:
#                 print(i)
        last_v = self.graph[s][short]
        last_p = short
        short = self.shortest(short)#第二步
        print(short, last_p)
def shortest(self, a):#取最短路徑
    c=[]
    for i in range(self.V):
        if self.graph[a][i] != 0 and check[i]!=True:
                c.append(self.graph[a][i])
#                     print(c)
    for i in range(self.V):
        if self.graph[a][i] == min(c):
            return i
```
檢查結果發現最短路徑有誤，變成頂點0和頂點1在輪流替換。又發現我現在的寫法，後面可能無法順利按老師課堂上教過的步驟進行。重新寫的時候想說，先把無法到達的點給標出來。
```Python
def infinity(self, a):
    inf = float("inf")#無窮大
    will_do=[inf]*self.V
    for i in range(len(will_do)):
#             print(i, a, type(a))
        if i==a or self.graph[a][i]!=0:
            will_do[i]=self.graph[a][i]
    return will_do
def shortest(self, i):#取最短路徑
    now = self.graph_matrix[i]
    c = []
    for r in range(self.V):
        if check[r] != True:
            c.append(self.graph_matrix[i][r])
    print(i,c)
    for k in range(self.V):
        if self.graph_matrix[i][k] == min(c):
            return k
        break
```
取最短路徑時發生一個問題：**NameError: name 'check' is not defined**
發現是我忘了將check放進去，所以shortest找不到check是什麼。但這之後有遇到一個問題是：雖然用手繪走訪圖我沒問題，但我沒辦法順利地將我想表達的相同樣子放進graph_matrix，一步驟一步驟呈現。因此我決定再看看更多的教學，重新釐清我的觀念。
> 參考資料：[[101北一資訊集訓] 07_1 最短路徑Shortest Path (part1: 單源最短路徑)](https://www.youtube.com/watch?v=NX2Qf0c75Og)、[戴克斯特拉算法](https://bit.ly/2MvNGXl)

我參考了pseudocode和影片的教學，理解後重新撰寫的程式的邏輯是：
1. 我先將所有無法到達的點標成 ∞ 。( *float("inf")* 可以表 ∞ )
2. 創建一個list `check` 來確認是否造訪過。(造訪過=True，未造訪=False)
3. 創建另一個list `d` 表示目前Dijkstra的情況。(到各點的最短路徑)
4. 先將起點與其能夠到達的點加入d。
5. 找出目前的點的**最短路徑的點和它的index**。
   * 會走訪該層的每一個點。
   * 每次都假設還沒造訪過的點中，第一個點是short，再逐一判定是否是最小值。
   * 確認是最小值後回傳最短路徑的點和index。
6. 確定找得到下一個點後，先將它標記成已加入。
7. 確認還沒走訪完的點，是否有點可以獲得更小的最短距離。
   * 是：將值替換。
8. 將結果轉成題目要求的dict。

我原先遇到最大的問題就是，我沒辦法順利將上一層與目前這一層，哪個點才是最短路徑這點完整的呈現出來，這期間出現的問題像是結果變成[0, 4, 12, 22, 21, 11, 9, 8, 15]，但這並沒有每個點都是最短路徑，顯然這過程中有誤。因為我原本是插入完再比較，現在重新撰寫過的是先確認加總的路徑長度是最短的，才插入，解決了我原先無法每個點都取到最短路徑的問題。
### Kruskal
> 參考資料：[Cycle in Undirected Graph Graph Algorithm](https://www.youtube.com/watch?v=n_t0a_8H8VY&t=163s)、[[101北一資訊集訓] 06_3_1 MST之Kruskal演算法(NEW)](https://www.youtube.com/watch?v=wuU4DDEUu1w&t=542s)、[Python 初學第十講 — 排序](https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-f3148ebb33a4)

我理解後撰寫的邏輯：
1. 將輸入的graph按權重排序。
2. 創建一個list `parent` 判定是否是同一個set。(-1表沒有root。)
3. 抓每一層的起點和終點。
   * 同一個set都標記成該set的起點。
   * 如果起點和終點位子的set相同，會導致cycle，因此將它移除。
4. 最後將結果按題目要求轉乘dict。

期間有遇到的問題是，我的結果和答案少一組解。後來發現是因為我少考慮了這種情況：
```Python
if parent[src]!=parent[dest]:#不同set且不是-1的話，仍可進行
    if parent[src]!=-1 and parent[dest]!=-1:
        parent = self.replace(parent,src,dest)
        parent[src]=src
```
補上這個情況後，結果就不會發生，應該要是**Kruskal {'4-5': 2, '0-2': 3, '2-3': 3, '1-2': 4, '3-4': 4}**，卻變成**Kruskal {'4-5': 2, '0-2': 3, '2-3': 3, '1-2': 4}**，少掉其中幾組解的情況。

## 參考資料總整理
1. [[101北一資訊集訓] 07_1 最短路徑Shortest Path (part1: 單源最短路徑)](https://www.youtube.com/watch?v=NX2Qf0c75Og)
2. [戴克斯特拉算法](https://bit.ly/2MvNGXl)
3. [代克思托演算法 (Dijkstra's algorithm)](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dijkstra.html)
4. [Cycle in Undirected Graph Graph Algorithm](https://www.youtube.com/watch?v=n_t0a_8H8VY&t=163s)
5. [[101北一資訊集訓] 06_3_1 MST之Kruskal演算法(NEW)](https://www.youtube.com/watch?v=wuU4DDEUu1w&t=542s)
6. [Python 初學第十講 — 排序](https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-f3148ebb33a4)
