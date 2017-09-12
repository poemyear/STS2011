f = open("data.txt", "r")
r = f.read()
words = r.split()

d ={}
for k in words:
    if k in d.keys(): d[k] += 1
    else: d[k] = 1

#print(d)
d = sorted(d)
print(d)
