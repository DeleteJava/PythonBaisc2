# 다중 반복문 : 중첩되어있는 반복문
# 1. 시계 : 초가 다 끝나야 분, 분이 다 끝나야 시간 순으로 반복이 움직인다.
# for hr in range(24):
#     for min in range(60):
#         # 연동되어 움직이지만, 동시(병렬) 동작은 아님.
#         for sec in range(60):
#             print("%.2d시간 %.2d분 %.2d초"%(hr, min, sec))

# 2. 가로/세로
# 1) 평면상의 화면에 보여준다.
for yaxis in range(10): # 줄의 수량을 담당
    for xaxis in range(10): # 한줄을 담당
        print(yaxis,xaxis,sep="", end=" ")
    print()

# 2) 가상으로 만들어낸 평면의 저장공간을 이용한다.
# -> 리스트를 내부에 한번 더 배치하여 사용한다.
# -> 리스트 같은 것들 내부에 리스트 같은 것들이 있다면
#    이는 대분류(바깥 리스트)와 소분류(내부 리스트)의 관계가 된다.
lst2d=[
# x  0 1 2 3 4  # y
    [1,0,0,0,0],# 0
    [0,0,0,0,0],# 1
    [0,0,9,0,0],# 2
    [0,0,0,0,0],# 3
    [0,0,0,0,1],# 4
]
# 기본사용은 인덱싱. 중첩된 만큼....
print(lst2d[2][2]) # 3번째 리스트의 3번째 값
# 공간 그자체가 필요하다 - 인덱싱
print(len(lst2d))
num=1
for x in range(len(lst2d)):
    if x%2==0:
        for y in range(5):
            lst2d[y][x]=num
            num+=1
    else:
        for y in range(4,-1,-1):
            lst2d[y][x]=num
            num+=1
# 단순하게 값만 필요하다 - 리스트를 굴리면 된다.
for lst1d in lst2d:
    for value in lst1d:
        print(value, end=" ")
    print()

# 이중반복은 반복되는 내용이 더 있어서 굴린다.
# 외부반복과 내부 반복은 연동된다.

# 단일반복으로 만들면 끔찍하게 복잡해진다.
# 결과물은 간단할지 몰라도....
y=0
for i in range(25):
    if (i//5)%2==0:
        lst2d[y][i//5] # 0
        y+=1
    else:
        y-=1
        lst2d[y][i//5] # 5
for lst1d in lst2d:
    for value in lst1d:
        print(value, end=" ")
    print()