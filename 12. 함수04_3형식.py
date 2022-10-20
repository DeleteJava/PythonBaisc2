# 4형식의 문제 : 독립되어 있음
# - 일절의 간섭을 허용하지 않는다.....
# 해결책 : 변수에 저장된 값은 복사가 되니, 이를 외부로 복사시켜주면 된다!
# -> return 명령어를 이용한다.
# ★ return : 함수를 종료시키는 명령어이며
#            함수 내부의 특정값을 외부로 복사시켜주는 명령어

# 3형식 : 값을 외부로 복사시켜서 쓸 수 있게 해주는 함수
# 3형식부터는 기능을 구분해야 한다.
# 자료 -> 처리 -> 정보 중에서 정보(출력)을 쳐냈기 때문에, 프로그램이 안된다.
def program1():
    num1=int(input("정수1 입력 >> "))
    num2=int(input("정수2 입력 >> "))
    # 주의사항 : 버려지는 경우의 수가 없도록 배치해야 한다.
    if num1>num2:
        return num1
    elif num1<num2:
        return num2
    else:
        print("서로 같습니다.") # 여기로 오게 되면 못쓰는 값 None이 나온다.
        # 1. return을 포기한다.
        # 2. 임의값을 약속으로 정해서 나오도록 한다.

def program2():
    value=int(input("정수 입력 >> "))
    if value<0: value*=-1
    return value

result = program2()
print("절대값 :", result)
result1=program1()
print("결과 :", result1)