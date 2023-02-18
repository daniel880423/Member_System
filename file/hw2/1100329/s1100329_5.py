def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    for i in range(len(lst)):               #以lst長度為範圍的迴圈
        if i==0:                            #如果是首位數，進入
            if lst[i]%2==0:                 #如果首位數為偶數進入
                bef=lst[i]                  #設定變數bef，並將首位數的值丟給bef
                step=0                      #步數設為0
            else :
                bef=lst[i]+1                #設定變數bef<並將首位數的值+1後丟給bef
                step=1                      ##步數設為1
        else:
            if bef==lst[i]:                 #如果bef==lst中跑到的數 ，進入
                bef+=2                      #bef+2
                step+=2                     #step+2
            elif bef>lst[i]:                #如果bef>lst中跑到的數 ，進入
                step=step+bef-lst[i]+2      #步數=原有步數加上bef與lst跑到的數的差，在加2
                bef+=2                      #bef+2
            else:
                if lst[i]%2!=0:             #如果跑到數得值為奇數，進入
                    step+=1             #步數=原有步數加上1
                    bef=lst[i]+1              #將lst跑到的數的值丟給bef，後再加1
                else:
                    bef=lst[i]              #將lst跑到的數的值丟給bef

    return step                                #回傳總步數



if __name__ == '__main__':
    lst = [1, 5, 2, 7, 4]
    print(homework_2(lst))
    