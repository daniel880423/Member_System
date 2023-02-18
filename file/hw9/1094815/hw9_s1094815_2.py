def homework_9(items, bag_size):
    # 此題使用了四種方法實現，若實際執行的話同時只能執行一個區塊，請把其他三個區塊註解起來


    # ========================== BFS ==========================
    # 時間複雜度：O(n!)   空間複雜度：O(n!)
    # 實際執行所有測試資料 100 次花費時間：20.7 sec

    dup = set() # 為了過濾掉重複物品所設定的集合
    Max = 0 # 初始化獲取總價值最大值
    q = [] # 初始化佇列

    # 開始過濾重複物品(價格與重量皆相同)
    # 在實際偷取物品的過程中，若多個物品完全相同，我們確實可以全部偷取
    # 但是在BFS過程中，假設有 AB 兩個完全相同的物品，我們偷取 A 與偷取 B 延伸出的可能性是完全相同的
    # 故在此處旨在提升演算法的效率，不做也可以，但遇到最差情況時，運算效率會大幅降低
    for i, e in enumerate(items):
        if (tup_e := tuple(e)) not in dup and e[0] <= bag_size:
            q.append((e[0], e[1], {i}))
            dup.add(tup_e)
    # 此時佇列中包含所有物品(沒有重複)
    while q:
        cur_cob = list() # 儲存偷取物品組合，每輪更新一次
        for _ in range(len(q)): # 將 BFS 做分層，此處的做法為典型的 BFS 分層方式
            size, price, visit = q.pop(0) # 將物品取出來
            Max = max(Max, price) # 更新最大值
            for i, item in enumerate(items):
                size_ = size + item[0]
                price_ = price + item[1]
                visit_ = visit | {i}
                if i not in visit and visit_ not in cur_cob and size_ <= bag_size: # 可偷取條件
                    q.append((size_, price_, visit_)) # 若可偷取就將新參數加入佇列中
                    cur_cob.append(visit_) # 將此偷取組合加入全組合中
    return Max

    # ========================== BFS(bit) ==========================
    # 時間複雜度：O(n!)   空間複雜度：O(n!)
    # 實際執行所有測試資料 100 次花費時間：3.8 sec

    # 此處大部分與一般 BFS 方法相同
    # 主要是在儲存所有偷取物品組合的資料結構改為使用 bit 整數最為表示
    # 所有偷取物品組合原本是使用 list(set()) 的方式進行儲存，現在改為 set(int()) 的形式
    # 搜索重複組合的時間複雜度由 O(n) 提升至 O(1)
    # 空間複雜度也從 2 維的 set，降低至一維的 int
    # 故判定重複組合的速度大幅提升

    # bit 優化實際資料結構差異：若總共有 5 種物品，index 分別為 0 1 2 3 4
    # 假設以偷取物品為 1 3 4，使用集合的表示法為 {1, 3, 4}
    # 使用 bit 的表示法為 11010 (= 28)，僅使用一個整數就可以代表以偷取的所有物品
    # 從位置 0 開始從右到左觀看，0 代表未偷取，1 代表以偷取

    dup = set()
    Max = 0
    q = []
    visit_cob = set() # 儲存所有組合的集合
    for i, e in enumerate(items):
        if (tup_e := tuple(e)) not in dup and e[0] <= bag_size:
            q.append((e[0], e[1], 1<<i))
            dup.add(tup_e)
            visit_cob.add(1<<i) # 將物品轉為 bit 表示法並加入所有組合的集合中
    while q:
        size, price, visit = q.pop(0)
        Max = max(Max, price)
        for i, item in enumerate(items):
            size_ = size + item[0]
            price_ = price + item[1]
            visit_ = visit | (1<<i)
            # 以下三者同時成立才可將新參數加入佇列中
            # 1.若此物品與目前偷取物品之交集為 0，代表還沒被偷取過
            # 2.若將此物品加入偷取組合中後，沒有存在於所有偷取組合中
            # 3.若偷取後的 size 小於等於 bag_size
            if visit & (1<<i) == 0 and visit_ not in visit_cob and size_ <= bag_size:
                visit_cob.add(visit_) # 將此偷取組合加入所有偷取組合中
                q.append((size_, price_, visit_))
    return Max

    # ========================== DFS ==========================
    # 時間複雜度：O(n!)   空間複雜度：O(n!)
    # 實際執行所有測試資料 100 次花費時間：3.0 sec

    # 此方法使用了 Recursion with Memoization 的方式優化複雜度極高的演算法
    # 我們對於 dp[(size, price)] 的定義為「在背包總使用空間為 size 且 當前偷取物品總價值為 price 時，繼續偷取物品能獲得的最大利潤」
    # 使用 dp 去儲存當前的 (size, price) pair，如果此組合已出現過，代表在 dp 已經存取這個組合所能偷取的最大利潤了
    # 那我們就直接調用計算過的結果，不需要再進行搜尋，因為再搜下去也只是會得到與 dp[(size, price)] 相同的結果
    # 故此方法屬於一種 bottom-up 遞迴中時常使用的剪枝技巧，能讓 O(n!) 時間複雜度的演算法效率大幅提升

    from collections import defaultdict
    def dfs(size, price, visited):
        if (size, price) in dp: return dp[(size, price)] # 若此組合已存在在 dp 中，那我們就直接調用並回傳，不繼續進行重複的搜尋
        Max = price # 將目前偷取的物品總價值儲存起來
        for i, item in enumerate(items):
            s, p = item
            # 若符合條件就進行偷取，此處一樣使用到 BFS(bit) 中使用的 bit 來目前已偷取的物品
            if size+s <= bag_size and (1<<i) & visited == 0: 
                # 對於每種可以偷取的物品，去計算所有可能性能獲得的最大值
                Max = max(Max, dfs(size + s, price + p, (1<<i) | visited))
        # 將此最大值賦值給 dp[(size, price)]
        dp[(size, price)] = Max
        return Max
    dp = defaultdict(int)
    return dfs(0, 0, 0) # 遞迴從 size = 0, price = 0, visited = 0 開始，visited = 0代表還未偷取任何物品

    # ========================== DP ==========================
    # 時間複雜度：O(n*m)   空間複雜度：O(n*m)
    # 實際執行所有測試資料 100 次花費時間：0.4 sec

    # 此 Dynamic Programming 解法為此題的最佳解，不用重複的搜尋
    # 時間複雜度與空間複雜度皆為 O(bag_size * len(items))

    from collections import defaultdict
    n = len(items)
    dp = defaultdict(int)
    for i in range(n):
        size, price = items[i]
        for curSize in range(1, bag_size+1):
            if curSize < size: # 若當前設定的背包空間小於此物品的大小
                dp[i, curSize] = dp[(i-1, curSize)] # 則直接將上層的結果複製下來
            else: # 若反之
                # 則將偷取此物品後的價值，與上層不偷取此物品的結果，兩者做比較取最大值
                dp[i, curSize] = max(dp[i-1, curSize], price + dp[i-1, curSize-size])

    return dp[n-1, bag_size] # 運算完畢後，整個 table 的右下角即為我們可以取得的最大價值