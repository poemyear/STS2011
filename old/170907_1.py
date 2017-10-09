import datetime, time
import urllib.request
import re
def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

url = "http://www.khaiyang.com/3175"

f = urllib.request.urlopen(url)
data = f.read().decode('utf-8')

begin = data.find("<!-- 본문상단 우측 -->")
end = data.find("지켜봐야 겠습니다")

end += len("지켜봐야 겠습니다")


print("total=", len(data))
print("begin=", begin)
print("length=", end-begin)

review = data[begin:end]
review = striphtml(review)
review = re.sub(r'(\(.*\);|&nbsp|\▲|;)', '', review)
review = re.sub(r'.*=.*', '', review)
words = review.split()

analyze = {}
for word in words:
    analyze[word] = analyze.get(word, 0) + 1   

flist = sorted(analyze.items(), key=lambda kv: kv[1], reverse=True)
print("number of words is ", len(flist))
cnt = 0
for k, v in flist:
    print(k, v)
    if cnt > 300: break
    cnt += 1
