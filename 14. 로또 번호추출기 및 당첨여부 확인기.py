# 로또 당첨번호를 임의로 선택하여 출력한다.
# 내가 입력한 번호와 당첨번호를 비교한다.

# 현재 이 while 무한반복은 6개의 값을 채우는 것이 목적입니다.
# 6번 반복시 값이 채워질 때마다 중복활률은 0퍼센트에서 1/45, 2/45, 3/45로 점점 상승합니다.
# 그래서 반복횟수는 더 많아질 수 있고, 정확하게 6번으로 처리가 되지 않습니다.
import random
lotto=[]
while len(lotto)<6:
    value=random.randint(1,45) # <임의> 사용시 주의사항 : 중복
    if value not in lotto:
        lotto.append(value)
lotto.sort()
print("당첨번호 :", lotto)
myLotto=[]
while len(myLotto)<6:
    value=int(input("번호 입력 >> "))
    if value>=1 and value<=45:
        if value not in myLotto:
            myLotto.append(value)
        else:
            print("중복된 값입니다.")
    else:
        print("잘못된 범위입니다.")
print("당첨번호 :", myLotto)
count=7
for value1 in myLotto:
    if value1 in lotto:
        count-=1
if count<=5:
    print("당신은 %d등입니다."%(count))
else:
    print("꼴등입니다.")