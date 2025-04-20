#일부로 오류있는 파이썬 파일을 받았음.
print("안녕하세요!")
f = open("data.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()
