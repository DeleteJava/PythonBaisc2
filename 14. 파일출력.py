import random
lotto=[]
while len(lotto)<6:
    value=random.randint(1,45) # <임의> 사용시 주의사항 : 중복
    if value not in lotto:
        lotto.append(value)
lotto.sort()
print("당첨번호 :", lotto)

# 파일 출력 : 메모장(텍스트)파일로 출력하여 보관시킨다.
# w : 파괴저장모드(새로운 파일 생성)
# a : 추가저장모드(기존 파일에 덧붙임)
with open("Lotto.txt","a",encoding="UTF-8") as result:
    # write 메서드 : 문자열값을 저장하는 함수
    # writelines 메서드 : 리스트에 저장된 문자열을 모두 저장시켜준다.
    record=str(lotto)
    record=record.replace(",","\t")
    record=record.replace(" ","")
    record=record.strip("[]")+"\n"
    result.write(record)