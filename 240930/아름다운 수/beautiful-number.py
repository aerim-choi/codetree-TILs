n = int(input())

result = 0
number_list = []
number_split=[]

#1~4조합의 n자리의 숫자 만들기
def choose_num(curr_idx):
    if curr_idx>n:
        #아름다운 수 인지 체크
        #아름다운 수라면 result+1 
        if check_beautiful_num(number_list):
            global result
            result+=1
        return 
    else:
        for i in range(1,5):
            number_list.append(str(i))
            choose_num(curr_idx+1)
            number_list.pop()
        return 

def check_beautiful_num(number_list):
    i=0
    while i < n:
        #연속한 숫자만큼 올 수 없으면 False
        if i+int(number_list[i])-1 >= n:
            return False 

        # 연속한 숫자만큼 올 수 있으면 아름다운 수 인지 체크하기 
        for j in range(i,i+int(number_list[i])):
            if number_list[i] != number_list[j]:
                return False
        
        i+=int(number_list[i])
    return True


choose_num(1)
print(result)