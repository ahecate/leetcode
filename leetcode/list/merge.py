#
class Solution:
    def merge(self, A, m, B, n):
        # write code here
        c = []
        i, j = 0,0
        while i < m and j < n:
            if A[i] < B[j]:
                c.append(A[i])
                i += 1
            else:
                c.append(B[j])
                j += 1
        if j == n:
            c.extend(A[i:m])
        if i == m:
            c.extend(B[j:n])
        A[:] = c
        return A


if __name__ == '__main__':
    a = [1, 2]
    b = [1, 5, 7]
    s = Solution().merge(a, len(a), b, len(b))
    print(s)
