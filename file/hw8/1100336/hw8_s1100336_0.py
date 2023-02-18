def homework_8(N): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search + backtracking
    global ans  #設一個全域變數存最後要回傳的值
    ans = []    #把該全域變數設成List
    if N==0:    #如果N=0，直接回傳空List
        return []
    def dfs(row,col,right_slach,left_slash):  #depth first search

        if len(col)==N:  #如果col有存0~N的值了話
            draw(col)  #就傳col的值給draw把N皇后的List依照col[]內的row值


        for i in range(N):  #i是當下的(列)
            if i not in col and row-i not in right_slach and row+i not in left_slash: #如果i沒在col內，且row-i沒在右斜線內，且row+i沒在左斜線內
                col.append(i)             #就把i加入col內(加入col中的值為之後"Q"在row(行)內要放的位置)
                right_slach.append(row-i) #就把row-i加入right_slach內
                left_slash.append(row+i)  #就把row+i加入left_slash內
                dfs(row+1,col,right_slach,left_slash)  #把row+1(也就是row的下一行)，去遞迴
                #如果row的下一行不符合i沒在col內，且row-i沒在右斜線內，且row+i沒在左斜線內，就會再往上一層去跑，直到如果col有存0~N的值了話跑if那
                col.pop()   #把col最後面剛加入的值刪掉
                right_slach.pop()  #把right_slach最後面剛加入的值刪掉
                left_slash.pop()   #把left_slash最後面剛加入的值刪掉

    def draw(col):     #把N皇后的List印出來
        lst=[]         #先設一個lst
        for i in range(len(col)):  #col的長度0~N-1分別代表row的1~N
            x=""                   #先設一個空字串
            for j in range(N):     #j為第幾列
                if j == col[i]:    #如果j=col(row中的第幾個位置有"Q")
                    x+='Q'         #把Q加入該字串
                else:
                    x+='-'         #沒有的話直接加-進去字串
            lst.append(x)          #把值加入lst中
        ans.append(lst)            #把最後的lst加入起初設的全域變數內(全域變數存最後要回傳的值)


    dfs(0, [],[],[])  #傳進去dfs(row的初始值，row的初始List,right_slach的初始List,left_slash的初始List)
    return ans   #回傳印好的N皇后的List
        

if __name__ == '__main__':
    N = 1
    #N=0
    #N=2
    #N=3
    #N=4
    print(homework_8(N))
    # [["Q"]]
    