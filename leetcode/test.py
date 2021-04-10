# 反转一个单链表。
# 示例:#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # head: ListNode) -> ListNode:
    def printroot(self, head):
        if head == None:
            return 0
        print(head.val)
        if head.left != None:
            self.printroot(head.left)
        if head.right != None:
            self.printroot(head.right)
    def printleft(self, head):
        if head == None:
            return 0
        if head.left != None:
            self.printleft(head.left)
        print(head.val)
        if head.right != None:
            self.printleft(head.right)
    def printright(self, head):
        if head == None:
            return 0
        if head.left != None:
            self.printleft(head.left)
        if head.right != None:
            self.printleft(head.right)
        print(head.val)



if __name__ == '__main__':
    n1 = ListNode(1)
    n1.left = ListNode(2)
    n1.right = ListNode(6)
    n1.right.left = ListNode(7)
    n1.right.left.right = ListNode(8)
    n1.right.right = ListNode(9)
    n1.left.left = ListNode(3)
    n1.left.right = ListNode(4)
    s = Solution().printroot(n1)
    print("====--------")
    s1 = Solution().printleft(n1)
