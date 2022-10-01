from multiprocessing.connection import answer_challenge


def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    a=1
    max=0 
    i=0   
    len_nums=len(nums)
    for i in range(len_nums-1):
        if nums[i] == nums[i+1]:
            a+=1
        else:
            a=1
        if a>max:
            max=a

    return max

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    