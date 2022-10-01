def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    n=len(nums)
    a=max(nums)
    b=min(nums)
    d=0
    e=0
    ans=1
    if n<3 or n>1000 or a>10000 or b<-10000:
        print("error")
        return
    else:
        for i in range(0,n):
            c=nums[i]
            if c==d:
                e+=1
                if e>=ans:
                    ans=e
            else :
                if e>=ans:
                    ans=e
                e=1
                d=c           

    return ans

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    