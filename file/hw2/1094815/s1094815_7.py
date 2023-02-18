def homework_2(lst):
    total = 0 # 計算總共的step數
    pre = 0   # 儲存上一個值(因lst內值的範圍為1~10000，故可初始化為0)
    for cur in lst: 
        # cur：lst內當前目標的值   pre：上一個值   step：此次迴圈需要增加的step數
        # if   -> 若 pre >= cur，則 step = 兩數的正差 + 2
        # else -> 若 pre < cur，則只需判斷cur的奇偶，若奇則 step = 1，若偶則 step = 0
        step = pre - cur + 2 if pre >= cur else cur%2
        total += step    # 儲存此次的 step 數
        pre = cur + step # 將 pre 改為 cur 更新後的值
    return total