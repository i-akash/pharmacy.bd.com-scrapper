from bs4 import BeautifulSoup as soup 
import requests as req
import re 
import json

data={}
data["drugs"]=[]


with open("med_saved_url.txt","r") as f:
    url_list=f.readlines()

done=1

for url in url_list[:2000]:
    try:
        page=req.get(url[:-1]).text
        page_soup=soup(page,"lxml")

        product_image=page_soup.find("div",class_="product-images")
        product_summery=page_soup.find("div",class_="product-info")
        # product_details=page_soup.find("div",class_="product-footer")

        # data structure
        drug={}

        # image
        drug["image_src"]=product_image.img["src"]

        # summery
        drug["title"]=product_summery.h1.text[1:]
        drug["price"]=product_summery.span.text[2:]
        prod_short_description=product_summery.find("div",class_="product-short-description").p.text.split(":")
        drug["brand name"]=prod_short_description[1][1:-14]
        drug["menufacturer"]=prod_short_description[2][2:]

        prod_meta=product_summery.find("div",class_="product_meta")
        drug["DAR"]=prod_meta.find("span",class_="sku").text
        drug["categories"]=[]
            
        for post in prod_meta.find_all("span",class_="posted_in"):
            cnt=0
            temp=post.find_all("a")
            for meta in temp:
                if cnt<len(temp)-1:
                    drug["categories"].append(meta.text)
                else :
                    drug["brand"]=meta.text
            cnt+=1    
        print(done,": Done !!")
        done+=1
        data["drugs"].append(drug)
    
    except Exception as e:
        done+=1
        
    
# description
# tab_description=product_details.find("div",id="tab-description")

# description={}
# header=[]

# for title in tab_description.find_all("h4",class_="ac-header"):
#     header.append(title.text)
# cnt=0
# for info in tab_description.find_all("div",class_="col-xs-12 ac-body"):
#     key=header[cnt]
#     description[key]=[]
#     cnt+=1     

#     for post in info.find_all("p"):
#         try:
#             key=post.strong
#         except Exception as e:
#             description[key].append(post)

            
#         print(key)



with open("drugs.json","w") as f:
    json.dump(data,f,indent=4)