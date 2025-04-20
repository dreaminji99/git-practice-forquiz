print("안녕하세요!")
f = open("data.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()
