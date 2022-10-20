# 딕셔너리 : 메서드를 이용하면 편할 수 있다.
dic={"A":1,"B":2,"C":3,"D":4}
for key in dic:
    print("%s : %d\n"%(key, dic[key]))
# 딕셔너리의 일부가 필요할 때?
# keys() / values() 메서드를 이용한다.

# 1) keys() : 딕셔너리의 키만 뽑아서 쓸 수 있도록 준비해준다.
print(dic.keys()) # view라는 목록표(값들)로 나온다.
for key in dic.keys():
    print(key,end=" ")
print()

# 2) values() : 값만 뽑아서 준비해준다.
print(dic.values()) # 쓸려면 list로 형변환이 필수이다.
for value in dic.values(): # 단, for를 쓰면 바로 써먹기 가능
    print(value,end=" ")
print()