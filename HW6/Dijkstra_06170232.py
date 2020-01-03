from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w])#u:src, v:dest, w:weight
    def Dijkstra(self, s): 
        self.change_to_inf()#避免搞亂，先將沒法連到的點標成無限
        inf = float("inf")
        check = [False]*self.V#確認走過沒
        d = [inf]*self.V#final list
        d[s] = 0#起點
        check[s] = True#已確認
        for i in range(self.V):#第一步&可連接點加入
            if self.graph[s][i] != inf:#原本是0，因為graph中0=無法到達=inf，後來為了不要搞混，先轉inf
                d[i] = self.graph[s][i]
        for i in range(self.V):#共有幾步
            short_index,short = self.shortest(check,d)#該點的index&最短路徑
            if short_index != -1:#是的話代表找不到下一個點
                check[short_index] = True#先標記成確認加入
                for k in range(self.V):
                    if check[k] == False:#只看還沒標記確認的
                        if d[short_index]+self.graph[short_index][k]<d[k]:#確認加上去的結果是否小於原先該位的值
                            d[k] = d[short_index]+self.graph[short_index][k]#是的話，替換
        final = self.shortpath_dict(d)#回傳結果
        return final                
        
    def change_to_inf(self):#先將無法到達的點標成無限
        for i in range(self.V):
            for j in range(self.V):
                if i!=j and self.graph[i][j]==0:#i=j時表該行起點
                    self.graph[i][j] = float("inf")
    
    def shortest(self,check,d):
        short_index = -1#如果是-1表不存在
        short = False#short還沒出現(最短路徑)
        for j in range(self.V):#走訪每一層的每一個點
            if check[j] == False and d[j] != float("inf"):
                if short == False:#short不存在
                    short_index = j
                    short = d[j]
                else:
                    if d[j] < short:
                        short_index = j
                        short = d[j]
        return short_index,short
    
    def shortpath_dict(self, d):
        final = {}#回傳結果
        for i in range(self.V):
            final[str(i)]=d[i]
        return final
    
    def Kruskal(self):
        self.sort_by_weight()#先將graph按權重排序
        parent = [-1]*self.V#確認是否是同一個set
        a = self.graph.copy()#稍後移除用，因為用for，所以用複製的避免影響到for
        for i in self.graph:
            src=i[0]
            dest=i[1]
            if parent[src]==-1 and parent[dest]==-1:#第一步
                parent[src]=src
                parent[dest]=src
            elif parent[src]==-1 and parent[dest]!=-1:
                parent = self.replace(parent,src,dest)
                parent[src]=src
                parent[dest]=src
            elif parent[src]!=-1 and parent[dest]==-1:
                parent = self.replace(parent,src,dest)
                parent[src]=src
                parent[dest]=src
            elif parent[src]!=parent[dest]:#不同且不是-1的話，仍可進行
                if parent[src]!=-1 and parent[dest]!=-1:
                    parent = self.replace(parent,src,dest)
                    parent[src]=src
            else:#parent[src]==parent[dest]，且不是-1
                a.remove(i)#因為會形成cycle，不能加入，所以要移除
        final = self.mst_dict(a)#回傳結果
        return final
        
    def mst_dict(self,a):
        final = {}
        for i in a:
            final[str(i[0])+'-'+str(i[1])]=i[2]
        return final
    def replace(self,parent,src,dest):
        if parent[src]==-1 and parent[dest]!=-1:
            x = parent[dest]
            for i in range(self.V):
                if parent[i]== x:
                    parent[i]=src
        elif parent[src]!=-1 and parent[dest]==-1:
            x = parent[src]
            for i in range(self.V):
                if parent[i]==parent[x]:
                    parent[i]=src
        elif parent[src]!=parent[dest]:
            if parent[src]!=-1 and parent[dest]!=-1:
                x = parent[src]
                y = parent[dest]
                for i in range(self.V):
                    if parent[i]== x:
                        parent[i]=src
                    if parent[i]== y:
                        parent[i]=src     
        return parent
    
    def sort_by_weight(self):
        a = self.graph
        self.graph = sorted(a,key=lambda a:a[2])

## 參考資料總整理
#1. [[101北一資訊集訓] 07_1 最短路徑Shortest Path (part1: 單源最短路徑)](https://www.youtube.com/watch?v=NX2Qf0c75Og)
#2. [戴克斯特拉算法](https://bit.ly/2MvNGXl)
#3. [代克思托演算法 (Dijkstra's algorithm)](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dijkstra.html)
#4. [Cycle in Undirected Graph Graph Algorithm](https://www.youtube.com/watch?v=n_t0a_8H8VY&t=163s)
#5. [[101北一資訊集訓] 06_3_1 MST之Kruskal演算法(NEW)](https://www.youtube.com/watch?v=wuU4DDEUu1w&t=542s)
#6. [Python 初學第十講 — 排序](https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-f3148ebb33a4)
