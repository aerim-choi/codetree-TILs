n = int(input())

num_list = list(map(int, input().split()))

#두개의 리스트를 각각 합을 구한 후 차를 구한다.
 
def calc(a_list,b_list):
    return abs(sum(a_list)-sum(b_list))


#두 그룹으로 나누기 (N개중에 중복 없이 N/2 뽑기)
combination_result = []
combination = []
calc_answer = 10000 
def choose(curr_idx, cnt):
    global combination
    global num_list
    global calc_answer
    combination2 = []
    
    if cnt > n/2:
        for i in num_list:
            if i not in combination:
                combination2.append(i)
        calc_answer = min(calc_answer, calc(combination,combination2))
        return
    if curr_idx==len(num_list):
        return 

    
    #선택
    combination.append(num_list[curr_idx])
    choose(curr_idx+1, cnt+1)
    combination.pop()
    
    #선택안함
    choose(curr_idx+1, cnt)

            
choose(0,0)
print(calc_answer)