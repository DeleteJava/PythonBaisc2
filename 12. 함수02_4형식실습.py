# 4형식의 특징 : 저장된 코드만으로 자료 -> 처리 -> 정보 과정이 모두
#               있어야 하고, 완결되어야 한다.
# 함수 정의시 주의사항
# - 그 어떤 것보다 최상단에 배치한다.
# 함수 호출시 주의사항
# - 함수 중간에 섞어서 사용하지 않는다.

# 실습1. program1
# 두 개의 정수를 입력을 받아 더 큰 수를 출력하고
# 같다면 <서로 같다> 고 출력하는 함수를 정의하세요.
def program1():
    num1=int(input("정수1 입력 >> "))
    num2=int(input("정수2 입력 >> "))
    if num1>num2:
        print("%d이/가 더 큽니다."%(num1))
    elif num1<num2:
        print("%d이/가 더 큽니다."%(num2))
    else:
        print("서로 같습니다.")
# 실습2. program2
# 임의의 정수를 입력을 받아, 그 절대값을 출력하는
# 함수를 정의하세요.
def program2():
    value=int(input("정수 입력 >> "))
    if value<0: value*=-1 # 코드가 하줄뿐이면 한줄로 올릴 수 있습니다.
    print("절대값 :",value)
# 실습3. program3
# 임의의 두 정수를 입력을 받아
# 나누기, 몫연산, 나머지연산 결과를 출력하는 함수를 정의하세요.
# 단, 연산할 수 없는 경우의 수는 <연산불가> 라고 출력합니다.
def program3():
    values=input("정수 2개 입력 >> ").split()
    values[0]=int(values[0])
    values[1]=int(values[1])
    if values[1]==0:
        print("연산불가")
    else:
        print("결과 : %.2f %d %d"%(values[0]/values[1], values[0]//values[1], values[0]%values[1]))

# 실제 함수를 실행하는 위치 : 함수 정의(저장) 끝나고 쓴다.
while True:
    select=int(input("1. 크기비교 / 2. 절대값 / 3. 연산 / 4. 종료\n>> "))
    if select==4:
        print("실행기를 종료합니다.")
        break
    if select==1:
        program1()
    elif select==2:
        program2()
    elif select==3:
        program3()
    else:
        print("잘못된 선택입니다.")