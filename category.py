import json 


with open("drugs.json",'r') as jfile:
    data=json.load(jfile)
l=len(data['drugs'])

category=dict()
catlist=list()

for i in range(0,l):
    categ=data["drugs"][i]["categories"]
    for cat in categ:
        if cat not in category:
            category[cat]=1
            catlist.append(cat)

data={}
data["category"]=catlist

print(data)
with open("catagories.json","w") as f:
    json.dump(data,f,indent=4)



