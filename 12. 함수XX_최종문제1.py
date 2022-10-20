# 3형식(매개변수 없고, return만 있음)
def get_dic(): # 딕셔너리가 나오는 함수
    dic={}
    for i in range(1,2+1):
        values=input("%d번 항목명과 값 입력 >> "%(i)).split()
        dic[values[0]]=values[1]
    return dic
def get_list(): # 리스트가 나오는 함수
    lst = []
    for i in range(1,3+1):
        lst.append( input( "값%d 입력 >> "%(i) ) )
    return lst

result1=get_dic()
result2=get_list()
print(result1)
print(result2)

# 1형식(매개변수 있고, return도 있음)
def convert_to_int(lst): # 리스트의 정수문자열을 정수로 바꾸는 함수
    for i in range(len(lst)):
        lst[i]=int(lst[i])
    return lst
def convert_to_flt(lst): # 리스트의 실수문자열을 실수로 바꾸는 함수
    for i in range(len(lst)):
        lst[i]=float(lst[i])
    return lst
def get_sum_from_lst(lst): # 리스트의 내부의 값들의 합을 구하는 함수
    result = 0
    for value in lst:
        result+=value
    return result
def get_avg_from_lst(lst): # 리스트의 내부의 값들의 평균을 구하는 함수
    result = 0
    for value in lst:
        result+=value
    result/=len(lst)
    return result

sample1=["1","2","3","4","5"]
sample2=["1.1","2.2","3.3","4.4","5.5"]
print( "원본\n%s, %s"%(sample1, sample2) )
sample1=convert_to_int(sample1)
sample2=convert_to_flt(sample2)
print( "변환된 결과물\n%s, %s"%(sample1, sample2) )
sum1=get_sum_from_lst(sample1)
avg1=get_avg_from_lst(sample1)
print("정수리스트의 합/평균 : %d / %.2f"%(sum1, avg1))
sum2=get_sum_from_lst(sample2)
avg2=get_avg_from_lst(sample2)
print("실수리스트의 합/평균 : %d / %.2f"%(sum2, avg2))
