# 입력받아 저장하는 방법
# 1) 반복이용하기 - 보통 while 이용안합니다.
# 2) 미리 설정해놓고 입력받기
inform={
    "이름":input("이름 입력 >> "),
    "나이":input("나이 입력 >> "),
    "취미":input("취미 입력 >> ")
    }
print(inform)
# 3) 없는 키를 생성하며 입력받아 저장하기
inform={}
inform["이름"]=input("이름 입력 >> ")
inform["나이"]=input("나이 입력 >> ")
inform["취미"]=input("취미 입력 >> ")
print(inform)

# 딕셔너리의 사용은 키를 이용해 매칭되어 있는 값 불러오기
# 키는 변수명에 대응된다.
# 값은 변수에 저장된 값이다.
# 1) 기본사용 : 하나씩 불러와서 쓰기.
print("이름 :",inform["이름"])
print("나이 :",inform["나이"])
print("취미 :",inform["취미"])
print(inform["이름"],inform["나이"],inform["취미"])

# 2) 지원되는 것들에 한하여 ** 붙여서 넘기기
# -> 내부에서는 replace를 이용해서 처리됩니다.
print("이름 : {이름}".format(**inform))
print("나이 : {나이}".format(**inform))
print("취미 : {취미}".format(**inform))
print("{이름} {나이} {취미}".format(**inform))

# ※format메서드에 딕셔너리를 넘겼을 경우, 비슷하게 구현한 형태...
# print("이름 : {이름}".format(**inform))
form="이름 : {이름}"
if "{" in form:
    first=form.index("{")
if "}" in form:
    last=form.index("}")
key=form[first+1:last]
if key in inform: # 딕셔너리에 대해서는 키가 있는지 여부만 체크가능
    result = form.replace("{"+key+"}", inform[key])
print(result)
