def homework_2(lst): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    index=0
    l=len(lst)
    tmp_ans = sum(lst, l)
    become_even(lst, index, l)
    judge_big_small(lst, index, l)
    ans = sum(lst, l)
    ans = ans - tmp_ans
    return ans

def sum(lst, l):
    total = 0
    for i in range(l):
        total +=lst[i]
    return total

def become_even(lst, index, l):
    if index>=l:
        return 0
    tmp = lst[index]
    tmp_2=tmp//2
    if 2*tmp_2-tmp != 0 :
        tmp+= 1
        lst[index] = tmp
    return become_even(lst, index+1, l)
    
def judge_big_small(lst, index, l):
    tmp=lst[index]
    index_2 = index+1
    if index_2 >= l:
        return 0 
    tmp_2=lst[index_2]
    if tmp > tmp_2:
        add = tmp-tmp_2 + 2
        tmp_2+= add
        lst[index+1] = tmp_2
    if tmp == tmp_2:
        tmp_2+= 2
        lst[index+1] = tmp_2
    judge_big_small(lst, index+1, l)

if __name__ == '__main__':
    lst = [2,4,6,8]
    print(homework_2(lst))
    