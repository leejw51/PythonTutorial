import hashlib
 
b = input("Enter password= ")
h = hashlib.sha256(b.encode()).hexdigest();
print(f'{b} hash={h}')
for c in range(10000) :
    h2 = hashlib.sha256(str(c).encode()).hexdigest();    
    print(f'hacking {c} hash={h2}')
    if h2 == h : 
        break

print("##########################################")
print(f"found your password is {c}")