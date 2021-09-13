import json
import yaml
import toml


with open ("a.json") as f :
    a=f.read()
    b1= json.loads(a)    
    cap=b1["app_state"]["capability"]
    ibc=b1["app_state"]["ibc"]
    del ibc["client_genesis"]
    b={"capability": cap, "ibc": ibc}    
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
    
    
    
          
