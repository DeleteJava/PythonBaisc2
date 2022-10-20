# 1형식 : 처리만 하는 함수
# - <만들어낸다> 를 연상시키는 동사로 쓰는 편이 좋다.
def make_sum(num):
    result=0
    for i in range(1, num+1):
        result+=i
    return result

value=int(input("정수 입력 >> "))
result=make_sum(value)
print("결과 :",result)