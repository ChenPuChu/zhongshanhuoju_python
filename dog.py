from bs4 import BeautifulSoup
import requests
from pyspark.sql.functions import ifnull

header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}
for start_num in range(0,250,25):
    url=requests.get(f"https://movie.douban.com/top250?start={start_num}",headers=header)
    html=url.text
    soup=BeautifulSoup(html,"html.parser")
    all_titles=soup.findAll("span",attrs={"class":"title"})
    all_speak=soup.findAll("span",attrs={"class":"inq"})
    titles=[title.string for title in all_titles if "/" not in title.string]
    speaks=[speak.string for speak in all_speak]
    for i,title in enumerate(titles):
        print(title)
        if i<len(speaks) and speaks[i]:
            print("作品评价：",speaks[i])
        else:
            print("无评分短语")