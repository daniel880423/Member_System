def homework_1(nums): 

    time_n = 1
    last_n = None
    n = 1

    for i in nums:
        if i == last_n:
            time_n += 1
            n = max(n, time_n)
        else:
            last_n = i
            time_n = 1

    return n

if __name__ == '__main__':
    lst = [50, 40, 100, 100, 40, 50]
    print(homework_1(lst))