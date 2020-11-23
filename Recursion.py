def cal_sum(n):

    if n ==1:
        return 1
    else:
        return n + cal_sum(n-1) #called again and again untill n==1


sum = cal_sum(3)    #fuction cal
print(sum)