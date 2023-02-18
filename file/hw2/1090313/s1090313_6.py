def homework_2(nums):
    n_step = 0      # number of steps
    for i in range(0,len(nums)):      # run the whole list 
        if len(nums) == 1:            # if the length of the list is only 1, just need to run the program once
            if nums[0] % 2 == 1:      
                n_step = 1
                break
            else:
                break
        if nums[i] % 2 == 1:            # check if nums[i] is odd or even
            nums[i] += 1 
            n_step += 1
            if i==0:
                while nums[i] > nums[i+1]:
                    nums[i+1] += 2
                    n_step += 2
            if i!=0:
                while nums[i-1] >= nums[i]:
                    nums[i] += 2
                    n_step += 2
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
    return n_step

if __name__ == '__main__':
    lst = [3]
    print(homework_2(lst))