f = open("data.txt", "r")
r = f.read()
words = r.split()

analyze = {}
for word in words:
    analyze[word] = analyze.get(word, 0) + 1   

flist = sorted(analyze.items(), key=lambda kv: kv[1], reverse=True)
print("number of words is ", len(flist))
cnt = 0
for k, v in flist:
    print(k, v)
    if cnt > 100: break
    cnt += 1
