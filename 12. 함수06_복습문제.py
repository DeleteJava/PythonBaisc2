# 파이썬 18일차

# 함수 : 코드를 저장하여 쓰기 위한 방법
# 특징
# - 독립된 코드가 될 수 있다(4형식)
# - 결과를 만들어서 줄 수 있다(3형식)
# - 결과를 만들기 위한 값을 넣어줘야 한다(2형식)
# - 투입하면 결과가 나온다(1형식)

# 복습문제
# - 4형식
# 1. 내가 입력한 수부터 1씩 감소하는 정수 5개를 출력하는 함수를 정의하세요.
def main_program():
    num=int(input("정수 입력 >> "))
    for i in range(5):
        print(num, end=" ")
        num-=1
# - 3형식
# 2. 내가 입력한 양의 정수의 약수의 수량을 외부에서 쓸 수 있도록
#   준비해주는 함수를 정의하세요.
#   0이하의 값일 경우 약수의 수량은 0개로 취급합니다.
def get_count():
    num=int(input("약수를 구할 정수 입력 >> "))
    if num<1:
        return 0
    else:
        count=1
        for i in range(2, num+1):
            if num%i==0:
                count+=1
        return count

result=main_program() # 복습문제1
print(result) # None이 나옵니다. return이 있으면 안됩니다.
result=get_count() # 복습문제2
print(result) # 약수의 수량이 나옵니다.