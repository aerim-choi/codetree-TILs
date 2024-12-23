from functools import cmp_to_key

# custom comparator를 직접 정의
# x가 앞에 있는 숫자, y가 뒤에 있는 숫자 가정했을 때
# 이 순서가 우리가 원하는 순서라면 0보다 작은 값을,
# 반대라면 0 보다 큰 값을
# 둘의 우선순위가 동일하다면 0을 반환하면 됩니다.
# 보통 반환값에 1, -1, 0 을 사용합니다

def compare(a,b):
    # a 가 앞에 있다면
    if str(a)+str(b) > str(b)+str(a):
        return -1
    # b가 더 앞에 있어야함 
    if str(b)+str(a) > str(a)+ str(b):
        return 1
    # 우선순위가 동일
    return 0



n = int(input())
arr = []


for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

s = str(arr[0])
for i in range(1, len(arr)):
    a = str(arr[i])
    # 뒤에 붙이기, 앞에 붙이기
    compare_ans = compare( s , a )

    if compare_ans== -1:
        s = s + a
    else : 
        s = a + s

answer = s
print(answer)
