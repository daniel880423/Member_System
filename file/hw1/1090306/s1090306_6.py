def homework_1(nums):# 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    _max = 0
    _cur = 1
    _pre = None
    for i in nums:
        if i == _pre:
            _cur += 1
            _max = max((_cur, _max))
        else:
            _pre = i
            _cur = 1
    return _max

if __name__ == '__main__':
    lst = [10,11,54,54,21,61,61,61,12]
    print(homework_1(lst))
    