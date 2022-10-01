def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    b = set(nums)    #利用set找出串列中出現的所有數字
    x = 0           
    for i in b:       
        if nums.count(i)>x:    #在b串列中，按照順序計算每個數字出現次數，每次計算出的最大次數成為新的x
            x = nums.count(i)
    ans = x-1                  #因為是計算重複次數，所以出現次數需要減掉第一次的出現，才會是題目所求
    return ans

if __name__ == '__main__':
    lst =  [1,2,2,2,3,5,2,2,4,4,4,1,1,1,1,1]

    print(homework_1(lst))
    