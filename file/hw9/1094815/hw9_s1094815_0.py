def homework_9(items, bag_size):
    # ========================== DFS ==========================
    # from collections import defaultdict
    # def dfs(size, price, visited):
    #     if (size, price) in dp: return dp[(size, price)]
    #     Max = price
    #     for i, item in enumerate(items):
    #         s, p = item
    #         if size+s <= bag_size and (1<<i) & visited == 0:
    #             Max = max(Max, dfs(size + s, price + p, (1<<i) | visited))
    #     dp[(size, price)] = Max
    #     return Max
    # dp = defaultdict(int)
    # return dfs(0, 0, 0)

    # ========================== BFS(bit) ==========================
    # dup = set()
    # Max = 0
    # q = []
    # visit_cob = set()
    # for i, e in enumerate(items):
    #     if (tup_e := tuple(e)) not in dup and e[0] <= bag_size:
    #         q.append((e[0], e[1], 1<<i))
    #         dup.add(tup_e)
    #         visit_cob.add(1<<i)
    # while q:
    #     size, price, visit = q.pop(0)
    #     Max = max(Max, price)
    #     for i, item in enumerate(items):
    #         size_ = size + item[0]
    #         price_ = price + item[1]
    #         visit_ = visit | (1<<i)
    #         if visit & (1<<i) == 0 and visit_ not in visit_cob and size_ <= bag_size:
    #             visit_cob.add(visit_)
    #             q.append((size_, price_, visit_))
    # return Max

    # ========================== BFS ==========================
    dup = set()
    Max = 0
    q = []
    for i, e in enumerate(items):
        if (tup_e := tuple(e)) not in dup and e[0] <= bag_size:
            q.append((e[0], e[1], {i}))
            dup.add(tup_e)

    while q:
        cur_cob = list()
        for _ in range(len(q)):
            size, price, visit = q.pop(0)
            Max = max(Max, price)
            for i, item in enumerate(items):
                size_ = size + item[0]
                price_ = price + item[1]
                visit_ = visit | {i}
                if i not in visit and visit_ not in cur_cob and size_ <= bag_size:
                    q.append((size_, price_, visit_))
                    cur_cob.append(visit_)
    return Max

    # ========================== DP ==========================
    # from collections import defaultdict
    # n = len(items)
    # dp = defaultdict(int)
    # for i in range(n):
    #     size, price = items[i]
    #     for maxSize in range(1, bag_size+1):
    #         if maxSize < size:
    #             dp[i, maxSize] = dp[(i-1, maxSize)]
    #         else:
    #             dp[i, maxSize] = max(dp[i-1, maxSize], price + dp[i-1, maxSize-size])

    # return dp[n-1, bag_size]



# if __name__ == "__main__":
#     from capital_measurement import hw9_Ans as ANS, hw9_In as IN
#     import time
#     t1 = time.time()
#     for i in range(len(ANS)*100):
#         i %= len(ANS)
#         homework_9(IN[i][0], IN[i][1])
#         print(homework_9(IN[i][0], IN[i][1]) == ANS[i])
#     t2 = time.time() - t1
#     print(t2)
    # DFS       3.0 sec
    # BFS(bit)  3.8 sec
    # BFS      20.7 sec
    # DP        0.4 sec