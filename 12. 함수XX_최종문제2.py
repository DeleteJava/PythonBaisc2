# 1형식(매개변수 있고, return도 있음)
# ※ 파이썬에서는, 함수를 변수로 보내서 저장하여 이용할 수 있다.
#   변수로 받은 값을 이용할 수 있다.
def convert_to_(lst, cnvt): # 리스트의 정수문자열을 정수로 바꾸는 함수
    for i in range(len(lst)):
        lst[i]=cnvt(lst[i])
    return lst
def get_sum_from_lst(lst): # 리스트의 내부의 값들의 합을 구하는 함수
    result = 0
    for value in lst:
        result+=value
    return result
# ※ 우리가 만든 함수는 우리가 만든 다른 함수에서 써먹을 수 있다.
def get_avg_from_lst(lst): # 리스트의 내부의 값들의 평균을 구하는 함수
    result = get_sum_from_lst(lst)/len(lst)
    return result

sample1=["1","2","3","4","5"]
sample2=["1.1","2.2","3.3","4.4","5.5"]
print( "원본\n%s, %s"%(sample1, sample2) )
sample1=convert_to_(sample1, int)
sample2=convert_to_(sample2, float)
print( "변환된 결과물\n%s, %s"%(sample1, sample2) )
sum1=get_sum_from_lst(sample1)
avg1=get_avg_from_lst(sample1)
print("정수리스트의 합/평균 : %d / %.2f"%(sum1, avg1))
sum2=get_sum_from_lst(sample2)
avg2=get_avg_from_lst(sample2)
print("실수리스트의 합/평균 : %d / %.2f"%(sum2, avg2))
