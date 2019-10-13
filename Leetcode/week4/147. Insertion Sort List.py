# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        out = head # 默認原先第一位為已排序之資料
        head = head.next
        t = out
        while head != None:
            test = head # 測試值
            head = head.next
            if test.val <= out.val:
                test.next = out
                out = test
            elif test.val >= t.val:
                t.next = test
                t = test
            else:
                n = out
                while n.next != t and n.next.val < test.val:
                    n = n.next
                test.next = n.next
                n.next = test
        t.next = None
        return out
