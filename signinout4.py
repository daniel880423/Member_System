# 初始化資料庫連線
import os
from werkzeug.utils import secure_filename  # 過濾檔案名稱
import pymongo
from testing import ans  # 計算成績
from autohtml import Html  # 輸出排名
import pandas as pd
# from livereload import Server  # 自動刷新

client = pymongo.MongoClient("mongodb+srv://root:root123@potsen.tysb9.mongodb.net/?retryWrites=true&w=majority")
db = client.member_system   # 資料庫
collection = db.member  # 集合
print("資料庫連線建立成功")

# 載入 Flask 所有的相關工具
from flask import *
app = Flask(__name__, static_folder="public", static_url_path="/")
app.secret_key = "any string but secret"

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/member")
def member():
    cursor = collection.find()  # 取得所有資料的 cursor 物件
    for i in cursor:
        if i["StudentID"] == session["StudentID"]:
            name = i["Name"]
    if "StudentID" in session:
        return render_template("member.html", message = f"{session['StudentID']}{name}")
    else:
        return redirect("/")

# /error?msg=錯誤訊息
@app.route("/error")
def error():
    msg = request.args.get("msg", "發生錯誤,請聯繫客服!")
    return render_template("error.html", message=msg)  # 彈性帶入資料

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/signup", methods=["POST"])
def signup():
    # 從前端接收資料
    nickname = request.form["nickname"]
    studentid = request.form["studentid"]
    password = request.form["password"]
    result = collection.find_one({  # 檢查學號是否相同
        "StudentID":studentid
    })
    if result != None:
        return redirect("/error?msg=學號已經被註冊!")
    collection.insert_one({
        "Name":nickname,
        "StudentID":studentid,
        "Password":password
    })
    return redirect("/error?msg=恭喜~註冊成功!")

@app.route("/signin", methods=["POST"])
def signin():
    # 從前端取得使用者輸入
    studentid = request.form["studentid"]
    password = request.form["password"]
    result = collection.find_one({
        "$and":[
            {"StudentID":studentid,
            "Password":password}
        ]
    })
    # 如果沒有找到對應資料, 代表沒有註冊
    if result == None:
        return redirect("/error?msg=帳號或密碼輸入錯誤!")
        # return render_template("home.html", name="帳號或密碼輸入錯誤!")
    # 登入成功, 在 Session 紀錄會員資訊, 並導向到會員頁面
    session["StudentID"] = result["StudentID"]
    return redirect("/member")

@app.route("/signout")
def signout():
    # 移除 Session 中的會員資訊
    del session["StudentID"]
    return redirect("/")
    
@app.route("/rank1")
def rank1():
    # 顯示演算法概論排名
    if "StudentID" in session:
        #------------------------------------------------# 自動化輸出排名
        Html(createSheet())
        #------------------------------------------------#
        return render_template("rank1.html")
    else:
        return redirect("/error?msg=尚未登入!請先登入謝謝~")

@app.route("/rank2")
def rank2():
    # 顯示演算法概論排名
    if "StudentID" in session:
        #------------------------------------------------# 自動化輸出排名
        Html(createSheet())
        #------------------------------------------------#
        return render_template("rank2.html")
    else:
        return redirect("/error?msg=尚未登入!請先登入謝謝~")

@app.route("/rank3")
def rank3():
    # 顯示演算法概論排名
    if "StudentID" in session:
        #------------------------------------------------# 自動化輸出排名
        Html(createSheet())
        #------------------------------------------------#
        return render_template("rank3.html")
    else:
        return redirect("/error?msg=尚未登入!請先登入謝謝~")

@app.route("/goupload")
def goupload():
    # 顯示上傳檔案的頁面
    if "StudentID" in session:
        msg = request.args.get("msg", "尚未上傳檔案!")
        return render_template("goupload.html")
    else:
        return redirect("/error?msg=尚未登入!請先登入謝謝~")

#--------------------------------------------------------------------------------#    函式區塊

def createSheet():
    sheet_Ori = [[i["StudentID"], i["Name"], i["Time"], i["Memery"]] for i in collection.find() if "Time" in i]
    sheet_StuID = sorted(sheet_Ori, key=lambda x:x[0])
    sheet_Time = sorted(sheet_Ori, key=lambda x:x[2])
    sheet_Memory = sorted(sheet_Ori, key=lambda x:x[3])
    #====================================================================================
    who_get_medal_dict = dict()  # 儲存獎牌人
    medal_dict = {1:"🥇", 2:"🥈", 3:"🥉"}  # 獎牌字典  
    #====================================================================================
    df_Time = pd.DataFrame()
    df_Time["Rank"] = [j[2] for j in sheet_Time]
    df_rank_Time = df_Time.Rank.rank(method='min', ascending=True)
    final_rank_Time = [int(j) for j in df_rank_Time] # 將時間和記憶體做排名

    for i in range(len(sheet_Time)):
        sheet_Time[i] = [final_rank_Time[i]] + sheet_Time[i]
        stu_name = sheet_Time[i][2]
        sheet_Time[i][2] += medal_dict[sheet_Time[i][0]]
        if i < 3:
            if stu_name not in who_get_medal_dict:
                who_get_medal_dict[stu_name] = [medal_dict[sheet_Time[i][0]]]
            else:
                who_get_medal_dict[stu_name].append(medal_dict[sheet_Time[i][0]])
    #====================================================================================
    df_Memory = pd.DataFrame()
    df_Memory["Rank"] = [j[3] for j in sheet_Memory]
    df_rank_Memory = df_Memory.Rank.rank(method='min', ascending=True)
    final_rank_Memory = [int(j) for j in df_rank_Memory] # 將時間和記憶體做排名

    for i in range(len(sheet_Memory)):
        sheet_Memory[i] = [final_rank_Memory[i]] + sheet_Memory[i]
        stu_name = sheet_Memory[i][2]
        sheet_Memory[i][2] += medal_dict[sheet_Memory[i][0]]
        if i < 3:
            if stu_name not in who_get_medal_dict:
                who_get_medal_dict[stu_name] = [medal_dict[sheet_Memory[i][0]]]
            else:
                who_get_medal_dict[stu_name].append(medal_dict[sheet_Memory[i][0]])
    #====================================================================================
    for i in range(len(sheet_StuID)):
        stu_name = sheet_StuID[i][1]
        if stu_name in who_get_medal_dict.keys():
            for medal in who_get_medal_dict[stu_name]:
                sheet_StuID[i][1] += medal
    #====================================================================================
    for i in range(len(sheet_StuID)):
        sheet_StuID[i] = tuple(sheet_StuID[i])
    sheet_StuID = tuple(sheet_StuID)
    for i in range(len(sheet_Time)):
        sheet_Time[i] = tuple(sheet_Time[i])
    sheet_Time = tuple(sheet_Time)
    for i in range(len(sheet_Memory)):
        sheet_Memory[i] = tuple(sheet_Memory[i])
    sheet_Memory = tuple(sheet_Memory)
    #====================================================================================
    return [sheet_StuID, sheet_Time, sheet_Memory]
    

def TimeMemery(id, time, memery, score):  # 寫入時間複雜度和空間複雜度
    if score == 100:
        cursor = collection.find()
        # print(id, time, memery, score)
        for i in cursor:
            if i["StudentID"] == id:
                try:
                    if i["Time"] < time:
                        time = i["Time"]
                except KeyError:pass
                try:
                    if i["Memery"] < memery:
                        memery = i["Memery"]
                except KeyError:pass
        result = collection.update_many({
            "StudentID":id
        }, {
            "$set":{
                "Time":time,
                "Memery":memery
            }
        })
        print(f"符合篩選條件的文件數量(TimeMemery):{result.matched_count}")
        print(f"實際符合更新的文件數量(TimeMemery):{result.modified_count}")


def uploadCount(id, score):  # 計算上傳次數
    if score == 100:
        cursor = collection.find()
        for i in cursor:
            if i["StudentID"] == id:
                if "Frequency" not in i:
                    result = collection.update_one({
                        "StudentID":id
                    }, {
                        "$set":{
                            "Frequency":1
                        }
                    })
                    print(f"符合篩選條件的文件數量(Frequency):{result.matched_count}")
                    print(f"實際符合更新的文件數量(Frequency):{result.modified_count}")
                    break
                else:
                    result = collection.update_one({  # 利用 'StudentID':學號 當搜尋目標 ;再用 '$inc' (加 or 減) 想要的資料
                        "StudentID":id
                    }, {
                        "$inc":{
                            "Frequency":1  # '1' 代表原本數字加 1
                        }
                    })
                    print(f"符合篩選條件的文件數量(Frequency):{result.matched_count}")
                    print(f"實際符合更新的文件數量(Frequency):{result.modified_count}")
                    break


ALLOWED_EXTENSIONS = set(['py'])  # 限制檔案格式
def allowed_file(filename):
    return '.' in filename and \
           filename.split('.', 1)[1] in ALLOWED_EXTENSIONS

#--------------------------------------------------------------------------#

hwn = "4"
@app.route("/upload", methods=["POST"])
def upload():
    UPLOAD_FOLDER = f'C:/Users/user/Desktop/論文/Membership system/file/hw{hwn}'
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER  # 存放的資料夾
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 限制檔案大小 "16MB"
    file = request.files["file"]
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        Score, Time, Memery = ans(filename, hwn)
        TimeMemery(session["StudentID"], Time, Memery, Score)  # Time and Memery 寫入資料庫
        # print(session["StudentID"])
        uploadCount(session["StudentID"], Score)  # 計算上傳次數
        return render_template("membererror.html", message="成功上傳!", Score=f"分數:{Score}", Time=f"時間:{Time}ms", Memery=f"記憶體:{Memery}KB")
    return redirect("/membererror?msg=檔案錯誤,請重新上傳!")

@app.route("/membererror")
def membererror():
    msg = request.args.get("msg", "發生錯誤,請聯繫助教!")
    return render_template("membererror.html", message=msg)


if __name__ == '__main__':
    app.run(port=3000, debug=True)
