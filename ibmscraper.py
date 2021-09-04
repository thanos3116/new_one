import pandas as pd
import requests
from bs4 import BeautifulSoup
req=requests.get("https://www.ibm.com/in-en/products/power-system-s922")
soup=BeautifulSoup(req.content, "html.parser")
ibm=soup.find(attrs={'class':'ibm-textcolor-gray-40 ibm-textcolumns-2'}).text.replace('<ul class="ibm-textcolor-gray-40 ibm-textcolumns-2">','')
ibm_data=[[ibm]]
df=pd.DataFrame(ibm_data,columns=[''])
df.to_csv('ibmscrap',index=False)