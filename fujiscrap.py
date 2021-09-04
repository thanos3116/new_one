import pandas as pd
import requests
from bs4 import BeautifulSoup
req=requests.get("https://www.fujitsu.com/in/products/computing/servers/primergy/rack/rx1330m4/")
soup=BeautifulSoup(req.content, "html.parser")
u=soup.find(attrs={"class":"paragraph"}).text.replace('<div class="paragraph">',"")
data=[[u]]
df=pd.DataFrame(data,columns=[''])
df.to_csv('fujitsu scrap',index=False)
