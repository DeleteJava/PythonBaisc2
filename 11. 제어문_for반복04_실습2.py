# for 값을 받을 변수명 in 값의 목록:
#     변수로 원하는 것을 수행/다른 내용 실행
# ★range를 이용해 반복을 하는 것이 기본이다.
while True:
    values=input("단수, 범위 설정 >> ").split()
    if len(values)==2:
        break
    else:
        print("잘못된 수량입니다.")
values[0]=int(values[0])
values[1]=int(values[1])
while values[0]<1 or values[0]>9:
    values[0]=int(input("올바른 단을 입력하세요\n>> "))
while values[1]<1 or values[1]>9:
    values[1]=int(input("올바른 범위를 입력하세요\n>> "))
    
# for는 값의 목록을 준비한다는 생각으로 변수준비하면 된다.
# while은 무한반복 용도로 사용된다.
# for는 유한반복 용도로 사용된다.
for num in range(1,values[1]+1):
    print("%d x %d = %2d"%(values[0],num,values[0]*num))
