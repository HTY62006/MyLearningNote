
# coding: utf-8

# In[2]:


# 設置節點
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# In[3]:


# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# 照順序排 並return新的linked list


# In[4]:


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prev = dummy = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 or l2
        return dummy.next

