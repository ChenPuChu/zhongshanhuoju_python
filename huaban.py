# 引入http请求包
import requests
# 引入json包
import json
# 引入webp包
from PIL import Image
# 引入io包
from io import BytesIO

# 搜索名称
search_name = "封面"
# 爬取的个数
limit = "30"
# 本地保存的路径
file_path="./imgs"

url = "https://huaban.com/v3/search/file?text="+search_name+"&sort=all&limit="+limit+"&page=2&position=search_pin&fields=pins:PIN|total,facets,split_words,relations,rec_topic_material,topics"

# 发送搜索请求
search_response_text=requests.get(url).text

# 将请求到的json数据转换为python对象
search_response_data=json.loads(search_response_text)

# 获取图片所在数据
pins=search_response_data["pins"]

# 定义图片网络路径数组
img_url_arr=[]
# 将图片路径存放在数组中
try:
    for i in range(int(limit)):
        img_url_arr.append("https://gd-hbimg.huaban.com/"+pins[i]["file"]["key"]+"_fw240webp")
except:
    pass
# 遍历图片路径数组，进行网络请求
for i in range(len(img_url_arr)):
    temp=requests.get(img_url_arr[i])
    try:
        byte_stream=BytesIO(temp.content)
        im = Image.open(byte_stream)
        # 将图片转换为jpeg并保存
        if im.mode == "RGBA":
            im.load()  # required for png.split()
            background = Image.new("RGB", im.size, (255, 255, 255))
            background.paste(im, mask=im.split()[3])
        im.save('{}/{}.jpeg'.format(file_path,i) ,"JPEG")
    except:
        pass

