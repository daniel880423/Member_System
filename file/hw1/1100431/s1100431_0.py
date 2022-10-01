import sys
def homework_1(nums): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
  result = {}
  for i in set(nums):
    result[i] = nums.count(i)
  return result








     

if __name__ == '__main__':
    lst = [0,0,1,1,1,1,0,0,0,1]
    print(homework_1(lst))
    