def homework_2(nums):
    n_step = 0      # number of steps
    for i in range(0,len(nums)):      # run the whole list 
        if len(nums) == 1:
            if nums[0] % 2 == 1:
                n_step = 1
            else:
                break
        if nums[i] % 2 == 1:            # check if nums[i] is odd or even
            nums[i] += 1 
            #print(nums[i])
            n_step += 1
            if i==0:
                while nums[i] > nums[i+1]:
                    nums[i+1] += 2
                    n_step += 2
            # elif i==0 and nums[i] <= nums[i+1]:
            #     continue
            if i!=0:
                while nums[i-1] >= nums[i]:
                    nums[i] += 2
                    n_step += 2
                    #print(n_step)
                    continue
            
        else:
            
            if i==0:
                while nums[i] >= nums[i+1]:
                    nums[i+1] += 2
                    n_step += 2
            if i!=0:
                while nums[i-1] >= nums[i]:
                    nums[i] += 2
                    n_step += 2
            #print(n_step)
    return n_step

if __name__ == '__main__':
    lst = [1,5,2,7,4]
    print(homework_2(lst))