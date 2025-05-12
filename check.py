
import time
import os
import sys
import json
import magic # type: ignore
import pandas as pd
from logings import Loggings
temp = Loggings()
logging = temp.get_hande()

def make_json_obj(key_list:list,info):
    key_list.append(info)

def fill_json_obj(json_obj,key,value):
    json_obj[key] = value

def get_file_type_by_content(file_path):
    mime = magic.Magic(mime=True)
    with open(file_path, "rb") as f:
        file_type = mime.from_buffer(f.read(2048))  # 仅读取前 2048 字节
    return file_type


def del_excel(file_path, rows=0):
    df = pd.read_excel(file_path, engine="openpyxl")  # 必须指定 engine="openpyxl"
    res_json = list()
    key_list =list()
    i =rows
    size =df.shape[0] - 1 # 序号减一
    print(size)
    while i <= size:
        if i == rows:
            for item in df.iloc[i]:
                # if 'nan' or 'np' in item:
                #     continue
                make_json_obj(key_list,item) 
            print(key_list)    
        else:
            key = 0
            json_obj=dict()
            for item in df.iloc[i]:
                fill_json_obj(json_obj,key_list[key],item)
                key+=1
            res_json.append(json_obj)
        
        i+=1

    with open(".test.json","ab") as fs:
        fs.write(json.dumps(res_json,ensure_ascii=False,indent= 2).encode())



if __name__=="__main__":
    file_path = sys.argv[1]
    rows = sys.argv[2]
    try:
        file_type=get_file_type_by_content(file_path)
    except Exception as e:
        logging.error(e)
        exit()
    print(file_type)
    if '.xlsx'in file_path or file_type in ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet","application/vnd.ms-excel"]:
        del_excel(file_path,int(rows))