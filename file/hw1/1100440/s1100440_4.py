def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    a=None                  #測試資料，即將與index i比較
    n=max=1                 #n是連續次數、max是最大連續次數
    for i in nums:          
        if a==i:            #一樣
            n+=1            

            if n>max:       #比較是否出現最高的連續次數
                max=n       

        else:               #不一樣
            n=1             
            a=i             

    return max              


if __name__ == '__main__':
    lst = [10,11,54,54,21,61,61,61,61,61,12] 
    print(homework_1(lst))
    