def homework_8(N):
    # if N == 0: return list() # 若輸入為 0 則直接 return []
    def dfs(y, x, cols, dia1, dia2, res): # 參數為 row_number, col_number, cols_used, dia1_used, dia2_uesd
        if y == N: # 若已跑到 index = N 的 row, 代表已找到一組解
            ans.append(res) # 將此組解加入答案清單中, 因無須再搜尋故直接 return
            return
        for x in range(N): # 從左到右搜尋當前 row
            if (x not in cols) and (y+x not in dia1) and (y-x not in dia2): # 若此位置不會與其他已放置的皇后衝突
                # 將此皇后的攻擊範圍加入3個集合中, 並更新當前結果 res, 再往 next row 繼續遞迴搜尋
                dfs(y+1, 0, cols|{x}, dia1|{y+x}, dia2|{y-x}, res + ["".join(["-" if i != x else "Q" for i in range(N)])])

    ans = list()
    dfs(0, 0, set(), set(), set(), list())
    return ans

print(homework_8(0))