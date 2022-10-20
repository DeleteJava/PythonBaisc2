# 표현만 바꾸면, 원하는 항목을 설정하여 입력받도록 구성하게 된다.

lst=[]
for i in range(1, int(input("입력받을 항목의 수량 >> "))+1):
    lst.append(input("%d번째 항목명 >> "%(i)))
print(lst)

dic={} # 비어있는 딕셔너리
for key in lst: # 순서가 필요없다면, 리스트에서 바로 꺼내면 된다.
    # 키는 되도록 문자열로 해주시는 편이 좋습니다.
    # 숫자로 하면 리스트와 혼란이 생기고, 파이썬 버전에 따라서는 안먹힙니다.
    dic[key] = input("{} 입력 >> ".format(key))
print(dic)