from collections import defaultdict 
class Graph:
    def __init__(self):  
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
 
    def BFS(self, s): 
        state1=[0]*len(self.graph)#設定一個list表該點尚未造訪過(尚未造訪=0，已造訪=1)
        state2=[]#final
        state2.append(s)
        y = 0
        while len(state2) <= len(state1) and y < len(state1):
            x = state2[y]#queue是先進先出
            if state1[x] != 1:#如果還沒被標記成造訪過
                state1[x] = 1#標記造訪過
                for i in self.graph[x]:
                    if state1[i] != 1 and state2.count(i) == 0:#排除已加入，但尚未標造訪過的點
                        state2.append(i)#還沒造訪過就加入state2
            y+=1
        return state2
    
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
        state=[0]*len(self.graph)#設定一個list表該點尚未造訪過(尚未造訪=0，已造訪=1)
        state1=[s]#check
        state2=[]#final
        while len(state2) < len(state):
            x = state1.pop()#stack是後進先出，pop會回傳刪除的值並刪除
            if state[x] != 1:#如果還沒被標記成造訪過
                state[x] = 1#標記造訪過
                state2.append(x)#造訪後加入
                for i in self.graph[x]:
                    if state[i] != 1 and state2.count(i) == 0:#排除已加入，但尚未標造訪過的點
                        state1.append(i)#還沒造訪過就加入state1
        return state2

# 1. [上課簡報](https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.g7a5d8b85ee_0_23)
# 2. 演算法圖鑑p.96~p.99
# 3. [The Depth First Search Graph traversal algorithm](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/11-Graph/dfs.html)
# 4. [The Breadth First Search Graph traversal algorithm](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/11-Graph/bfs.html)
# 5. [Difference Between BFS and DFS(techdifferences)](https://techdifferences.com/difference-between-bfs-and-dfs.html)
# 6. [Difference Between BFS and DFS(geeksforgeeks)](https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/)
