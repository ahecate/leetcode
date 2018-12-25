# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 示例 1:
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
# 所有输入只包含小写字母 a-z 。

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) > 2:
            s1 = strs[0]
            s2 = strs[1]
            ans = ""
            if len(s1)>len(s2) :
                len_id=len(s2)
            else:
                len_id=len(s1)
            for i in range(0, len_id):
                if s1[i] == s2[i]:
                    ans += s1[i]
                else:
                    break
            if ans == "":
                return ans
            else:
                del strs[0]
                del strs[0]
                strs.insert(0, ans)
                return self.longestCommonPrefix(strs)


        elif len(strs) == 2:
            s1 = strs[0]
            s2 = strs[1]
            ans = ""
            if len(s1)>len(s2) :
                len_id=len(s2)
            else:
                len_id=len(s1)
            for i in range(0, len_id):
                if s1[i] == s2[i]:
                    ans += s1[i]
                else:
                    break
            return ans

        elif len(strs) ==1:
            return strs[0]

        else:
            return ""


if __name__ == '__main__':
    strs = ["sdf"]
    solution = Solution()
    print(solution.longestCommonPrefix(strs))
