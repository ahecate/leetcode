# 206. 反转链表
# 反转一个单链表
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
# Definition for singly-linked list.

# 没懂啊啊哈哈哈

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    class Solution:
        def reverseList(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            p, rev = head, None
            while p:
                rev, rev.next, p = p, rev, p.next
            return rev

    def reverseList2(self, head):
        # 递归终止条件是当前为空，或者下一个节点为空
        if (head.next == None):
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList2(head.next)
        # print(cur, type(cur))
        # 这里请配合动画演示理解
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur


if __name__ == '__main__':
    n1 = ListNode(1)
    head = ListNode(0)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = None
    head.next = n1
    ans = Solution()
    l = ans.reverseList2(head)
    print(l.val, l.next.val, l.next.next.val)

# class Node(object):
#     def __init__(self, elem, next_=None):
#         self.elem = elem
#         self.next = next_
#
#
# def reverseList(head):
#     if head == None or head.next == None:  # 若链表为空或者仅一个数就直接返回
#         return head
#     pre = None
#     next = None
#     while (head != None):
#         next = head.next  # 1
#         head.next = pre  # 2
#         pre = head  # 3
#         head = next  # 4
#     return pre
#
# if __name__ == '__main__':
#     l1 = Node(3)  # 建立链表3->2->1->9->None
#     l1.next = Node(2)
#     l1.next.next = Node(1)
#     l1.next.next.next = Node(9)
#     l = reverseList(l1)
#     print(l.elem, l.next.elem, l.next.next.elem, l.next.next.next.elem)
