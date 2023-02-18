def homework_2(lst):
    count = 0
    if lst[0] %2 != 0:
        count =1
        lst[0]+=1
    for i in range(1,len(lst)):
        if lst[i] < lst[i-1]:
            count += lst[i-1] - lst[i] +2
            lst[i] = lst[i-1] +2
        if lst[i] % 2 != 0:
            lst[0] +=1
            count +=1
    return count

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    