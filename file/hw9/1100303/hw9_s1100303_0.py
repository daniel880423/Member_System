from itertools import permutations
def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking
    all={}
    
    def dfs(weight,value,inter,maxvalue):
        if weight<=bag_size:
            maxvalue=value

        item=(weight,value)
        if item not in all:
            all[item]=maxvalue
        else:
            return all[item]
        
        for i in range(len(items)):
            if i not in inter:
                if weight<=bag_size:

                    maxvalue=max(dfs(weight+items[i][0],value+items[i][1],inter+[i],maxvalue),maxvalue)
        return maxvalue
    
    themax=dfs(0,0,[],0)
    return themax
            

if __name__ == '__main__':
    bag_size = 3
    items = [[1,25],[4,120],[4,30],[1,130],[2,20]]
    print(homework_9(bag_size, items))
    # 155
    