def homework_8(N): 
        
    ans = []    #要回傳的list
    ans_2 = []   #在這個list操作
    if N == 0:
        return ans_2
    def to_sort(row , column, left_shift, right_shift, n, queen):
        if row>=n:  #若全部做完，便將答案傳入最終的list
            ans.append(ans_2[:])
            return
        for i in range(n):
            
            if (i not in column) and (row+i not in left_shift) and (row - i not in right_shift) :  #一列一列將Q填入位置
                roww = ""  #先建立空字串
                for j in range(n):  #j表示每一列的位置，從0跑到n
                    if j == i: roww += "Q"   #若j這個位置符合上面條件，填入Q
                    else: roww += "-"
                ans_2.append(roww)
                
                
                to_sort(row+1, column+[i], left_shift + [row+i], right_shift + [row-i], n, queen)  
                ans_2.pop()  #做完一列就清空
                
                   





    to_sort(0, [], [], [], N, [])
    return ans

       

if __name__ == '__main__':
    N = 4
    print(homework_8(N))
    
    