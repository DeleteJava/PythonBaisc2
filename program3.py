def program():
    values=input("정수 2개 입력 >> ").split()
    values[0]=int(values[0])
    values[1]=int(values[1])
    if values[1]==0:
        print("연산불가")
    else:
        print("결과 : %.2f %d %d"%(values[0]/values[1], values[0]//values[1], values[0]%values[1]))