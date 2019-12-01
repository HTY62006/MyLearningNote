# Hash Table
## 目錄
* Hash Table和Hash Function原理
* 流程圖
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
1. add
![image](https://github.com/HTY62006/MyLearningNote/blob/master/large_image/HT01.png)
2. remove
![image](https://github.com/HTY62006/MyLearningNote/blob/master/large_image/HT02.png)
3. contains
![image](https://github.com/HTY62006/MyLearningNote/blob/master/large_image/HT03.png)
## 學習歷程
1. add
先將key以MD5加密，存取的busket的位子判定以輸入的capacity來決定，先將其轉為16進位，再去除以capacity以得到餘數。（餘數 = bucket）
```Python
def add(self, key):
    # 要用MD5加密儲存資料
    h = MD5.new()
    h.update(key.encode("utf-8"))
    # 16進位
    bucket = int(h.hexdigest() , 16)%self.Acapacity
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
* 判斷要刪除的Key它理論上會被儲存在哪個bucket之後，如果該bucket存在值，開始比較是否在裡面，在的話就移除。沒有的話不必進行任何動作。
* 如果查詢key還查得到的話就再刪除一次。
```Python
def remove(self, key):
    """
    :type key: str
    :rtype: None
    """
    h = MD5.new()
    h.update(key.encode("utf-8"))
    bucket = int(h.hexdigest() , 16)%self.capacity
    del_bucket = self.data[bucket]
    prev = del_bucket
    if del_bucket != None:
        if del_bucket.next != None:
            if del_bucket.val == h:
                self.data[bucket] = del_bucket.next
            else:
                prev = del_bucket
                while del_bucket.next:
                    if del_bucket == h:
                        prev.next = del_bucket.next
                    else:
                        prev = del_bucket
                        del_bucket = del_bucket.next
        else:
            if del_bucket.val == h:
                del_bucket = None
    if self.contains(key) == True:
        self.remove(key)
```
出現問題：沒有刪除成功。檢查後發現是我直接讓del_bucket=None的關係。不能直接讓del_bucket = None，因為del_bucket原本是self.data[bucket]，這樣會直接被覆蓋掉，而self.data還是沒有被改到。
```Python
else:
    if del_bucket.val == h:
        self.data[bucket] = None
```
針對此段作出修改，測試後目前此段無誤。

3. contains
原本的想法：用for迴圈去查每個位子的ˋ值是否有和key一致的，有的話回傳True，沒的話回傳False。
```Python
def contains(self, key):
    """
    :type key: str
    :rtype: bool(True or False)
    """
    h = MD5.new()
    h.update(key.encode("utf-8"))
    for i in self.data:
    # 因為i是Linked list，而Linked lisdt的值又經MD5加密
        if i != None:
            if i.val == h:
                return True
    return False
```
發生問題：有新增成功，但查詢失敗。測試後發現即使我儲存的是一樣的key，但因為我儲存進linked list內的資料沒有轉成h.hexdigest()，因此即使key一樣也不會相等。
```Python
h = MD5.new()
h.update(key.encode("utf-8"))
h = h.hexdigest()
bucket = int(h , 16)%self.capacity
```
重新定義會存入linked list的值(h)。測試時發現有些加入的值使用contains，明明應該找得到的值卻回傳False。
* 假設現在要找cat，且cat在linked list中，走訪時走訪到pig去。(f74c6af46a78becb2f1bd3f95bbd5858)
因為我原本的寫法只會判斷到linked list的第一個節點，因此修改成從該bucket的linked list去比對是否存在。
```Python
h = MD5.new()
h.update(key.encode("utf-8"))
h = h.hexdigest()
bucket = int(h , 16)%self.capacity
if self.data[bucket] != None:
    node = self.data[bucket]
#             if self.data[bucket].next != None:
    while node.next != None:
        node = node.next
        if node.val == h:
            break
#                 print(node.val)
    if node.val == h:
        return True
    else:
        return False
else:
    return False
```
還是False，檢查過後發現是add的環節出問題。在這段之中：
```Python
new = ListNode(h)
now = self.data[bucket]
prev = now
while now.next != None:
    prev = now
    now = now.next
prev.next = new
```
在設置linked list時受到刪除的影響，但其實根本沒必要設prev，因為會造成錯誤：理論上是要變成A→B→C，結果卻變成A→C。
```Python
new = ListNode(h)
now = self.data[bucket]
while now.next != None:
    now = now.next
now.next = new
```
將prev移除後，直接以now來試試看。add在建造linked list時不會出現這個錯誤。進而在運行contains時，原先回傳有誤的情況已解決。

測試結果：
![image](https://images.plurk.com/NJ3eGdU02c2q3jUAVv5qK.png)
## 參考資料總整理：
* [Hash Table：Intro(簡介)](http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html)
* [[資料結構] 雜湊 (Hash)](https://ithelp.ithome.com.tw/articles/10208884)
* 演算法圖鑑p.128~p.131
