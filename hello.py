print("안녕하세요!")
f = open("data.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()
#오류 수정 안 했는데 일단 이걸 적고 깃허브로 add 되는지 확인할거임. 