# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 示例 1:
# 输入: 123
# 输出: 321
#  示例 2:
# 输入: -123
# 输出: -321
# 示例 3:
# 输入: 120
# 输出: 21
# 注意:
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。
# 请根据这个假设，如果反转后整数溢出那么就返回 0。


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        f = 1
        if x < 0:
            f = -1
            x *= f

        max =2**31
        ans = 0
        if f == 1:
            while x != 0:
                t = x % 10
                ans = ans * 10 + t
                if ans > max - 1:
                    return 0
                x = int(x / 10)

        else:
            while x != 0:
                t = x % 10
                ans = ans * 10 + t
                if ans > max:
                    return 0
                x = int(x / 10)

        ans *= f
        return ans


if __name__ == '__main__':
    solution = Solution()
    # x = 2**31-2
    x=123456000
    ans = solution.reverse(x)

    print(ans)
