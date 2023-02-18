def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    wt = []
    val = []
    n = len(items)
    for i in range(n):
        wt.append(items[i][0])
        val.append(items[i][1])
    table = [[0 for x in range(bag_size + 1)] for x in range(n + 1)] 
 
    for i in range(n + 1): 
        for j in range(bag_size + 1): 
            if i == 0 or j == 0: 
                table[i][j] = 0
            elif wt[i-1] <= j: 
                table[i][j] = max(val[i-1]  + table[i-1][j-wt[i-1]],  table[i-1][j]) 
            else: 
                table[i][j] = table[i-1][j] 
   
    return table[n][bag_size]


    