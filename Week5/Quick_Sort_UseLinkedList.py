# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):        
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        tail = self.getTail(head)
        head, tail = self.QuickSort(head, tail) # 進行quick sort，得到排序好的linked list新的head與tail
        tail.next = None # Linked list結束
        return head
    
    # Quick Sort
    def QuickSort(self, head, tail):
        # 若head=tail，代表已比對完畢，只剩下一個，若head≠tail，則對尚未分完的部分繼續進行quick sort
        if head != tail:
            # 將linked list由partition()進行分類並回傳值
            head_l, tail_l, head_piv, tail_piv, head_r, tail_r = self.partition(head, tail)
            if head_l == None: # 若left為空
                head = head_piv 
            else:
                head_l, tail_l = self.QuickSort(head_l, tail_l)
                head = head_l
                tail_l.next = head_piv
            if head_r == None: # 若right為空
                tail = tail_piv 
            else:
                head_r, tail_r = self.QuickSort(head_r, tail_r)
                tail_piv.next = head_r
                tail = tail_r
        return head, tail
    
    # 與基準點比較，分成left與right
    def partition(self, head, tail):
        pivot = tail #基準點設為tail
        head_piv = pivot
        tail_piv = pivot
        head_l, tail_l, head_r, tail_r = None, None, None, None
        
        s = ListNode(None) # 使用s來簡化code
        s.next = head
        node = s
        while node.next != tail:
            node = node.next
            if node.val > pivot.val: # > pivot，放入right
                if head_r != None:
                    tail_r.next = node
                    tail_r = node
                else: # right為空
                    head_r = node
                    tail_r = node
            elif node.val < pivot.val: # > pivot，放入right
                if head_l != None:
                    tail_l.next = node
                    tail_l = node
                else: # left為空
                    head_l = node
                    tail_l = node
            else: # 節點放入pivot
                tail_piv.next = node
                tail_piv = node
        return head_l, tail_l, head_piv, tail_piv, head_r, tail_r
    
    # 取得linked list的最後一位
    def getTail(self, node):
        while node.next:
            node = node.next
        return node
