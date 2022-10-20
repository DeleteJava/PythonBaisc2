size=int(input("크기 입력 >> "))
cube=input("문자 입력 >> ")

# 출력 - 연산방식
print( ( cube * size + "\n" ) * size )

# 출력 - 반복방식
for y in range(size):
    for x in range(size):
        print(cube, end="" )
    print()
