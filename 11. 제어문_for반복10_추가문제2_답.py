lst = [1,2,3,4,5,6,7,8,9,10]
start = int(input("시작 위치 입력 >> ")) - 1
end = int(input("끝 위치 입력 >> ")) - 1
if (start < 0 and end<0) or (start > 9 and end > 9) or (start > end):
    print("출력 안합니다.")
else:
    if start < 0:
        start = 0
    if end > 9:
        start = 9
    for i in range(start, end+1):
        print(lst[i], end=" ")
