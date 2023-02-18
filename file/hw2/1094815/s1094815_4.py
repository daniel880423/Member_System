def homework_2(nums):
    ans = 0
    if len(nums) == 1:
        if nums[0] % 2 != 0:
            return ans + 1
    for i in range(len(nums)-1):
        if nums[0] % 2 != 0:
            ans += 1
            nums[i] += 1
        if nums[i] < nums[i+1] and nums[i+1]%2 == 0:
            continue
        else:
            if nums[i] < nums[i+1]:
                ans += 1
                nums[i+1] += 1
            else:
                calculate = nums[i]-nums[i+1]+1+nums[i+1]
                step = nums[i]-nums[i+1]+1
                if calculate % 2 == 0:
                    ans += step
                else:
                    step += 1
                    calculate += 1
                    ans += step
                nums[i+1] = calculate
    return ans

if __name__ == '__main__':
    lst = [1, 4]
    print(homework_2(lst))