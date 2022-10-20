# 단순 반복이나 정수만 필요하면 range()라는 함수를 사용한다.

# lst=[]
# num=0
# while 0<=num<5:
#     lst.append(num)
#     num+=1

# range 정규문법 : 독특한 규칙의 숫자들이 필요할 때
for value in range(0,5,1): # range(A,B,C) : A부터 B미만 C씩 변화
    # B-A : 5 - 0 = 5번 반복한다.
    # 0부터 4까지의 1씩 증가한 정수가 준비된다.
    print(value, end=" ")
print()

# range(횟수) : 단순반복 또는 0부터 시작하는 정수가 필요할 때
for value in range(5): # range(0,5,1)
    print(value, end=" ")
print()

# range(시작이상, 끝미만) : 일정구간의 1씩 증가하는 정수가 필요할 때
for value in range(1,11):
    print(value,"번째")

# range 저장해서 쓰면 안되나? 못쓰는건 아님
lst=range(1,11)
print(lst) # 그냥 쓰면 range 자료형으로 나온다.
print(list(lst)) # 활용할려면 형변환시켜야 내부 확인도 가능하고 편해진다.