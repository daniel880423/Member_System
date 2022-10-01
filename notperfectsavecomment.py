# 載入 pymongo 套件
import pymongo
# 連線到 MongoDB 雲端資料庫

def not_perfect_get_comment_and_show(name, name_id,filename, date, comment_by, comment, hw_num, not_perfect_memory_file, not_perfect_time_file, frequency, tmp):
    client = pymongo.MongoClient("mongodb+srv://root:root123@potsen.tysb9.mongodb.net/?retryWrites=true&w=majority")
    tmp = "Comment_" + tmp
    exec(f"db = client.Homework_{hw_num}")  # 選擇操作 website 資料庫 (website 自行定義資料庫名稱)
    exec(f"collection = db.{tmp}")  # 選擇要操作 users 集合 (users 自行定義集合名稱)
    exec(f"""
result = collection.find_one({{'Name':'{name}'}})
if result == None:
    stu_dict = {{'{comment_by}':[{{'ModuleName':'{filename}.py', 'Comment':'{comment}', 'Comment_Time':'{date}'}}]}} 
    collection.insert_one({{'Name':'{name}','StudentID':'{name_id}','Comment_detail': stu_dict, 'Comment_number':1, 'Not_perfect_memory_file':'{not_perfect_memory_file}', 'Not_perfect_time_file':'{not_perfect_time_file}', 'Frequency_file':{frequency}}})
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