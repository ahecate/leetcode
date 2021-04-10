# 剑指 Offer 06. 从尾到头打印链表
# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
# 示例 1：
# 输入：head = [1,3,2]
# 输出：[2,3,1]
# 限制： 0 <= 链表长度 <= 10000
#
# 链接：https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/5dt66m/
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head):
        # ans = []
        # while head:
        #     ans.append(head.val)
        #     head = head.next
        # # return [ans[i] for i in range(len(ans) - 1, -1, -1)]
        # return ans[::-1]
        a = self.reversePrint(head.next) + [head.val] if head else []
        print(a)
        return a


if __name__ == '__main__':
    h = ListNode(1)
    h.next = ListNode(13)
    h.next.next = ListNode(3)
    h.next.next.next = ListNode(2)

    s = Solution().reversePrint(h)
    print(s)

