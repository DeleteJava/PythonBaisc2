# 딕셔너리는 직접 만들면 손가락 꼬이기 딱 좋은 구조다.
# 1) 키는 왠만하면 문자열로 준비해야 한다.
# -> 정수값은 나중에 리스트와 구분이 잘 안되어서 사용못할 수 있다.
# 2) 반복을 이용하여 만들어내는 경우가 태반이다.
# -> 리스트를 이용해 목록을 만든다.
info={} # 깡통 딕셔너리
item_list=["이름","나이","취미"]
values=input("이름, 나이, 취미 입력 >> ").split()
size=len(item_list)
index=0
info={}
while index<size:
    # 추가할 때 해당 키가 없으면 생성하고 저장한다.
    info[ item_list[ index ] ] = values[ index ]
    # 우리가 작성하는 변수생성과 동등. 위치가 딕셔너리 내부일 뿐이다.
    index+=1
print(info)

# info[ item_list[ 0 ] ] = values[ 0 ]
# info[ item_list[ 1 ] ] = values[ 1 ]
# info[ item_list[ 2 ] ] = values[ 2 : ] # 굳이 반복안해도 가능함.
# print(info)
