"""한수"""
num = int(input())
hansu = 0

for n in range(1, num+1) :
    if n <= 99: # 1부터 99까지는 모두 한수
        hansu += 1 
    
    else:     
        nums = list(map(int, str(n))) # 숫자를 자릿수대로 분리 
        a = nums[0] - nums[1]
        b = nums[1] - nums[2]
        if a == b :
            hansu+=1