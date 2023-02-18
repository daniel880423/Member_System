def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking 
    def pm(tatalw, totalp, items, bag_size):
        global mtotalp

        ttw = tatalw 
        ttp = totalp
        
        if(items):   
            if tatalw+items[0][0] <= bag_size: 
                tatalw+=items[0][0] 
                totalp+=items[0][1] 
                pm(tatalw, totalp, items[1:], bag_size) 

            else: 
                pm(tatalw, totalp, items[1:], bag_size) 

            if totalp > mtotalp:
                mtotalp = totalp
            pm(ttw, ttp, items[1:], bag_size)

    global mtotalp 
    mtotalp = 0
    totalw = 0 
    totalp = 0 

    i = 0 
    while i < len(items) :
        if items[i][0] > bag_size:
            del(items[i])
            i-=1
        i+=1

    pm(totalw, totalp, items, bag_size)
    return mtotalp