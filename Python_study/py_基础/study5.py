import json
dic = {'mzy' : 1}
with open('dic.json','w') as fp:
    json.dump(dic,fp)