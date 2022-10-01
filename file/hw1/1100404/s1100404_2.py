def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)

    c = 1 #假如下一個與自己一樣，自己也要算，所以初始值是1(c是記數的變數)
    max = 0 #初始化MAX為0
    for i in range(len(nums) - 1): #lst每一個數字都跑一遍
        if nums[i] == None:
            break
        if nums[i] == nums[i + 1]: #假如自己與下一個一樣
            c += 1 #記數+1
            continue #直接進行下一次迴圈
        if c > max: #如果本次的連續出現次數大於最大次數
            max = c #將現在的次數指定給MAX
        c = 1 #記數初始化為1
        
    return max #回傳MAX

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    