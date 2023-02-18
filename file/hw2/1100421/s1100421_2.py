from functools import total_ordering


def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    index=0
    l=len(lst)  #設l為list長度
    total = 0   #設初始總和
    tmp_sum = become_even(lst, index, l, total)     #設一個方法將list裡的數都先變為偶數，回傳值為當前總步數
    ans = judge_big_small(lst, index, l, tmp_sum)   #再比較前後數大小決定要加多少，回傳值為總步數
    return ans

def become_even(lst, index, l, total):
    if index>=l:    #表示list裡的數都已經是偶數，回傳當前總步數
        return total
    tmp = lst[index]    #設當前數為tmp
    tmp_2=tmp//2        #再設tmp_2為當前數整除2為多少
    if 2*tmp_2-tmp != 0 :   #不等於0代表非偶數
        tmp+= 1     #當前數加一變偶數
        total+= 1   #總步數加一
        lst[index] = tmp    #將當前數丟到list裡，改變當前數值
    return become_even(lst, index+1, l, total)  #遞迴並回傳數值
    
def judge_big_small(lst, index, l, tmp_sum):
    tmp=lst[index]      #設當前數為tmp
    index_2 = index+1   #設另一個index值為index_2
    if index_2 >= l:    #判斷是否已經到list尾了，式的話回傳更新的總步數
        return tmp_sum
    tmp_2=lst[index_2]  #設當前數後一位數為tmp_2
    if tmp > tmp_2:     #當tmp_2 > tmp代表tmp_2要加值
        total = tmp-tmp_2 + 2   #加tmp與tmp_2的差值再加二
        tmp_2+= total       #再將要加的總值加到tmp_2
        tmp_sum+= total     #也將加值加到總步數
        lst[index+1] = tmp_2    #最後改變list了的值
    if tmp == tmp_2:    #當tmp等於tmp_2時，只需加二
        tmp_2+= 2
        tmp_sum += 2    #更新總步數
        lst[index+1] = tmp_2    #將list裡的值改變
    return judge_big_small(lst, index+1, l, tmp_sum)    #遞迴並回傳數值

if __name__ == '__main__':
    lst = [1, 1, 1]
    print(homework_2(lst))
    