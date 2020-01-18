from json import load, dump

with open("grad-2018.json", "r") as f:
    j = load(f)
    #for d in j:
        #if d["name_j"] == "全教員":
            #print(d)

with open("all_grad-2018.json", "w", encoding = "utf-8") as g:
    for d in j:
        if d["name_j"] == "全教員":
            dump(d, g, ensure_ascii=False)
        else:
            pass
        
with open("jd-2018.json", "r") as f:
    j = load(f)
    #for d in j:
        #if d["name_j"] == "全教員":
            #print(d)

with open("all_jd-2018.json", "w", encoding = "utf-8") as g:
    for d in j:
        if d["name_j"] == "全教員":
            dump(d, g, ensure_ascii=False)
        else:
            pass