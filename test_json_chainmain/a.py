import json
import yaml
import toml


with open ("a.json") as f :
    a=f.read()
    b= json.loads(a)
    c=json.dumps(b, indent=4)
    print(c)
    
with open ("b.json", "w") as f:
    f.write(c)
    
with open ("b.yaml", "w") as f:
    c=yaml.dump(b)    
    f.write(c)

with open ("b.toml", "w") as f:
    c=toml.dumps(b)    
    f.write(c)
    
