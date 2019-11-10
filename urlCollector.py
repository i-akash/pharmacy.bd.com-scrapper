from bs4 import BeautifulSoup as soup 
import requests as req

base_path='https://www.pharmacy.com.bd'
scrap_path=base_path+'/shop/medicines'

drug_url=[]
next_map=dict();
next_url=[]

next_url.append(scrap_path)
next_map[scrap_path]=1

for url in next_url :
    
    html_page=req.get(url).text
    soup_page=soup(html_page,'lxml')
        
    for pref in soup_page.find_all("p",class_="name product-title"):
        drug_url.append(pref.a["href"])
    
    try:
        scrap_path=soup_page.find("a",class_='next page-number')["href"]
    except Exception as e:
        break
    
    if scrap_path not in next_map:
        next_map[scrap_path]=1;
        next_url.append(scrap_path)
    print("done: ",url)

with open("med_saved_url.txt","w") as f:
    for url in drug_url:
        f.write("%s\n"% url);
# print(drug_url)
