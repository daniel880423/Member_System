from sqlite3 import enable_callback_tracebacks


def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    a = 0
    w = 0
    
    while True:
        max = 0
        for i in nums:
            if i == w:
                a+= 1
                w = i
            else:
                if a > max:
                    max = a
                w = i
                continue           
        


    return max



if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    