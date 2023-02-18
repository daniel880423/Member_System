def homework_2(lst):
    tmp = 0
    total = 0
    for i in lst:
        count = 0
        if i <= tmp:
            count += tmp + 1 - i
            i = tmp + 1
        if i % 2 != 0:
            count += 1
            i += 1
        total += count
        tmp = i
    return total

if __name__ == '__main__':
    lst = [1,1,1]
    print(homework_2(lst))
    