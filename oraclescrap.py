import pandas as pd
import requests
from bs4 import BeautifulSoup
req=requests.get("https://www.oracle.com/in/servers/x86/")
soup=BeautifulSoup(req.content, "html.parser")
o=soup.find(attrs={'class':'rc36w2'}).text.replace('<div class="rc36w2">',"")
oracle_data=[[o]]
df=pd.DataFrame(oracle_data,columns=['u'])
df.to_csv('oracle_scrapy.csv',index=False)
