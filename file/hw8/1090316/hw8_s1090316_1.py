class Solution:
    def homework_8(self,N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
        # depth first search + backtracking
        res, q = [], [-1] * N   # cnt 用計數，q用於已經放的位置，例如q[2]=3 表示第3行的放到了第4個位置

        def dfs(k, N):
            if k == N:
                tmp = []
                for i in range(N):  # 輸出一个結果
                    s = ''
                    for j in range(N):
                        s += 'Q' if q[i] == j else '-'
                    tmp.append(s)
                res.append(tmp)
            else:
                for j in range(N):  # 一行一行的进行深度搜索
                    if self.place(k, j, q):
                        q[k] = j
                        dfs(k+1, N)
        dfs(0, N)
        return res

    def place(self, k, j, q):  # 判斷該位置是否可以放一个棋子
        for i in range(k):
            if q[i] == j or abs(q[i]-j) == abs(i-k):  # 不同列，不同斜線
                return 0
        return 1


if __name__ == '__main__':
    solu = Solution()
    N=4
    print(solu.homework_8(N))
    # [["Q"]]
    