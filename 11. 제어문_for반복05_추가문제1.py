# 실습1-1.
# for를 이용하여 10부터 1까지 1씩
# 감소하는 정수를 출력하세요.
for i in range(1,11,1): # 이상, 미만, 양수
    print(i, end=" ")
print()
for i in range(10,0,-1): # 이하, 초과, 음수
    print(i, end=" ")
print()

# 실습1-2.
# 내가 입력한 구간 내에서 2씩 증가하는
# 정수를 출력하세요.
# 단, 시작값은 끝보다 작거나 같아야 가능합니다.
while True:
    values=input("정수 2개 입력 >> ").split()
    if len(values)==2:
        break
values[0]=int(values[0])
values[1]=int(values[1])
# 만능처리가 필요하다 -> values.sort()
while values[0]>values[1]:
    values[0]=int(input("시작값을 다시 입력하세요 >> "))
    # 또는 values[1]=int(input("끝값을 다시 입력하세요 >> "))
for num in range(values[0],values[1]+1,2):
    print(num, end=" ")
print()

# 실습1-3.
# 내가 지정한 횟수만큼 정수값을 입력을 받아
# 그 합을 구하여 출력하세요.
result=0
for num in range(1,int(input("횟수 입력 >> "))+1):
    result+=int(input("%d번째 값 입력 >> "%(num)))
print("result :",result)
# for의 특징 : 총에 넣는 탄창과 같은 구조이다
# -> 한번 탄창이 들어가면 재장전하던지/탄을 다 쏘지 않으면 중간에
#    변경이 안된다.
# while의 특징 : 조건식을 매 반복마다 실시간으로 점검한다.