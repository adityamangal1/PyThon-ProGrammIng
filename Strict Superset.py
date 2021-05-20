set_A=set(map(int,input().split()))
num_other_sets=int(input())
set_list=[]
for i in range(num_other_sets):
    set_other=set(map(int,input().split()))
    set_list.append(set_other)
result=True
for i in set_list:
    if not set_A.issuperset(i):
        result= False
print(result)
