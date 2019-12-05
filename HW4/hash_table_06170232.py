from Cryptodome.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        """
        :type capacity: int
        :rtype: None
        """
    def add(self, key):
        """
        :type key: str
        :rtype: None
        """
        # 要用MD5加密儲存資料
        h = MD5.new()
        h.update(key.encode("utf-8"))
        h = h.hexdigest()
        # MD5是16進位，轉成10進位
        bucket = int(h , 16)%self.capacity
        if self.data[bucket] == None:
            self.data[bucket] = ListNode(h)
        else:
            new = ListNode(h)
            now = self.data[bucket]
            while now.next != None:
                now = now.next
            now.next = new

    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
        h = MD5.new()
        h.update(key.encode("utf-8"))
        h = h.hexdigest()
        bucket = int(h , 16)%self.capacity
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
                    self.data[bucket] = None
        # 相同質移除
        if self.contains(key) == True:
            self.remove(key)

    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
        h = MD5.new()
        h.update(key.encode("utf-8"))
        h = h.hexdigest()
        bucket = int(h , 16)%self.capacity
        if self.data[bucket] != None:
            node = self.data[bucket]
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

# 參考資料總整理：
# [Hash Table：Intro(簡介)](http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html)
# [[資料結構] 雜湊 (Hash)](https://ithelp.ithome.com.tw/articles/10208884)
# 演算法圖鑑p.128~p.131
