def homework_9(bag_size, items): # 請同學記得把檔案名稱改成自己的學號(ex.1104813.py)
    # depth first search / breadth first search + backtracking 
    def index(tab, top, items, bag_size):
        global maxtop

        temw = tab #複製一份的tab top給不放入背包使用
        temp = top
        
        if   (items):   
            if tab+items[0][0] <= bag_size: #繼續偷

                tab+=items[0][0] #背包已有的重量 加上此物的重量

                top+=items[0][1] #背包已有的價值 加上此物的價值  

                index(tab, top, items[1:], bag_size) #放入背包，下一項
            else: #偷不動這個
                
                index(tab, top, items[1:], bag_size) #偷不動這個，下一項
            if top > maxtop:
                
                maxtop = top
            index(temw, temp, items[1:], bag_size)#不放入背包，下一項

   
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   
    global maxtop #最大價值

    maxtop = 0

    tab = 0 #當前重量

    top = 0 #當前價值

    i = 0 #忽略items裡超過背包重量上限的物品
    while i < len(items) :

        if items[i][0] > bag_size:

            del(items[i])
            i-=1
        i+=1

    index(tab, top, items, bag_size)

    return maxtop
    