def homework_2(array):# 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    step_count = 0
    for i in range(len(array)):
        if array[i] % 2 != 0 and (array[i] > array[i - 1]): #奇數且大於上一數
            step_count += 1 #奇數+1=偶數
            array[i] = array[i] + 1 #更改成偶數升冪條件
        elif array[i] % 2 != 0 and (array[i] <= array[i - 1]): #奇數且小於上一數
            if i == 0: #第一個數無法與前一個數比較
                step_count +=1 #奇數+1=偶數
                array[i] +=1 #更改成偶數升冪條件
            else:
                step_count += array[i - 1] + 2 - array[i] #上一個偶數+2扣掉目前的數
                array[i] = array[i - 1] + 2 #更改成偶數升冪條件
        elif array[i] % 2 == 0 and (array[i] <= array[i - 1]): #偶數且小於上一數
            if i != 0:
                step_count += array[i-1] + 2 - array[i] #上一個偶數+2扣掉目前的數
                array[i] = array[i-1] + 2 #更改成偶數升冪條件

    return step_count

if __name__ == '__main__':
    lst = [1,5,2,7,4]
    print(homework_2(lst))
    