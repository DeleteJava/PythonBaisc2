# 리스트의 운용
# 1. 값만 필요하다 -> 바로 굴린다.
lst=[10,20,30]
for num in lst:
    print(num, end=" ")
print()
# 2. range 응용하기 -> 인덱스 때문에 쓴다.
lst=[]
while True:
    value=int(input("새로운 값 입력 >> "))
    if value==0:
        break
    else:
        lst.append(value)
# 1) 입력받는 횟수가 정해진다 - 변수에 저장해서 그 값으로 반복을 통제한다.
# 2) 입력받는 수량을 모른다 - len() 함수를 이용한다.
for i in range(len(lst)):
    print(lst[i], end=" ")
print()