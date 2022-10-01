def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    
    l=len(nums)-1 #計算nums的長度，最後一個不算
    frequ=1 #先設最多連續出現1次
    t=1 #設一個變數，用來計算次數

    for i in range(l) :  #利用 for 迴圈取出nums裡的數字         
        if  nums[i]==nums[i+1]: #比較當下取出的數字與下個位子的數字，如果一樣次數加一
            t+=1
        else: #如果不一樣重新計算次數
            t=1
        if t>frequ: #比較之前連續出現最多次與當下計算的次數，如果後者比較大最多次更新為後者
            frequ=t

    return frequ

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    