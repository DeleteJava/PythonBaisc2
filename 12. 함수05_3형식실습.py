# 함수를 만들 때 요령
# - 전체 코드에서 중복되는 것을 뽑아낸다.
# - 값이 흘러가는 방향을 파악해야 한다.

# 실습1. 1부터의 합을 구하는 함수입니다.
# 1이상의 값을 넣으면 1부터 해당 값까지의 합입니다. ex) 5 -> 1 + 2 + 3 + 4 + 5 = 15
# 1미만의 값을 넣으면 1부터 해당 값까지의 합입니다. ex) -5 -> 1 + 0 + -1 + -2 + -3 + -4 + -5 = -14
# 합을 구하는 함수를 정의하세요.
def get_sum():
    value=int(input("합을 구할 정수 입력 >> "))
    result=0
    if value>=1:
        values=range(1,value+1)
    else:
        values=range(1,value-1,-1)
    for i in values:
        result+=i
    return result

# 실습2.
# 내가 입력한 두 문자를 합쳐서 하나의 값으로 만들어주는
# 함수를 정의하세요.
# ex) A, B -> AB
def get_string():
    word1=input("단어1 입력 >> ")
    word2=input("단어2 입력 >> ")
    return word1+word2

# 실습3.
# 내가 입력한 양의 정수의 약수의 수량을 구하는 함수를
# 정의하세요.
# 0이하의 값은 0이 나오도록 처리합니다.
def get_count():
    value=int(input("정수 입력 >> "))
    if value < 1:
        return 0
    else:
        # 단순수량체크 : 정수값으로 1씩 증가시킨다.
        count=0
        # 값들의 목록이 필요하다 : 리스트 등을 준비한다.
        values=[]
        for i in range(1,value+1):
            if value%i==0:
                count+=1
                values.append(i)
        # 그냥 값 여러개 나온다 -> 쉼표로 구분한다.
        return count, values

result1 = get_sum() # 3형식부터 주의사항 : 더이상 완결되는 프로그램이 아니다.
print("실습1번 :",result1)
result2 = get_string() # 함수명을 동사로 만들어주는 편이 좋다.
print("실습2번 :",result2)
result3 = get_count() # return에 쉼표로 묶으면 튜플이 나온다.
print("실습3번 :",result3)
# ※ 튜플 : 값을 못바꾸는 리스트.