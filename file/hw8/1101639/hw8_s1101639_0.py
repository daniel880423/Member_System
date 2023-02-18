def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    if N == 0:return []
    a = []                                                                         #建立list a放答案
    for i in que(N):                                                               #將function que運算出的結果取出進行視覺化
        a.append(transferr(i))                                                     #放入list a
    return a


def que(n, state=()):                                                              #參數代表所需之皇后數與用來記錄已擺放的皇后
    if len(state) == n:                                                            #如果每行都有皇后
        return [()]                                                                #回傳tuple
    ans = []
    for pos in range(n):                                                           #Backtracking依層判斷
        if not quarrel(state, pos):                                                #如果此解可行
            ans += [(pos,)+ result for result in que(n, state + (pos,))]           #Ex:queens(4,(0,))之解，即為que(4,(0,2))及que(4,(0,2))的所有可行解組合
    return ans

def transferr(output):                                                             #建立function transferrr用來視覺化que所生成之tuple
    vis=['-'*len(output)] * len(output)
    for i ,item in enumerate(output):
        vis[i]=vis[i][:item]+"Q"+vis[i][item+1:]                                   #Q之前加上'-'+ Q + 補上'-'
    return vis

def quarrel(s, nextX):                                                         #定義function quarrel判斷與現存皇后衝突的位置
    nextY = len(s)                                                             #依列判斷
    con = any(abs(s[i] - nextX) in (0, nextY - i) for i in range(nextY))       #判斷是否同列或同對角線
    return con                                                                 #回傳布林值




if __name__ == '__main__':
    N = 1
    print(homework_8(N))
    # [["Q"]]
    