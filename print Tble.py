class Solution:

    def getTable(self, N):
        l1 = []
        for i in range(1, 11):
            l1.append(N*i)
        return l1


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.getTable(N)
        for i in ans:
            print(i, end=" ")
        print()
