# 给定两个数组，编写一个函数来计算它们的交集。
# 示例
# 1：
# 输入：nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# 输出：[2]
# 示例
# 2：
# 输入：nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# 输出：[9, 4]
# 说明：
#
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。

# class Solution(object):
#     def intersection(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         ans = []
#         len1 = len(nums1)
#         len2 = len(nums2)
#         if len1 <= len2:
#             for i in nums1:
#                 if i in nums2:
#                     if i not in ans:
#                         ans.append(i)
#         else:
#             for i in nums2:
#                 if i in nums1:
#                     if i not in ans:
#                         ans.append(i)
#         return ans

class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        print(type(set1))
        set2 = set(nums2)
        return self.set_intersection(set1, set2)

    def set_intersection(self, set1, set2):
        if len(set1) > len(set2):
            return self.set_intersection(set2, set1)
        return [x for x in set1 if x in set2]


if __name__ == '__main__':
    s = Solution()
    n1 = [1, 7, 2, 3, 4, 4, 5]
    n2 = [4, 5]
    # print(list(set(n1).intersection(set(n2))))
    print(s.intersection(n1, n2))
