def  to_1D_array(Matrix, Major):  # Matrix型態:list[list]，Major型態:str
    length = len(Matrix)                #先算矩陣大小
    #右下
    right_down = True                    #判斷是否為右下三角形，一開始先設為True
    for i in range(length -1):
        for j in range(length-i-1):      #右下三角形，右上左下對角線的左上方都是0
            if Matrix[i][j] != 0:        #若左上方有不為0的就不是右下三角形
                right_down=False         #若不是則為False

    #左下
    left_down = True                     #判斷是否為左下三角形，一開始先設為True
    for i in range(length -1):
        for j in range(1 + i, length):   #左下三角形，左上右下對角線的右上方都是0
            if Matrix[i][j] != 0:        #若右上方有不為0的就不是左下三角形
                left_down = False           #若不是則為False


    #右上
    right_up = True                     #判斷是否為右上三角形，一開始先設為True
    for i in range(1, length):
        for j in range(i):              #右上三角形，左上右下對角線的左下方都是0
            if Matrix[i][j] != 0:       #若左下方有不為0的就不是右上三角形
                right_up = False            #若不是則為False

    # 左上
    left_up = True                       #判斷是否為左上三角形，一開始先設為True
    for i in range(1, length):
        for j in range(length-i, length):   #左上三角形，右上左下對角線的右下方都是0
            if Matrix[i][j] != 0:           #若右下方有不為0的就不是左上三角形
                left_up = False             #若不是則為False



    if right_down and Major=='c':                       #若是右下三角形且Major 為c
        one＿dimensional＿matrix = [None] * ((1 + length) * length // 2) #算出一維陣列中有幾個值
        index = 0                                       #B陣列中要更改的第一個位置
        for i in range(length):
            for j in range(0,i+1):                      #右下三角形且c，順序為第一行最下面，第二行下面兩個由上而下．．．最後一行全部的由上而下
                one＿dimensional＿matrix[index] = Matrix[length-1-i+j][i]      #算出位置後依序更改一維陣列中原本none的值
                index += 1                              #每更改一個後，B陣列的要更改的位置往後一位


    elif right_down and Major=='r':                     #若是右下三角形且Major 為r
        one＿dimensional＿matrix = [None] * ((1 + length) * length // 2)       #算出一維陣列中有幾個值
        index = 0                                       #B陣列中要更改的第一個位置
        for i in range(length):
            for j in range(0, i + 1):                   #右下三角形且r，順序為第一列最右邊，第二列右邊兩個由左而右．．．最後一列全部的由左而右
                one＿dimensional＿matrix[index] = Matrix[i][length - 1 - i + j]#算出位置後依序更改一維陣列中原本none的值
                index += 1                              #每更改一個後，B陣列的要更改的位置往後一位


    elif left_down and Major=='c':                      #若是左下三角形且Major 為c
        one＿dimensional＿matrix = [None] * ((1 + length) * length // 2)       #算出一維陣列中有幾個值
        index = 0                                       #B陣列中要更改的第一個位置
        for i in range(length):
            for j in range(length-i):                   #左下三角形且c，順序為第一行全部由上而下，第二行除了第一個其他由上而下．．．最後一行最後一個
                one＿dimensional＿matrix[index] = Matrix[i+j][i]#算出位置後依序更改一維陣列中原本none的值
                index += 1                              #每更改一個後，B陣列的要更改的位置往後一位


    elif left_down and Major=='r':                      #若是左下三角形且Major 為r
        one＿dimensional＿matrix = [None] * ((1 + length) * length // 2)       #算出一維陣列中有幾個值
        index = 0                                       #B陣列中要更改的第一個位置
        for i in range(length):
            for j in range(0, i + 1):                   #左下三角形且r，順序為第一列最左邊，第二列左邊兩個由左而右．．．最後一列全部的由左而右
                one＿dimensional＿matrix[index] = Matrix[i][j]  #算出位置後依序更改一維陣列中原本none的值
                index += 1                              #每更改一個後，B陣列的要更改的位置往後一位


    elif right_up and Major == 'c':                     #若是右上三角形且Major 為c
        one＿dimensional＿matrix = [None] * ((1 + length) * length // 2)       #算出一維陣列中有幾個值
        index = 0                                       #B陣列中要更改的第一個位置
        for i in range(length):
            for j in range(0,i+1):                      #右上三角形且c，順序為第一行第一個，第二行上面兩個由上而下．．．最後一行全部由上而下
                one＿dimensional＿matrix[index] = Matrix[j][i]#算出位置後依序更改一維陣列中原本none的值
                index += 1                              #每更改一個後，B陣列的要更改的位置往後一位


    elif right_up and Major == 'r':                     #若是右上三角形且Major 為r
        one＿dimensional＿matrix = [None] * ((1 + length) * length // 2)       #算出一維陣列中有幾個值
        index = 0                                       #B陣列中要更改的第一個位置
        for i in range(length):
            for j in range(i, length):                  #右上三角形且r，順序為第一列全部由左而右，第二列除了最左邊其他由左而右．．．最後一列最後一個
                one＿dimensional＿matrix[index] = Matrix[i][j] #算出位置後依序更改一維陣列中原本none的值
                index += 1                              #每更改一個後，B陣列的要更改的位置往後一位


    elif left_up and Major == 'c':                      #若是左上三角形且Major 為c
        one＿dimensional＿matrix = [None] * ((1 + length) * length // 2)       #算出一維陣列中有幾個值
        index = 0                                       #B陣列中要更改的第一個位置
        for i in range(length):
            for j in range(length - i):                 #左上三角形且c，順序為第一行全部由上而下，第二行除了最後一個其他由上而下．．．最後一行第一個
                one＿dimensional＿matrix[index] = Matrix[j][i] #算出位置後依序更改一維陣列中原本none的值
                index += 1                              #每更改一個後，B陣列的要更改的位置往後一位


    elif left_up and Major == 'r':                      #若是左上三角形且Major 為r
        one＿dimensional＿matrix = [None] * ((1 + length) * length // 2)       #算出一維陣列中有幾個值
        index = 0                                       #B陣列中要更改的第一個位置
        for i in range(length):
            for j in range(length - i):                 #左上三角形且r，順序為第一列全部由左而右，第二列除了最右邊其他由左而右．．．最後一列第一個
                one＿dimensional＿matrix[index] = Matrix[i][j] #算出位置後依序更改一維陣列中原本none的值
                index += 1                                #每更改一個後，B陣列的要更改的位置往後一位


    return one＿dimensional＿matrix                       #算完後回傳B
    # return  # 回傳值型態:list


if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[0,0,0,0,0,0],
          [0,0,0,0,7,8],
          [0,0,0,5,5,9],
          [0,0,1,6,4,1],
          [0,0,5,8,4,9],
          [0,7,2,6,9,0]]
    to_1D_array(input_matrix, "r")
    output_array = to_1D_array(input_matrix, "c")
    print(output_array)
