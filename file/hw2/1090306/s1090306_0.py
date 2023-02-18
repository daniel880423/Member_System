def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    s=0
    idx=0
    for i in lst:
        if (idx == 0):
            if i % 2 != 0:
                s=s+(2-i)
                lst[idx]=lst[idx]+s
        else:
            
            if lst[idx-1]<lst[idx]:
                if lst[idx] % 2 != 0:
                    d=((lst[idx]+1) - lst[idx])
                    s = s + d
                    lst[idx]=lst[idx]+d
            else:
                if lst[idx] % 2 != 0:
                    d=((lst[idx-1]+2) - lst[idx])
                    s = s + d
                    lst[idx]=lst[idx]+d
                else:
                    d=((lst[idx-1]+2) - lst[idx])
                    s = s + d
                    lst[idx]=lst[idx]+d
                                                                                            
        idx=idx+1

    return s
 

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    