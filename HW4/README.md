# Hash Table
## 目錄
* Hash Table和Hash Function原理
* 流程圖
1. add
![image](https://images.plurk.com/65IY93Bgwzv6AAXKyQdisK.png)
2. remove
3. contains
* 學習歷程
* 參考資料總整理
## Hash Table和Hash Function原理
### Hash Table
根據Key來存放雜湊值，稱為Hash Table。
1. 希望將存放資料的Table大小降至`真正會存放到Table的資料數量`。（= `有用到的key的數量`）
2. 需使用Hash Function，將key對應到符合Table大小的範圍（= index）。
3. 可能發生Collision（碰撞），也就是兩筆資料存到Table裡同一個位子。
   1. 用`Linked List`將同一個位子的資料串起來。
   2. 使用Probing Method來尋找Table中空的位子存放資料。
> 參考資料：[Hash Table：Intro(簡介)](http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html)
### Hash Function
1. 將不同長度的訊息輸入，算成`固定長度`的雜湊值。
2. 輸入相同的訊息會出來相同的雜湊值。
3. 計算出來的雜湊值`無法反推`。
4. 雜湊值必須隨`輸入的訊息改變而改變`。
5. 雖然機率很低，但輸入完全不同的訊息有可能產生一樣的雜湊值，此時稱為Hash Collision。→使用Linked List將資料串起來。
> 參考資料：[[資料結構] 雜湊 (Hash)](https://ithelp.ithome.com.tw/articles/10208884)、演算法圖鑑p.128~p.131
## 流程圖
## 學習歷程
1. add
先將key以MD5加密，存取的busket的位子判定以輸入的capacity來決定，先將其轉為capcity值的進位
```Python
def add(self, key):
    # 要用MD5加密儲存資料
    h = MD5.new()
    h.update(key.encode("utf-8"))
    bucket = int(h.hexdigest() , self.capacity)%self.capacity
    if self.data[bucket] == None:
        self.data[bucket] = ListNode(h)
    else:
        new = ListNode(h)
        now = self.data[bucket]
        prev = now
        while now.next != None:
            prev = now
            now = now.next
        prev.next = new
```
2. remove
3. contains

## 參考資料總整理：
* [Hash Table：Intro(簡介)](http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html)
* [[資料結構] 雜湊 (Hash)](https://ithelp.ithome.com.tw/articles/10208884)
* 演算法圖鑑p.128~p.131
