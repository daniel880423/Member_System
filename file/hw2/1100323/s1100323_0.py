from operator import and_


def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    count = 0
    lst_len = len(lst)
    if lst_len == 1 and lst[0]%2 !=0:
        return 1
    if lst[0] %2 != 0:
        lst[0]+=1
        count += 1 
    for i in range(lst_len-1):
        fir = lst[i]
        sec = lst[i+1]
        if sec>fir and sec%2 !=0:
            sec+=1
            count+=1
            lst[i+1] = sec
        if fir>sec:
            ori_sec = sec
            sec = fir+2
            count += (sec-ori_sec)
            lst[i+1] = sec

    return count

if __name__ == '__main__':
    lst = [1,5,2,7,4]
    print(homework_2(lst))