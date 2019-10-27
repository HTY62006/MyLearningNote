class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        else:
            pivot = head
            head = head.next
            left = None
            right = None
        
        while head != None:
            if head.val < pivot.val:
                if left == None:
                    left = head
                    head = head.next
                    left_first = left
                else:
                    left.next = head
                    left = left.next
                    head = head.next
            elif head.val > pivot.val:
                if right == None:
                    right = head
                    head = head.next
                    right_first = right
                else:
                    right.next = head
                    right = right.next
                    head = head.next
                
        return self.sortList(left_first)+equal+self.sortList(right_first)
    
