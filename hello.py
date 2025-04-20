print("안녕하세요!")
#f = open("data.txt", "r")
#lines = f.readlines()
#for line in lines:
#    print(line)
#f.close()
#오류 수정 안 했는데 일단 이걸 적고 깃허브로 add 되는지 확인할거임. 
try:
    f = open("data.txt", "r")
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()
except FileNotFoundError:
    print("파일이 존재하지 않습니다. data.txt가 같은 폴더에 있는지 확인하세요.")