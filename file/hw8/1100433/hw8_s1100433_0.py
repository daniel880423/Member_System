def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    q = []                                                                         #建立list q用來擺放答案
    for i in queens(N):                                                            #將function queens運算出的結果取出進行視覺化
        q.append(viz(i))                                                           #放入list q
    return q
def conflict(state, nextX):                                                        #定義function conflict用來判斷與現存皇后衝突的位置(意即為promising)，參數為tuple及下個位置
    nextY = len(state)                                                             #依列判斷
    con = any(abs(state[i] - nextX) in (0, nextY - i) for i in range(nextY))       #判斷是否同列或同對角線(nextY - i:x座標絕對值之差 = y座標絕對值之差)
    return con                                                                     #回傳布林值

def queens(n, state=()):                                                           #建立遞迴function queens，參數為需要的皇后數與tuple用來記錄已擺放的皇后
    if len(state) == n and len(state) != 0:                                        #如果每行都有可行皇后
        return [()]                                                                #回傳tuple
    ans = []
    for pos in range(n):                                                           #依照Backtrackin依層判斷
        if not conflict(state, pos):                                               #如果此解可行
            ans += [(pos,)+ result for result in queens(n, state + (pos,))]        #Ex:queens(4,(0,))之解，即為queens(4,(0,2))及queens(4,(0,3))的所有可行解拼湊
    return ans

def viz(state):                                                                    #建立function viz用來視覺化queens所生成之tuple
    vis=['-'*len(state)] * len(state)
    for i ,item in enumerate(state):
        vis[i]=vis[i][:item]+"Q"+vis[i][item+1:]                                   #Q之前加上'-'+ Q + 補上'-'
    return vis

if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    # [["Q"]]
    