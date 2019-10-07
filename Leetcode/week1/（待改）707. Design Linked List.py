# https://images.plurk.com/69HQxEAr5YNQFsg0XH0AbI.png
# get有錯，待改。

class ListNode(object):
    def __init__(self, data):
        self.val = data
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None # Linked list為空
        self.len = 0 # 長度為0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.len or index<0:
            return -1
        else:
            # 新增節點n = self.head
            n=self.head
            for a in range(index):
                n=n.next
            return n.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newhead = ListNode(val)
        newhead.next = self.head
        self.head = newhead
        self.len+=1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newtail = ListNode(val)
        if self.len==0:
            self.head = newtail
        else:
            old=self.head
            for i in range(self.len):
                if old.next==None:
                    break
                else:
                    old=old.next
            old.next = newtail
        self.len+=1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # 在index個節點插入→index <= length
        if index > self.len:
            return -1
        elif index == 0:
            addAtHead(val)
        else:
            newNode = ListNode(val)
            A = self.head
            while index >= 1:
                A = A.next
                index-=1
            newNode.next = A.next
            A.next = newNode
            self.len+=1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.len:
            return -1
        elif self.len==1:
            self.head=None
            self.len=0
        elif index==0:
            value = self.head
            self.head = value.next
            self.len-=1
        else:
            A = self.head
            for i in range(index):
                if i==(index-1):
                    deli = A.next 
                    A.next = deli.next
                else:
                    A = A.next 
            self.len-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
