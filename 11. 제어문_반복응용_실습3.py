# 출력할 때는 반드시 Z이다. N모양으로 못그린다.

# 다음단을 출력할 수 있도록 준비해준다.
for num1 in range(1,10):
    # 각 단의 출력을 담당한다.
    for num2 in range(1,10):
        # 핵심 코드는 가장 안쪽의 반복문에 배치된다.
        print(num1, "x", num2, "=", num1 * num2)
    # 바깥반복문의 종속문은 내부 반복문을 보조하는 것들이 배치된다.
    print()

# 단일반복
for num in range(81):
    num1=num // 9 + 1
    num2=num % 9 + 1
    print(num1,"x",num2,"=",num1 * num2)