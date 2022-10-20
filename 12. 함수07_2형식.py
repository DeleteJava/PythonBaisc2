def sample():
    num=int(input("정수 하나 입력 >> "))
    for i in range(1,num+1):
        print(i, end=" ")

# 2형식 : 외부로부터 값을 받아와서(복사하여) 이용하는 함수
# - 결과를 보는데 필요한 값을 외부로부터 받는다.
# - 반드시 정규통로를 통하도록 점검해야 한다.
def show_values(num):
    # 매개변수 : 값을 받을 수 있도록 중계해주는 변수
    # - 값이 전달되면, 해당 값으로 함수내에서 생성되는 변수
    for i in range(1,num+1):
        print(i, end=" ")
num=int(input("정수 하나 입력 >> "))
show_values(num)