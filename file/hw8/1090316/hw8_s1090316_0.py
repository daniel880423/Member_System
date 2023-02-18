class Solution:
    def homework_8(self,n): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
        # depth first search + backtracking
        res, q = [], [-1] * n   # cnt 用計數，q用於已經放的位置，例如q[2]=3 表示第3行的放到了第4個位置

        def dfs(k, n):
            if k == n:
                tmp = []
                for i in range(n):  # 輸出一个結果
                    s = ''
                    for j in range(n):
                        s += 'Q' if q[i] == j else '-'
                    tmp.append(s)
                res.append(tmp)
            else:
                for j in range(n):  # 一行一行的进行深度搜索
                    if self.place(k, j, q):
                        q[k] = j
                        dfs(k+1, n)
        dfs(0, n)
        return res

    def place(self, k, j, q):  # 判斷該位置是否可以放一个棋子
        for i in range(k):
            if q[i] == j or abs(q[i]-j) == abs(i-k):  # 不同列，不同斜線
                return 0
        return 1


if __name__ == '__main__':
    solu = Solution()
    n=4
    print(solu.homework_8(n))
    # [["Q"]]
    