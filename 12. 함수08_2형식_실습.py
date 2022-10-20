# 매개변수는 함수를 정의할 때 쉼표로 구분하여 늘리면 됩니다.

# 1. 임의의 정수 2개 중 더 큰 수를 출력하는 함수를 정의하세요.
#   같으면 <서로 같습니다.> 라고 출력합니다.
def compare_2values(num1, num2):
    if num1 > num2:
        print("%d이/가 더 큽니다."%(num1))
    elif num2 > num1:
        print("%d이/가 더 큽니다."%(num2))
    else:
        print("서로 같습니다.")
# 기본값(Default Arguments) : 매개변수에 값 넣어두기
# - 자주 사용되는 상수값을 미리 넣어두는 것
# - 주의사항 : 오른쪽부터 채워서 써야 한다.
#             호출할 땐 값이 왼쪽부터 채워지기 때문이다.
def compare_2values_default(num1=None, num2=None):
    if num1==None:
        num1 = int(input("처번째 값 입력 >> "))
    if num2==None:
        num2 = int(input("두번째 값 입력 >> "))
    if num1 > num2:
        print("%d이/가 더 큽니다."%(num1))
    elif num2 > num1:
        print("%d이/가 더 큽니다."%(num2))
    else:
        print("서로 같습니다.")
# 2. 임의의 정수의 절대값을 출력하는 함수를 정의합니다.
def show_absolute(num):
    if num<0: num*=-1 # num = abs(num)
    print("절대값 :",num)

# 3. 두 정수의 몫 / 나머지 / 나누기 결과를 출력하는 함수를
#   정의하세요.
#   단, 안되는 경우의 수가 한가지 존재하며
#   이 때는 <연산불가> 라고 출력합니다.
def show_result(n1, n2):
    if n2==0:
        print("연산불가")
    else:
        print("%d %d %.2f"%(n1//n2,n1%n2,n1/n2))

compare_2values(10,5) # 10이/가 더큽니다.
compare_2values(5,8) # 8이/가 더 큽니다.
compare_2values(5,5) # 서로 같습니다.
# compare_2values_default()

show_absolute(-8) # 절대값 : 8
show_absolute(8) # 절대값 : 8

show_result(4, 8) # 0 / 4 / 0.50
show_result(8, 4) # 2 / 0 / 2.00
show_result(9, 0) # 연산불가
