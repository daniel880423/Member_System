def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    l = len(nums)
    index = 0  
    max = 0   #設最多重複數0個 
    while index < l:    #從第0個開始辨識，直到全部辨識完
        total = 1       #取一個數，初始值有一個
        tmp = nums[index]   #設一個變數來存取當前的index值
        while True:
            index += 1  #取下一位數
            if index > l-1:  #當index超過題目給的總值，跳出迴圈
                break
            jud = nums[index]   #設一個變數存取當前下一位數
            if jud == tmp:  #如果下一位數跟當前數相同
                total += 1  #代表數字一樣且連續，總數加一
            else:       #若當前數跟下一位數不同，跳出迴圈取下一位數
                break
        if total > max: #比較先前總數跟當前算出總數，若當前總數比先前總數大，max就設為當前總數
            max = total
    return max  

if __name__ == '__main__':
    lst = [10,11,54,54,21,61,61,61,12]
    print(homework_1(lst))
    