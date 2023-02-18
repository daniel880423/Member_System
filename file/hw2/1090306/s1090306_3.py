def homework_2(nums):
    s = 0
    for i in range(0,len(nums)):
        if len(nums)==1:
            if nums[0] % 2==1:
                s=1
                break
            else:
                break
        elif nums[i] % 2 == 0:
            if i==0:
                while nums[i] >= nums[i+1]:
                    nums[i+1] += 2
                    s += 2
            else:
                while nums[i-1] >= nums[i]:
                    nums[i] += 2
                    s += 2
        elif nums[i] % 2 == 1:
            nums[i] += 1 
            s += 1
            if i==0:
                while nums[i] > nums[i+1]:
                    nums[i+1] += 2
                    s += 2
            else:
                while nums[i-1] >= nums[i]:
                    nums[i] += 2
                    s += 2
    return s

if __name__ == '__main__':
    lst = [37,28,20]
    print(homework_2(lst))
    