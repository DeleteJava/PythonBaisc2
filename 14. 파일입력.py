# 파일입력 : 외부에 있던 것을 컴퓨터의 RAM으로 읽어들인다.
# r : 읽기모드
with open("Lotto.txt","r",encoding="UTF-8") as database:
    # result1=database.read() # 전부 읽어서 하나의 문자열로 준비
    # result1 = database.readline() # 줄바꿈 기준 한줄을 읽어 문자열로 준비
    # result2 = database.readline() # 자동으로 다음줄을 읽는다.
    result1=database.readlines() # 줄단위로 구분하여 리스트로 저장시켜준다.
print(result1)
# 읽어들인 것은 문자열이기 때문에 원하는 형태로 재해석이 되도록
# 직접 <형변환> 을 만들어야 쓸 수 있다.