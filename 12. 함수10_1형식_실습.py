# 실습1-1
# 1) 덧셈함수, 2) 뺄셈함수, 3) 곱셈함수, 4) 나눗셈함수를 정의하세요.
# 단, 나눗셈은 안되는 건 0이 나오도록 하세요.
def add(n1, n2): return n1+n2 # 한줄이면 한줄로 작성할 수 있습니다.
def sub(n1, n2): return n1-n2
def div(n1, n2): return 0 if n2==0 else n1/n2 # 조건문 한줄 쓰기
# def mul(n1, n2): return n1*n2
# lambda : 중간에 함수를 바로 만들어 쓰기 위한 문법. 한줄짜리만 가능.
mul = lambda n1,n2: n1 * n2
# 실시간 코드 작성 및 결과확인을 할 경우, 필요한 함수를 바로 만들기 위한 것

# 실습1-2. 임의의 정수 3개의 평균을 구하는 함수를 정의하세요.
def make_avg(n1,n2,n3):
    return (n1+n2+n3)/3
# *변수명 : 값을 바꿀 수 없는 튜플로 받아서 보관시키는 매개변수 문법
# 주의 : 리스트를 받아서 쓸 예정이면, 설정하지 않는 편이 좋음.
def make_avg_args(*args):
    result=0
    for value in args:
        result+=value
    return result/len(args)

# 실습1-3. 문자열을 적절하게 형변환시키는 함수를 정의하세요.
def convert(str_value):
    # 튜플 생성 : 소괄호로 묶으면 된다.
    check_list=("0","1","2","3","4","5","6","7","8","9",".")
    flag=True
    for ch in str_value:
        if ch not in check_list:
            flag=False
            break
    if flag:
        count=str_value.count(".")
        if count==0:
            return int(str_value)
        elif count==1:
            return float(str_value)
        else:
            return str_value
    else:
        return str_value

num=convert("123")
fnum=convert("3.14")
word=convert("문자열 : ")
print(word, num+fnum) # 문자열 : 126.14

value1=add(10,5) # num1+num2
value2=sub(10,5) # num1-num2
value3=mul(10,5) # num1*num2
value4=div(10,5) # num1/num2
print(value1, value2, value3, value4) # 15, 5, 50, 2.0

result=make_avg(10,15,20)
# result = make_avg_args(10,13,15,19,20)
print("평균 :",result) # 15.0