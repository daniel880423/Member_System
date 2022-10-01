def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count_new = 1                           #定義一個變數用來存放目前重複數字的個數，初始值為1。
    count_lst = []                          #定義一個list用來存放已計算過的重複數字之個數。
    len_nums = len(nums)                    #定義一個變數代表傳入值nums的長度。
    for k in range(len_nums-1):             #此迴圈代表k從0~len_nums-2去跑
        if nums[k] == nums[k+1]:            #判斷如果nums中index k和k+1的值相等(相等代表連續出現)。
            count_new += 1                  #目前重複數字的個數加1。
            if k+1 == len_nums-1:           #判斷現在的index k+1是否等於list中最後一位的index值(代表已比較到尾巴)。
                count_lst.append(count_new) #在count_lst中加入目前重複數字的個數。
                break                       #脫離迴圈。
     
        else:                               #判斷如果nums中index k和k+1的值不相等。
            if count_new > 1:               #判斷如果此數字至少重複2次。
                count_lst.append(count_new) #在count_lst中加入目前重複數字的個數。
                count_new = 1               #將count_new的值更新為1。
                
            else:                           #判斷如果此數字並未重複2次。
                count_new = 1               #將count_new的值更新為1。
    
    if count_new == 1:                      #如果經過迴圈判斷完後沒有任何連續出現的數字
        count_lst.append(count_new)         #在count_lst中加入count_new所代表的1為連續出現的最多次數。

    count_lst.sort(reverse = True)          #將count_lst中的個數由大排到小。

    return count_lst[0]                     #回傳count_lst中index為0的值即為連續出現的最多次數。


if __name__ == '__main__':
    lst = [10,11,4,54,21,12]
    print(homework_1(lst))
    