# 21.
# 合并两个有序链表
# 将两个升序链表合并为一个新的
# 升序
# 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# 示例1：
# 输入：l1 = [1, 2, 4], l2 = [1, 3, 4]
# 输出：[1, 1, 2, 3, 4, 4]
# 示例
# 2：
# 输入：l1 = [], l2 = []
# 输出：[]
# 示例
# 3：
# 输入：l1 = [], l2 = [0]
# 输出：[0]
# 提示：
# 两个链表的节点数目范围是[0, 50]
# -100 <= Node.val <= 100
# l1 和l2均按非递减顺序排列


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # return ListNode
    def mergeTwoLists(self, l1, l2):
        # timeout
        # if l1 is None:
        #     return l2
        # elif l2 is None:
        #     return l1
        # if l1.val > l2.val:
        #     return self.mergeTwoLists(l2, l1)
        # q = l1
        # while q.next != None:
        #     if l2.val >= q.val:
        #         if l2.val >= q.next.val:
        #             q = q.next
        #         else:
        #             if l2.next != None:
        #                 p = l2.next
        #                 l2.next = q.next
        #                 q.next = l2
        #                 return self.mergeTwoLists(l1, p)
        #             else:
        #                 l2.next = q.next
        #                 q.next = l2
        # if q.next == None:
        #     if l2 != None:
        #         q.next = l2
        # return l1

        # 递归
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    # 输入：l1 = [1, 2, 4], l2 = [1, 3, 4]

    n1 = ListNode(1)
    n1.next = ListNode(2)
    n1.next.next = ListNode(4)
    n2 = ListNode(1)
    n2.next = ListNode(3)
    n2.next.next = ListNode(4)
    print(type(n1))
    s = Solution().mergeTwoLists(n1, n2)
    while s!=None:
        print(s.val)
        s=s.next
