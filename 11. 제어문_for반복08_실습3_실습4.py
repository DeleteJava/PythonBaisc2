# 실습3번
lst=[]
for i in range(1, int(input("횟수 설정 >> "))+1):
    lst.append(input("%d번째 값 입력 >> "%(i)))
print(lst)
# 실습4번
dic={} # 비어있는 딕셔너리
for i in range(len(lst)):
    # 키는 되도록 문자열로 해주시는 편이 좋습니다.
    # 숫자로 하면 리스트와 혼란이 생기고, 파이썬 버전에 따라서는 안먹힙니다.
    dic[lst[i]] = input("새로운 값{} 입력 >>".format(i+1))
print(dic)