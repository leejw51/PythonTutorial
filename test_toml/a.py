import yaml
import json
import tomlkit


with open("a.toml") as f: 
    a=f.read()
    b=tomlkit.loads(a)
    c=json.dumps(b, indent=4)
    d=json.loads(c)
    e=yaml.dump(d)
    
with open("a.json","w") as f:
    f.write(c)
    
with open("a.yaml", "w") as f:
    f.write(e)