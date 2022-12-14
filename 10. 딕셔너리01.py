# 딕셔너리 : 리스트와 비슷한 목적으로 준비되는 값
# 차이점 : 인덱스 대신 키를 설정한다.
# -> 연산 되는 것이 없음
# -> 순서에 관계없이 사용할 수 있다.

# 리스트
# 어지간한 경우에는 통제하여 만들어지도록 조절한다.
values=["홍길동", 23, 177.7]
print("이름 : {0} / 나이 : {1} / 키 : {2}".format(*values))
# 통제를 할 수가 없는 상황이라면 어떻게 할 것인가?
values=[23, "홍길동", 177.7] # 
print("이름 : {0} / 나이 : {1} / 키 : {2}".format(*values))

# 딕셔너리
# 순서가 아닌, 고유의 이름을 기반으로 하여 값을 불러온다.
values_d={"이름":"홍길동","나이":23,"키":177.7}

# 1) 각각의 값을 키를 이용해 불러와서 사용한다.
print("이름 : {} / 나이 : {} / 키 : {}".format(values_d["이름"],values_d["나이"],values_d["키"]))

# 2) 지원되는 것들에는 **를 붙여서 딕셔너리를 넣어주면 된다.
#    - 이름을 설정해주거나, 이미 설정된 것들이 있어서 채우는 것들에 적용된다.
print("이름 : {이름} / 나이 : {나이} / 키 : {키}".format(**values_d))

# 3) 저장된 순서가 꼬여있어도 별 상관없다.
values_d={"키":177.7, "이름":"홍길동","나이":23}
print("이름 : {이름} / 나이 : {나이} / 키 : {키}".format(**values_d))
# -> 우리가 만들어 쓰던 일반적인 변수의 묶음과 동등하다.