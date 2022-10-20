# 모듈 불러오기
# 전체불러오기(중복은 없지만, 모듈명을 붙여야 해서 번거로움)
# - import 모듈명
# 일부불러오기(기능명으로 이용가능하지만 중복주의)
# - form 모듈명 import 기능명
import os as os_function # as를 이용해 다른 이름으로 바꿀 수 있음.
# system( ) : 명령어를 실행하는 함수

# pause : 프로그램 실행환경을 일시정지시키는 명령어
print("시작내용")
os_function.system("pause")

# cls : 화면을 깨끗하게 정리해주는 명령어
print("나올내용")
os_function.system("cls")
for i in range(1,100):
    os_function.system("cls")
    print("="*i)