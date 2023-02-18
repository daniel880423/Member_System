def homework_8(N):  # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    if N == 0:
        return []
    def visualize(state):
        vis = ["-" * len(state)] * len(state)
        for i, item in enumerate(state):
            vis[i] = vis[i][:item] + "Q" + vis[i][item + 1:]
        return vis

    def conflict(state, nextX):
        nextY = len(state)
        if any(abs(state[i] - nextX) == 0 for i in range(len(state))):  # 判斷是否同行
            return True
        if any(abs(state[i] - nextX) == nextY - i for i in range(len(state))):  # 判斷是否同對角線 若兩組(x,y)座標在同一條對角線 x座標絕對值之差 = y座標絕對值之差
            return True
        return False  # 不在上個皇后的攻擊範圍

    def queens(n, state=()):
        if len(state) == n:  # 若n個皇后放好則回傳
            # print(visualize(state))  # 印出答案
            ABC.append(visualize(state))
        ans = []  # 記錄在state棋子已經放好的狀況下後續的所有解答
        for pos in range(n):  # 在下一列中放新的皇后
            if not conflict(state, pos):  # 若不在皇后的攻擊範圍
                ans += [(pos,) + result for result in queens(n, state + (pos,))]  # 添加進ans
        return ans
    ABC = []
    queens(N)
    return ABC

if __name__ == '__main__':
    N = 0
    print(homework_8(N))
    # [["Q"]]