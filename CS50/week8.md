# Week8
## Content
* [Stack](https://github.com/HTY62006/MyLearningNote/blob/master/CS50/week8.md#stack)
* [Queue](https://github.com/HTY62006/MyLearningNote/blob/master/CS50/week8.md#queue)
* [Tree](https://github.com/HTY62006/MyLearningNote/blob/master/CS50/week8.md#tree)
* [BST](https://github.com/HTY62006/MyLearningNote/blob/master/CS50/week8.md#binary-search-treebst)
## Stack
### 觀念
後進先出，常用功能有：插入(push)、移除(pop)、回傳最上方資料(top)、確認資料個數(getSize)和確認是否有資料(isEmpty)。
> 此圖為例，插入4後，pop()將4刪除，top()找到3。此時剩三個資料，使用getSize會得到3。

![image](https://images.plurk.com/2bfn1ELXyi6beRjzN3pLf8.jpg)
### 會使用在哪？
* 回上一頁（瀏覽器）
* 編輯器的undo
## Queue
### 觀念
先進先出，像排隊一樣。常用功能有：插入(push)、移除(pop)、回傳最前方資料(getFront)、回傳最後方資料(getBack)、確認資料個數(getSize)和確認是否有資料(isEmpty)。
> 此圖為例，插入4後，pop()將1刪除，getFront()找到2，getBack()找到4。此時剩三個資料，使用getSize會得到3。

![image](https://images.plurk.com/4g27n8WiRxTIwC0OatI5hQ.jpg)
### 會使用在哪？
* 電腦的「工作排程」
## Tree
最源頭的節點稱為root(根)，每個節點可以有0~n個節點作為子節點。若該節點的子節點樹為0，則是這顆Tree的葉節點。

Tree的結構如下圖所示。
![image](https://images.plurk.com/21fY5KOfAvkU62UEul35ST.jpg)

## Binary Search Tree(BST)
**特性：**左子節點 < 節點；右子節點 > 節點。

BST的結構如下圖所示。
![image](https://images.plurk.com/5VsLOXYYCHU1lRWw0MiMzj.jpg)

## 參考資料
1. [樹狀結構(Tree)](http://homepage.ntu.edu.tw/~d02922022/AdvC/ppt/Part%202/05%20%E6%A8%B9%E7%8B%80%E7%B5%90%E6%A7%8B(Tree).pdf)
2. [Week8w](https://www.youtube.com/watch?v=9qvt6MwBKZQ)
3. [Week8f](https://www.youtube.com/watch?v=ihmHDZKOkA8)
