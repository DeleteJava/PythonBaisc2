# ※ 위에서 아래로 출력하는 것은 불가능하다!!!!!
# - 의도한 '모양' 을 먼저 그려놓고(저장시켜놓고)
#   이를 출력하면 원하는 형태로 조정할 수 있다.
for i in range(1,6):
    for num in range(i,i+21,5):
        print(num, end=" ")
    print()
# ※ 최초에 판단이 안되면 일단 단일 반복
#   하지만 과도하게 복잡하면 이중 반복으로 접근하자