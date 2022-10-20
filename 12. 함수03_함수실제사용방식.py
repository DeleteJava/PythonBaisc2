# 파일을 불러오는 명령어 import
# - import 파일명으로 불러와서 쓴다.
import program1 # 별개 프로그램은 별개 소스파일로 분리하여 관리한다.
import program2 # 함수로 묶어 두지 않으면 불러오는 과정에서 코드가 실행된다.
import program3 # 실행을 통제하기 위하여 함수로 묶어서 저장한다.
while True:
    select=int(input("1. 크기비교 / 2. 절대값 / 3. 연산 / 4. 종료\n>> "))
    if select==4:
        print("실행기를 종료합니다.")
        break
    if select==1:
        # 다른 파일의 것을 쓸 때는 파일명.함수명(변수명)으로 사용한다.
        program1.program()
    elif select==2:
        program2.program()
    elif select==3:
        program3.program()
    else:
        print("잘못된 선택입니다.")