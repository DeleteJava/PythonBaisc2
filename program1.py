def program():
    num1=int(input("정수1 입력 >> "))
    num2=int(input("정수2 입력 >> "))
    if num1>num2:
        print("%d이/가 더 큽니다."%(num1))
    elif num1<num2:
        print("%d이/가 더 큽니다."%(num2))
    else:
        print("서로 같습니다.")