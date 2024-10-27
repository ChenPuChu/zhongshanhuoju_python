from bs4 import BeautifulSoup
import requests
head={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}
url=requests.get("https://huaban.com/discovery",headers=head).text
soup=BeautifulSoup(url,"html.parser")
all_picture=soup.findAll("img",attrs={"class":"transparent-img-bg hb-image"})
for picture in all_picture:
    p_url=picture['src']
    w_picture=picture['alt']
    print(f"图片url:\n{p_url}")
    print(f"图片描述{w_picture}")
    print()