import json
def read_json():
    # fo = open("data.json","r")
    with open("data.json") as fo:
        data = json.load(fo)
    print(data)
    fo.close()
# read_json()

def write_json():
    address=[{"Type":"office","zipNumber":510000,"Street":"NanjingRoad"},
             {"Type":"Home","zipNumber":510000,"Street":"ChaojiaoRoad"},
             {"Type":"main-land","zipNumber":510000,"Street":"HuanchengRoad"},]
    fo = open("WriteJsonFile.json","w")
    json.dump(address,fo)
    print("Writing Json Done")
    fo.close()
write_json()