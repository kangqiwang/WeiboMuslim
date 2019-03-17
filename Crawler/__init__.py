import requests
import json
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
weibo = client['weibo']
comment_shengmengc = weibo['comment_shengmengc']

headers = {
    "Cookies":'xxxxxxxxxxx',
    "User-Agent":'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}

url_comment ='http://m.weibo.cn/api/comments/hotflow?id=4350145582261103&mid=4350145582261103&max_id_type=0'
def get_comment(url):
    wb_data = requests.get(url,headers=headers).text
    data_comment = json.loads(wb_data)
    try:
        datas = data_comment['data']
        for data in datas:
            # print(type(data))
            print(data['text'])
            # comment = {"comment":data.get("text")}
            # comment_shengmengc.insert_one(comment)
    except KeyError:
        pass

get_comment(url_comment)
time.sleep(2)
