# 載入 pymongo 套件
import pymongo
# 連線到 MongoDB 雲端資料庫
client = pymongo.MongoClient("mongodb+srv://root:root123@potsen.tysb9.mongodb.net/?retryWrites=true&w=majority")
# 把資料放進資料庫中

def connent_to_time(name):
    db = client.Homework_4  # 選擇操作 website 資料庫 (website 自行定義資料庫名稱)
    collection = db.Comment_Time
    result = collection.find_one({'Name':name})
    if result == None:return None
    else:
        cursor = collection.find()
        for i in cursor:
            if i["Name"] == name:
                return str(i["Comment_number"] + 1)