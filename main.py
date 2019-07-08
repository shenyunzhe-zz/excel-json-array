import pandas as pd
import json

cards = {
    "id":11,
    "cards":[]
}
# 提取excel数据 
excel_data = pd.read_excel('数据.xlsx')

#将数据转成json json.loads(excel_data.to_json(force_ascii=False,orient='index'))
#讲数据插入数组
for (k,v) in json.loads(excel_data.to_json(force_ascii=False,orient='index')).items():
    cards["cards"].append(v)

print(cards)
