# 전체불러오기 : 중복을 무조건 피할 수 있음
# 단점 : 작성할 때 불편하다.
import random # 모듈의 이름/파일명만 작성
# randint() : 임의의 숫자를 준비해준다.
# 중복값도 나오니 주의
result=[]
for i in range(10):
    result.append(random.randint(1,45))
print(result)

# choice() : 값의 목록중 임의의 하나를 선택한다.
new_value=random.choice(result)
print(new_value)

# 일부불러오기 : 간편하게 쓸 수 있음
# 단점 : 중복되면 못쓴다.
from time import time
from time import ctime, sleep
# time( ) : 1970년 1월 1일 00시00분00초 기준 누적시간을 출력한다.
# 나오는 값은 실수값
# 이를 이용하면 소요시간 등을 계산할 수 있다.
start = time()
lst=[]
for i in range(10000000):
    lst.append(i)
end = time()
print("%.2f초"%(end-start))

# ctime() : 규격화된 시간 정보를 문자열로 준비한다.
print(ctime()) # 문자열이기 때문에 슬라이싱처리하면 된다.

# sleep() : 코드를 지정시간동안 대기시킨다.
sleep(4)
print("4초뒤에 출력이 됩니다.")

# 응용
msg="마치 제가 직접 작성한 것 마냥 속여서 결과를 출력할 수 있습니다."
for ch in msg:
    sleep(random.randint(3,6)/10)
    print(ch,end="")
print()