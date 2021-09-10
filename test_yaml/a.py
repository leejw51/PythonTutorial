import yaml
import json
import tomlkit


with open("a.yaml") as f: 
    b= yaml.load(f, Loader=yaml.FullLoader)
b["chainmain-1"]["cmd"]="disney"
myjson=json.dumps(b, indent=4)
print(myjson)

with open("a.json","w") as f: 
    f.write(myjson)


with open("a.json") as f:
    myjson2= json.load(f)

myyaml= yaml.dump(myjson2)
print(myyaml)

with open("b.yaml", "w") as f:
    f.write(myyaml)
    
    
mytoml=tomlkit.dumps(myjson2)
print(mytoml)

with open("c.toml", "w") as f:
    f.write(mytoml)