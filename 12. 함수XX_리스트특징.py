def convert_str(lst):
    for i in range(len(lst)):
        lst[i]=str(lst[i])
    # lst=[]
# 리스트같은 것들은 이런 특징이 있습니다.
lst1=[ 10, 20, 30 ]
lst2=lst1
print(lst2, lst1)
lst1[2]="ABC"
print(lst2, lst1)
lst2[0]=999
print(lst2, lst1)
# ※ 일반적인 변수의 개념
# 정수 / 실수 / 문자열 : Immutable - 불변값 : 복사만 된다.
# - 값에 대해서 매번 새로운 공간을 창조한다.
# 변수명 == 개별저장공간

# ※ 객체지향 프로그래밍의 개념
# 리스트 / 튜플 / 딕셔너리 : Mutable - 가변값 : 변수가 공유되는 구조
# - 값에 대해서 새로운 것이 만들어지거나, 기존 공간을 공유한다.
# 변수명은 고유한 저장공간에 부여되는 이름(들)이 된다.
convert_str(lst1)
print(lst1)
print(lst2)