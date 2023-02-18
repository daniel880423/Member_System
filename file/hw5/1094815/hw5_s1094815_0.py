def homework_5(matrix, start, end, total):
    if start == end: # 若起點等於終點則直接 return [-1, None] 
        return [-1, None]
    # 製作 A 和 path (size = total*total)
    # 將 A 內值除了 i==j 的座標值為 0 (自己到自己的路徑長)，其餘全部初始化為 inf
    A = [[float("inf") if i!=j else 0 for j in range(total)] for i in range(total)]
    # 將 path 內值全部初始化為 -1
    path = [[-1 for j in range(total)] for i in range(total)]

    # 將 matrix 內的資料填入 A 距離矩陣
    for l1, l2, length in matrix:
        A[l1-1][l2-1] = length # 減 1 是因為 matrix 內座標從為 1-indexed，但 Python 中為 0-indexed
        
    # 查看有無其他更短路徑，trans 為中轉點
    for trans in range(total):
        for i in range(total):
            for j in range(total):
                new_path = A[i][trans] + A[trans][j]
                if A[i][j] > new_path:
                    A[i][j] = new_path
                    path[i][j] = trans
    
    # 取得最短路徑
    ans_len = A[start-1][end-1]
    if ans_len == float("inf"): # 若無法從 start 抵達 end 則 return [-1, None]
        return [-1, None]

    # 儲存最短路徑遞迴 v1為起點(int)，v2為終點(int)，p為路徑(str)
    def getPath(v1, v2, p, top = False):
        if top: # 若為第一層遞迴，則將起點加入路徑字串首
            p += str(start)
        if path[v1][v2] != -1: # 若不為 -1 則代表還有其他中轉點
            # 假設起點為 α，終點為 β，他們的中轉點 A[α][β] 為 θ
            p = getPath(v1, path[v1][v2], p) # 查看 α -> θ 有無其他中轉點
            p += str(path[v1][v2]+1)         # 將此中轉點填入，加 1 是將 12 行減的 1 加回來，才等於題目要求的點值
            p = getPath(path[v1][v2], v2, p) # 查看 θ -> β 有無其他中轉點
        if top: # 若為第一層遞迴，則將終點加入路徑字串尾
            p += str(end)
        return p # 若該點為 -1 則代表無其他中轉點，回傳傳入的 p

    return [ans_len, getPath(start-1, end-1, "", True)]