# Week7
## Linked List
### Array的缺點
* 大小是固定的。
* 無法插入新的元素在array中間，或是無法插入新的元素在array最後。
* 可能會浪費內存（超過實際需求）。
### Linked List說明
![image](https://images.plurk.com/7A0bZlodULj9GOH0FSOyxf.png)
> 圖片源自CS50該單元的[簡報](http://cdn.cs50.net/2013/fall/lectures/7/w/week7w.pdf)

![image](https://images.plurk.com/6jFMSdLOdeJ04ELQKYJZpH.jpg)
* 是Linear List(線性表)，但不會依照其順序在記憶體中儲存。
* 有兩個區域，一個是儲存值的地方(val)，一個是指向下一個節點(next)，最後會指向None。
#### 優點
* 是分散的，可以存在記憶體中不同的位子，不需要連續的內存。
* 不必像Array一樣需要預先知道資料大小。
#### 功能
1. 新增
2. 刪除
3. 搜尋
4. 走訪
## 參考資料
1. [Week7w](https://www.youtube.com/watch?v=RUAsmwYC2mc)
2. [CS50_Week7_Wed.](http://cdn.cs50.net/2013/fall/lectures/7/w/week7w.pdf)
