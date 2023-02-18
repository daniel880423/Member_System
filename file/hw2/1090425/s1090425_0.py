def homework_2(lst):
    lst.insert(0, 0)
    count = 0
    for i in range(1, len(lst)):
        d = lst[i] - lst[i-1]
        s = lst[i]
        if d == 0:
            lst[i] += 2
            count += 2
        if d < 0:
            lst[i] = lst[i-1] + 2
            count += (lst[i] - s)
        if d > 0:
            if lst[i] % 2 != 0:
                lst[i] += 1
                count += 1

    return count


if __name__ == '__main__':
    lst = [1, 5, 2, 7, 4]
    print(homework_2(lst))
    