# 계단모양으로 출력한다.
size=int(input("계단 단수 >> "))
# 연산으로는 죽었다 깨어나도 안됩니다.
# 원본
# 1차 분해 : 문자열의 곱연산이 가능하니
#           보통 여기서 멈추게 됩니다.
for y in range(1,size+1):
    print("ㅁ"*y+"\n", end="")

# 2차 분해 : 연산기능 없으면?
for y in range(1,size+1):
    # 반복문은 변하는 것이 있으면 이를 자동준비시킨다.
    for x in range(y): # y회 반복
        print("ㅁ", end="")
    print("\n", end="")