# for : 값의 목록을 기반으로 반복을 돌린다.
# 주 목적 : 내부에 들어있는 값을 쓰기 위한 것

# 1) 리스트대상
lst=[1,2,3,4,5]
for n in lst:
    print(n) # 내가 반복하면서 할 내용만 신경쓰면 끝!
result=0
for n in lst:
    result+=n # 이용할려면 어디에 무엇을 어떻게 적용해야 하나 파악해야 함
print(result)

# 2) 딕셔너리대상
dic={"A":0,"B":1,"C":2}
for key in dic: # 키만 나오고...
    print(key, dic[key]) # 키를 이용해서 값을 불러온다.