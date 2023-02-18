def homework_2(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    length=len(nums)
    count=0
    adda=0
    addb=0
    
    if length==1:
        a=nums[0]
        if a%2==0:
            adda=adda+0
        else:
            d=a
            a=a+2
            adda=adda+a-d

    if length!=1:
        for i in range(length):
        
        
            if i==length-1:
                a=nums[-2]
                b=nums[-1]
                break
        

            if i==0:
                a=nums[i]
                b=nums[i+1]
            b=nums[i+1]

            if a%2==0:
                adda=adda+0
            if a%2==1:
                a=a+1
                adda=adda+1
            if b%2==0:
                if b==a:
                    b=b+2
                    addb=addb+2
                if b>a:
                    addb=addb+0
                if a>b:
                    c=b
                    b=a+2
                    addb=addb+b-c
            if b%2==1:
                if b>a:
                    b=b+1
                    addb=addb+1
                if b<a:
                    c=b
                    b=a+2
                    addb=addb+b-c

            a=b
            count=count+adda+addb
            adda=0
            addb=0

    return count

if __name__ == '__main__':
    lst = [8]
    print(homework_2(lst))
    