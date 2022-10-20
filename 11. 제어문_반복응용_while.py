size=4
count=1
while count<=size:
    # while을 사용할 경우에는 사용된 변수값을 적절한 값으로
    # 바꿔줘야 된다.
    num=1
    # 안바꾸면, 같은 변수를 이용하기 때문에 조건식이 맞지 않아
    # 반복이 안된다.
    while num<=size:
        print("ㅁ", end="" )
        num+=1
    print()
    count+=1
# 반복 구성할 때, 어떤 단계에서 만든 코드든, 성립되어야
# 반복문이 완성된다.
# 반드시 중간중간에 실행해서 결과봐야 한다.