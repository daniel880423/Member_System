# 載入 pymongo 套件
import pymongo
# 連線到 MongoDB 雲端資料庫
from Comment_Time import connent_to_time  # 載入 Time 的 comment 次數
from Comment_Memery import connent_to_memery  # 載入 Memory 的 comment 次數


def get_comment_and_show(name, name_id,filename, date, comment_by, comment, hw_num, memery, time, memery_file, time_file, frequency, tmp):
    client = pymongo.MongoClient("mongodb+srv://root:root123@potsen.tysb9.mongodb.net/?retryWrites=true&w=majority")
    # print(comment)
    # 把資料放進資料庫中
    # if tmp == "Time":
    #     comment_num = connent_to_time(name)
    # else:
    #     comment_num = connent_to_memery(name)
    tmp = "Comment_" + tmp
    exec(f"db = client.Homework_{hw_num}")  # 選擇操作 website 資料庫 (website 自行定義資料庫名稱)
    exec(f"collection = db.{tmp}")  # 選擇要操作 users 集合 (users 自行定義集合名稱)
    exec(f"""
result = collection.find_one({{'Name':'{name}'}})
if result == None:
    stu_dict = {{'{comment_by}':[{{'ModuleName':'{filename}.py', 'Comment':'{comment}', 'Comment_Time':'{date}'}}]}} 
    collection.insert_one({{'Name':'{name}','StudentID':'{name_id}','Comment_detail': stu_dict, 'Comment_number':1, 'Memery':{memery}, 'Time':{time}, 'Memery_file':'{memery_file}', 'Time_file':'{time_file}', 'Frequency_file':{frequency}}})
else:  
    cursor = collection.find()
    for i in cursor:
        if i['Name'] == '{name}':
            collection.update_one({{'Name':'{name}'}}, {{'$inc':{{'Comment_number':1}}}})
            stu_dict = i['Comment_detail']
            if comment_by in stu_dict:
                for k,v in stu_dict.items():
                    if k == comment_by:
                        test_dict = {{'ModuleName':'{filename}.py', 'Comment':'{comment}', 'Comment_Time':'{date}'}}
                        v.append(test_dict)
                        collection.update_one({{'Name':'{name}'}}, {{'$set':{{'Comment_detail': stu_dict}}}})
                        break
            else:
                stu_dict['{comment_by}'] = [{{'ModuleName':'{filename}.py', 'Comment':'{comment}', 'Comment_Time':'{date}'}}]
                collection.update_one({{'Name':'{name}'}}, {{'$set':{{'Comment_detail': stu_dict}}}})             
                break
""")
    print("資料新增成功")
# #----------------------------------------------------------#

# text = """
# 456456
# 456456
# 456456
# """
# text = text.replace("\n", "!")
# get_comment_and_show("趕羚羊", "1104857", "s1104813_0", "2022-07-31", "詹淯森", "text", "4", 0.54, 1.56, "s1104813_5", "s1104813_9", 10, "Time")