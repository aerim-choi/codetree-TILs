n = int(input())

#4개의 수열
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))
c_arr = list(map(int, input().split()))
d_arr = list(map(int, input().split()))

#A+B = -C-D

ab_dict = dict()

for i in range(n):
    for j in range(n):
        a_plus_b = a_arr[i]+b_arr[j]

        if a_plus_b in ab_dict:
            ab_dict[a_plus_b]+=1
        else:
            ab_dict[a_plus_b]=1

answer = 0 
for i in range(n):
    for j in range(n):
        diff = -c_arr[i]-d_arr[j]

        if diff in ab_dict:
            answer += ab_dict[diff]
        
print(answer)